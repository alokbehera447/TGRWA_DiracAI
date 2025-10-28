# account/api.py
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import TeamMember, Project, GalleryItem
from .serializers import TeamMemberSerializer, ProjectSerializer, GalleryItemSerializer


class AdminDashboardAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # optional: ensure staff/superuser
        if not (request.user.is_staff or request.user.is_superuser):
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        
        # Return admin user details
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
    # permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return []  # No authentication required for GET
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
        # Handle file upload and JSON data
        data = {key: value for key, value in request.data.items()}
        
        print("=== DEBUG: REQUEST DATA ===")
        print(f"Method: {request.method}")
        print(f"Instance: {instance}")
        for key, value in data.items():
            print(f"{key}: {repr(value)} (type: {type(value)})")

        # Process JSON fields for both string and array formats
        json_fields = ['technologies', 'challenges', 'outcomes', 'stats', 'gallery']

        for field in json_fields:
            if field in data:
                field_value = data[field]
                print(f"Processing {field}: {repr(field_value)} (type: {type(field_value)})")

                if isinstance(field_value, str):
                    try:
                        # Try to parse as JSON first
                        data[field] = json.loads(field_value)
                        print(f"  -> Parsed as JSON: {data[field]}")
                    except json.JSONDecodeError:
                        # Fallback parsing for different formats
                        if field in ['technologies', 'gallery']:
                            # Comma-separated values
                            data[field] = [item.strip() for item in field_value.split(',') if item.strip()]
                            print(f"  -> Parsed as comma-separated: {data[field]}")
                        elif field in ['challenges', 'outcomes']:
                            # Newline-separated values  
                            data[field] = [item.strip() for item in field_value.split('\n') if item.strip()]
                            print(f"  -> Parsed as newline-separated: {data[field]}")
                        else:
                            data[field] = {}
                elif isinstance(field_value, list):
                    # Already a list, ensure it's clean
                    data[field] = [item.strip() if isinstance(item, str) else item for item in field_value if item]
                    print(f"  -> Already a list: {data[field]}")
                else:
                    # If it's neither string nor list, set to empty
                    data[field] = []
                    print(f"  -> Set to empty list")

        print("=== DEBUG: PROCESSED DATA ===")
        for key, value in data.items():
            if key in json_fields:
                print(f"{key}: {repr(value)}")

    # ... rest of your method ...

        # Handle empty values
        for field in json_fields:
            if field not in data or data[field] is None:
                data[field] = [] if field in ['technologies', 'challenges', 'outcomes', 'gallery'] else {}

        print("Processed data:", data)  # Debug log

        # Create or update the project
        if instance:
            serializer = ProjectSerializer(instance, data=data, partial=False)
        else:
            serializer = ProjectSerializer(data=data)
            
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK if instance else status.HTTP_201_CREATED)
        
        print("Serializer errors:", serializer.errors)  # Debug log
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ------------------ GALLERY API ------------------
class GalleryAPI(APIView):
    permission_classes = [IsAuthenticated]

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


# ------------------ GALLERY API ------------------
class GalleryAPI(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return []  # No authentication required for GET
        return [IsAuthenticated()]  # Authentication required for POST, etc.

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
            return []  # No authentication required for GET
        return [IsAuthenticated()]  # Authentication required for PUT, DELETE

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
