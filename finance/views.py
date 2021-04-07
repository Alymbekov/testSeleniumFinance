from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CsvData
from .serializers import FinanceDataSerializer, ParseDataSerializer
from .tasks import selenium_run


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class ParseDataView(APIView):
    """Parse Data"""
    serializer_class = ParseDataSerializer

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }
    ))
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            selenium_run.delay(duration=2, title=title)
            return Response(status=status.HTTP_200_OK, data={"message": "successfully parsed"})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Query is not valid"})


class FinanceDataList(generics.ListAPIView):
    queryset = CsvData.objects.all()
    serializer_class = FinanceDataSerializer
    pagination_class = StandardResultsSetPagination




