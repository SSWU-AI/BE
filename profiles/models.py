from django.db import models
from django.conf import settings

class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', '남성'),
        ('F', '여성'),
        ('O', '기타'),
    )

    EXPERIENCE_LEVEL_CHOICES = (
        ('beginner', '초보'),
        ('intermediate', '중급'),
        ('advanced', '고급'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True, help_text='cm 단위')
    weight = models.FloatField(null=True, blank=True, help_text='kg 단위')
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL_CHOICES, blank=True)
    preferred_exercise = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nickname or self.user.username
