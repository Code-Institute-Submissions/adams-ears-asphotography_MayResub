from django.db import models


class ContactForm(models.Model):
    """
      Services provided by photographer for dropdown contact form
    """
    portait_photo = models.CharField(max_length=20,  blank=True)
    event_photo = models.CharField(max_length=20,  blank=True)
    property_photo = models.CharField(max_length=20,  blank=True)


def __str__(self):
    return self.title
