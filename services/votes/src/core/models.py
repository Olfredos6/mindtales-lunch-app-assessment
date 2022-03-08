from django.db import models
import uuid


class Vote(models.Model):
    date_casted: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )
    id: models.UUIDField = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    employee: models.EmailField = models.EmailField()
    menu: models.UUIDField = models.UUIDField()

    class Meta:
        unique_together = ['employee', 'menu']
