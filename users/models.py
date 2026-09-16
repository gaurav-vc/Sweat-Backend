from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # We can add custom fields here in the future
    is_instructor = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
