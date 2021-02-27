from django.db import models


class Services(models.Model):

    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    info = models.TextField()

    def __str__(self):
        return self.name