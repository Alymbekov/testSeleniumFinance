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

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            #TODO add click functional
            download_url = "https://query1.finance.yahoo.com/v7/finance/download/ZUO?period1=1523491200&period2=" \
                           "1617235200&interval=1d&events=history&includeAdjustedClose=true"
            selenium_run.delay(duration=2, download_url=download_url, title=title)
            return Response(status=status.HTTP_200_OK, data={"message": "successfully parsed"})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Query is not valid"})


class FinanceDataList(generics.ListAPIView):
    queryset = CsvData.objects.all()
    serializer_class = FinanceDataSerializer
    pagination_class = StandardResultsSetPagination




