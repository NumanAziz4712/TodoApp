from django.db import models
from django.contrib.auth.models import User
class Todos(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=400, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name[:20]
   