from django.db import models
from django.contrib.auth.models import User
import uuid

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notify_time = models.DateTimeField()
    tablet_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    total_tablet_quantity = models.PositiveIntegerField()
    last_updated_time = models.DateTimeField()