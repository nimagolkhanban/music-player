from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ACCOUNT_TYPES = (
        ('N', 'Normal'),
        ('V', 'VIP'),
    )
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPES, default='N')
    image = models.ImageField(upload_to='users/', null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users table"
