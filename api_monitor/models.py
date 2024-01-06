from django.db import models


class Endpoint(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    method = models.CharField(
        max_length=10,
        choices=[
            ("GET", "GET"),
            ("POST", "POST"),
            ("PUT", "PUT"),
            ("DELETE", "DELETE"),
        ],
    )
    headers = models.JSONField(default=dict)
    check_interval = models.DurationField()

    def __str__(self):
        return self.name


class TestResult(models.Model):
    endpoint = models.ForeignKey(
        Endpoint, related_name="test_results", on_delete=models.CASCADE
    )
    status_code = models.IntegerField()
    response_time = models.FloatField()  # Store response time in seconds
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]
