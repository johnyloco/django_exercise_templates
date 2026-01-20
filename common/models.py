from django.db import models

class TimeStampModel(models.Model):
    class Meta:
        abstract = True

    # auto_now_add sets the timestamp only when the object is first created
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )