import json
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
        extra_kwargs = {
            'shortDescription': {'required': False, 'allow_blank': True},
            'description': {'required': False, 'allow_blank': True},
            'details': {'required': False, 'allow_blank': True},
            'client': {'required': False, 'allow_blank': True},
            'timeline': {'required': False, 'allow_blank': True},
            'team': {'required': False, 'allow_blank': True},
            'liveUrl': {'required': False, 'allow_blank': True},
            'videoUrl': {'required': False, 'allow_blank': True},
            'testimonial_name': {'required': False, 'allow_blank': True},
            'testimonial_role': {'required': False, 'allow_blank': True},
            'testimonial_image': {'required': False, 'allow_blank': True},
            'testimonial_quote': {'required': False, 'allow_blank': True},
            'image': {'required': False, 'allow_null': True},
        }

    def to_internal_value(self, data):
        # Create a mutable copy
        data = data.copy()
        
        # Handle JSON string conversion for array/object fields
        json_fields = ['technologies', 'challenges', 'outcomes', 'stats', 'gallery']
        
        for field in json_fields:
            if field in data:
                if isinstance(data[field], str):
                    try:
                        # Try to parse as JSON first
                        data[field] = json.loads(data[field])
                    except json.JSONDecodeError:
                        # Fallback parsing
                        if field in ['technologies', 'gallery']:
                            # Comma-separated values
                            data[field] = [item.strip() for item in data[field].split(',') if item.strip()]
                        elif field in ['challenges', 'outcomes']:
                            # Newline-separated values  
                            data[field] = [item.strip() for item in data[field].split('\n') if item.strip()]
                        else:
                            data[field] = {}
                elif isinstance(data[field], list):
                    # Already a list, ensure it's clean
                    data[field] = [item.strip() if isinstance(item, str) else item for item in data[field] if item]
        
        return super().to_internal_value(data)

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