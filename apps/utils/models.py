from django.db import models


class RequestLogModel(models.Model):
    """
    Model to log details of HTTP requests.
    """
    username = models.CharField(max_length=150)
    date_time = models.DateTimeField()
    path = models.CharField(max_length=200)
    method = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.method} - {self.path} {self.date_time}"
