import uuid
from django.db import models


# Create your models here.
class AuditGeneration(models.Model):
    uid = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    file_path = models.CharField(max_length=255)
