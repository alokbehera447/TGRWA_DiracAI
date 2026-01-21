import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import TeamMember, Project, GalleryItem, Product, ProductGallery
from .serializers import TeamMemberSerializer, ProjectSerializer, GalleryItemSerializer, ProductSerializer, ProductGallerySerializer


class AdminDashboardAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not (request.user.is_staff or request.user.is_superuser):
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        
        return Response({
            "msg": "ok", 
            "user": {
                "id": request.user.id,
                "username": request.user.username,
                "email": request.user.email,
                "phoneno": request.user.phoneno,
            }
        })

    def delete(self, request, pk):
        member = TeamMember.objects.get(id=pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------ PROJECT API ------------------
class ProjectAPI(APIView):
    parser_classes = [MultiPartParser, FormParser]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [IsAuthenticated()] 
    
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        return self.handle_project_request(request)
    
    def put(self, request, pk=None):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        return self.handle_project_request(request, project)

    def delete(self, request, pk=None):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def handle_project_request(self, request, instance=None):
        data = {key: value for key, value in request.data.items()}
        
        json_fields = ['technologies', 'challenges', 'outcomes', 'stats', 'gallery']

        for field in json_fields:
            if field in data:
                field_value = data[field]

                if isinstance(field_value, str):
                    try:
                        data[field] = json.loads(field_value)
                    except json.JSONDecodeError:
                        if field in ['technologies', 'gallery']:
                            data[field] = [item.strip() for item in field_value.split(',') if item.strip()]
                        elif field in ['challenges', 'outcomes']:
                            data[field] = [item.strip() for item in field_value.split('\n') if item.strip()]
                        else:
                            data[field] = {}
                elif isinstance(field_value, list):
                    data[field] = [item.strip() if isinstance(item, str) else item for item in field_value if item]
                else:
                    data[field] = []

        for field in json_fields:
            if field not in data or data[field] is None:
                data[field] = [] if field in ['technologies', 'challenges', 'outcomes', 'gallery'] else {}

        if instance:
            serializer = ProjectSerializer(instance, data=data, partial=False)
        else:
            serializer = ProjectSerializer(data=data)
            
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK if instance else status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------ GALLERY API ------------------
class GalleryAPI(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [IsAuthenticated()]

    def get(self, request):
        images = GalleryItem.objects.all().order_by("-created_at")
        serializer = GalleryItemSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GalleryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GalleryDetailAPI(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [IsAuthenticated()]

    def get(self, request, pk):
        try:
            item = GalleryItem.objects.get(id=pk)
            serializer = GalleryItemSerializer(item)
            return Response(serializer.data)
        except GalleryItem.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            item = GalleryItem.objects.get(id=pk)
        except GalleryItem.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = GalleryItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            item = GalleryItem.objects.get(id=pk)
        except GalleryItem.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------ PRODUCT API (COMPLETELY REWRITTEN) ------------------
class ProductAPI(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [IsAuthenticated()]

    def get(self, request, pk=None):
        queryset = Product.objects.prefetch_related('gallery_images')

        if pk:
            try:
                product = queryset.get(pk=pk)
            except Product.DoesNotExist:
                return Response({'error': 'Product not found'}, status=404)
            return Response(ProductSerializer(product).data)

        return Response(ProductSerializer(queryset.all(), many=True).data)

    def post(self, request):
        return self._save_product(request)

    def put(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)
        return self._save_product(request, instance=product)

    def delete(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response(status=204)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)

    def _save_product(self, request, instance=None):
        list_fields = [
            'features', 'outcomes', 'challenges',
            'technologies', 'stats',
            'platforms', 'integrations', 'support'
        ]

        incoming = request.data
        data = {}
        for key in incoming.keys():
            if key.startswith('gallery_'):
                continue
            if key in list_fields:
                continue
            data[key] = incoming.get(key)

        def _append_gallery_files(files):
            for f in files:
                if f:
                    gallery_files.append(f)

        gallery_files = []
        for key in request.FILES:
            if key.startswith('gallery_'):
                _append_gallery_files([request.FILES[key]])

        if hasattr(request.FILES, "getlist"):
            for key in ["gallery", "gallery[]", "images", "images[]"]:
                _append_gallery_files(request.FILES.getlist(key))

        def _strip_backticks(value):
            if not isinstance(value, str):
                return value
            text = value.strip()
            if len(text) >= 2 and text[0] == "`" and text[-1] == "`":
                return text[1:-1].strip()
            return text

        for url_field in ['liveUrl', 'demoUrl', 'documentationUrl']:
            if url_field in data:
                data[url_field] = _strip_backticks(data[url_field])

        def _coerce_scalar_to_str(value):
            if isinstance(value, (str, int, float, bool)):
                return str(value).strip()
            return None

        def _json_loads_if_possible(value):
            if not isinstance(value, str):
                return None
            text = value.strip()
            if text == "":
                return None
            try:
                return json.loads(text)
            except json.JSONDecodeError:
                return None

        for field in list_fields:
            if hasattr(incoming, "getlist"):
                raw_values = incoming.getlist(field)
            else:
                raw_values = incoming.get(field)

            if raw_values is None:
                continue

            raw_queue = raw_values if isinstance(raw_values, list) else [raw_values]

            if field == "stats":
                normalized_stats = []
                queue = list(raw_queue)
                while queue:
                    raw = queue.pop(0)
                    if raw in ["", None]:
                        continue
                    if isinstance(raw, dict):
                        normalized_stats.append(raw)
                        continue
                    if isinstance(raw, list):
                        queue = list(raw) + queue
                        continue
                    parsed = _json_loads_if_possible(raw)
                    if isinstance(parsed, dict):
                        normalized_stats.append(parsed)
                        continue
                    if isinstance(parsed, list):
                        queue = list(parsed) + queue
                        continue
                data[field] = normalized_stats
                continue

            normalized_strings = []
            queue = list(raw_queue)
            while queue:
                raw = queue.pop(0)
                if raw in ["", None]:
                    continue
                if isinstance(raw, list):
                    queue = list(raw) + queue
                    continue
                parsed = _json_loads_if_possible(raw)
                if isinstance(parsed, list):
                    queue = list(parsed) + queue
                    continue
                scalar = _coerce_scalar_to_str(parsed if parsed is not None else raw)
                if scalar:
                    normalized_strings.append(scalar)
            data[field] = normalized_strings

        serializer = (
            ProductSerializer(instance, data=data, partial=True)
            if instance else ProductSerializer(data=data)
        )

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        product = serializer.save()

        # 🔥 IMPORTANT: Handle gallery images
        if gallery_files:
            if instance:
                # Clear existing gallery if new files are uploaded
                product.gallery_images.all().delete()
            
            for img in gallery_files:
                ProductGallery.objects.create(product=product, image=img)

        # 🔹 Re-fetch with gallery
        product = Product.objects.prefetch_related('gallery_images').get(pk=product.pk)

        return Response(
            ProductSerializer(product).data,
            status=200 if instance else 201
        )


# ------------------ PRODUCT GALLERY API ------------------
class ProductGalleryAPI(APIView):
    parser_classes = [MultiPartParser, FormParser]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [IsAuthenticated()]

    def get(self, request, product_pk=None, gallery_pk=None):
        if not product_pk and not gallery_pk:
            gallery_images = ProductGallery.objects.all().order_by("-created_at")
            serializer = ProductGallerySerializer(gallery_images, many=True)
            return Response(serializer.data)
        
        elif product_pk and not gallery_pk:
            gallery_images = ProductGallery.objects.filter(product_id=product_pk).order_by("-created_at")
            serializer = ProductGallerySerializer(gallery_images, many=True)
            return Response(serializer.data)
        
        elif gallery_pk:
            try:
                gallery_item = ProductGallery.objects.get(pk=gallery_pk)
                serializer = ProductGallerySerializer(gallery_item)
                return Response(serializer.data)
            except ProductGallery.DoesNotExist:
                return Response({'error': 'Gallery image not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, product_pk=None):
        if not product_pk:
            return Response({'error': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            product = Product.objects.get(pk=product_pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        gallery_files = request.FILES.getlist('images')
        created_images = []
        
        for gallery_file in gallery_files:
            gallery_item = ProductGallery.objects.create(
                product=product,
                image=gallery_file
            )
            created_images.append(ProductGallerySerializer(gallery_item).data)
        
        return Response(created_images, status=status.HTTP_201_CREATED)

    def delete(self, request, gallery_pk=None, product_pk=None):
        if not gallery_pk:
            return Response({'error': 'Gallery image ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            gallery_item = ProductGallery.objects.get(pk=gallery_pk)
        except ProductGallery.DoesNotExist:
            return Response({'error': 'Gallery image not found'}, status=status.HTTP_404_NOT_FOUND)
        
        gallery_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
