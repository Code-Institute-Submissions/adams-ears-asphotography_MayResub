from django.db import models


class ServicesProvided(models.Model):
    service_name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
