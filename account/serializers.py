from rest_framework import serializers
from .models import TeamMember, Project, GalleryItem

class TeamMemberSerializer(serializers.ModelSerializer):
    joinDate = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = TeamMember
        fields = '__all__'
        extra_kwargs = {
            'education': {'required': False, 'allow_null': True},
            'joinDate': {'required': False, 'allow_null': True},
            'skills': {'required': False},
            'image': {'required': False, 'allow_null': True},  # remove allow_blank
        }

    def validate_status(self, value):
        # normalize frontend input to match choices
        if value.lower() == 'active':
            return 'Active'
        elif value.lower() == 'alumni':
            return 'Alumni'
        raise serializers.ValidationError('Invalid status choice')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = '__all__'
        extra_kwargs = {
            'title': {'required': False, 'allow_blank': True},
            'description': {'required': False, 'allow_blank': True},
            'category': {'required': False},
        }

    def validate_category(self, value):
        valid_categories = ['office', 'events', 'celebration', 'others']
        if value not in valid_categories:
            raise serializers.ValidationError(
                f'Invalid category. Must be one of: {", ".join(valid_categories)}'
            )
        return value