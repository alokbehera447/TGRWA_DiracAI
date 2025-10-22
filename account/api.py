# account/api.py
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
        return Response({"msg": "ok", "user": request.user.username})

# class TeamAPI(APIView):
#     permission_classes = [IsAuthenticated]
#     parser_classes = [MultiPartParser, FormParser]
#     def get(self, request):
#         members = TeamMember.objects.all()
#         serializer = TeamMemberSerializer(members, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         print("DEBUG: request.data =", request.data)
#         serializer = TeamMemberSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         print(serializer.errors) 
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TeamDetailAPI(APIView):
#     permission_classes = [IsAuthenticated]

#     def put(self, request, pk):
#         member = TeamMember.objects.get(id=pk)
#         serializer = TeamMemberSerializer(member, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        member = TeamMember.objects.get(id=pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# ------------------ PROJECT API ------------------
class ProjectAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            project = Project.objects.get(id=pk)
        except Project.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            project = Project.objects.get(id=pk)
        except Project.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class GalleryDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

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
