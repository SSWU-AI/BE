from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id', 'nickname', 'gender', 'birth_date',
            'height', 'weight', 'experience_level', 'preferred_exercise'
        ]
