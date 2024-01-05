from rest_framework import generics

from .models import Endpoint, TestResult
from .serializers import EndpointSerializer, TestResultSerializer


class EndpointListCreateView(generics.ListCreateAPIView):
    queryset = Endpoint.objects.all()
    serializer_class = EndpointSerializer

class EndpointDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Endpoint.objects.all()
    serializer_class = EndpointSerializer

class TestResultListView(generics.ListAPIView):
    serializer_class = TestResultSerializer

    def get_queryset(self):
        endpoint_id = self.kwargs['endpoint_id']
        return TestResult.objects.filter(endpoint_id=endpoint_id)