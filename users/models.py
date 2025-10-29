from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_indian_phone(value):
    pattern = r'^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$'
    if not re.match(pattern, value):
        raise ValidationError('Enter a valid Indian phone number')

class CustomUser(AbstractUser):
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[validate_indian_phone],
        null=True,  # Make nullable for superuser creation
        blank=True  # Make optional
    )
    date_of_birth = models.DateField(null=True, blank=True)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    
    def __str__(self):
        return self.username