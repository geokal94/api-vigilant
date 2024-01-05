import requests
from django.utils import timezone

from .models import Endpoint, TestResult


def run_api_test(endpoint_id):
    try:
        endpoint = Endpoint.objects.get(id=endpoint_id)
        
        response = requests.request(
            method=endpoint.method,
            url=endpoint.url,
            headers=endpoint.headers,
            timeout=10
        )
        
        # Calculate response time in milliseconds
        response_time = response.elapsed.total_seconds() * 1000
    
        TestResult.objects.create(
            endpoint=endpoint,
            status_code=response.status_code,
            response_time=response_time,
            timestamp=timezone.now()
        )
        
        return True
    except requests.RequestException as e:
        print(f"An error occurred while testing endpoint {endpoint_id}: {e}")
        return False