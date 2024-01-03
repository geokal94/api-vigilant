from django.db import models


class Endpoint(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    method = models.CharField(max_length=10)
    headers = models.TextField()
    expected_status = models.IntegerField()
    check_interval = models.DurationField()

    def __str__(self):
        return self.name

class TestResult(models.Model):
    endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)
    status_code = models.IntegerField()
    response_time = models.DurationField()
    response_body = models.TextField()
    passed_validation = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

# Add more models as needed for TestConfiguration, Alert, etc.