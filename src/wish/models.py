from django.db import models
from django.contrib.auth.models import User

class Wish(models.Model):
    item = models.CharField(null=True, max_length=150)
    description= models.TextField(null=True)
    granted = models.BooleanField(default=0)
    granted_date = models.DateTimeField(null=True,blank=True)
    user = models.ForeignKey(User, related_name='wish', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item