from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from posts.models import Post


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    # Added following field for Task 2
    following = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers', blank=True
    )

    # Fix clashes with default Django User
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # changed from default
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # changed from default
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username
