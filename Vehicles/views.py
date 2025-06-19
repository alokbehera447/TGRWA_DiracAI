
# views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import VehiclePermit
from .serializers import VehiclePermitSerializer
from .utils import generate_qr_code  # ensure this function is defined as shown earlier

class VehiclePermitList(APIView):
    def get(self, request):
        permits = VehiclePermit.objects.all().order_by('id')  # optional ordering

        # Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10  # or use settings
        result_page = paginator.paginate_queryset(permits, request)

        serializer = VehiclePermitSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


    # POST request to create a new vehicle permit
    def post(self, request):
        serializer = VehiclePermitSerializer(data=request.data)
        if serializer.is_valid():
            permit = serializer.save()

            # Build full URL to this permit's detail endpoint
            base_url = request.build_absolute_uri('/')[:-1]  # remove trailing slash
            permit_url = f"{base_url}/permits/{permit.id}/"

            # Generate and attach QR code
            permit.qr_code = generate_qr_code(permit_url)
            permit.save(update_fields=["qr_code"])

            return Response(VehiclePermitSerializer(permit).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehiclePermitDetail(APIView):
    # GET request to fetch a single vehicle permit by ID
    def get(self, request, pk):
        try:
            permit = VehiclePermit.objects.get(pk=pk)
        except VehiclePermit.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = VehiclePermitSerializer(permit)
        return Response(serializer.data)

    # PUT request to update an existing vehicle permit
    def put(self, request, pk):
        try:
            permit = VehiclePermit.objects.get(pk=pk)
        except VehiclePermit.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        print("Incoming PUT data:", request.data)  # <-- Debug line

        serializer = VehiclePermitSerializer(permit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # DELETE request to delete an existing vehicle permit
    def delete(self, request, pk):
        try:
            permit = VehiclePermit.objects.get(pk=pk)
        except VehiclePermit.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        permit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class VehiclePermitSearchAPIView(APIView):
#     def get(self, request):
#         search_query = request.query_params.get('vehicleno', None)

#         if search_query:
#             # Case-insensitive search for vehicleno
#             permits = VehiclePermit.objects.filter(vehicleno__icontains=search_query)
#             serializer = VehiclePermitSerializer(permits, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "No search query provided"}, status=status.HTTP_400_BAD_REQUEST)





class VehiclePermitSearchAPIView(APIView):
    def get(self, request):
        search_query = request.query_params.get('vehicleno', None)

        if not search_query:
            return Response({"error": "No search query provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Filter by search term
        permits = VehiclePermit.objects.filter(vehicleno__icontains=search_query)

        # Paginate results
        paginator = PageNumberPagination()
        paginator.page_size = 10  # Optional: set default page size
        result_page = paginator.paginate_queryset(permits, request)

        # Serialize paginated results
        serializer = VehiclePermitSerializer(result_page, many=True)

        # Return paginated response
        return paginator.get_paginated_response(serializer.data)






