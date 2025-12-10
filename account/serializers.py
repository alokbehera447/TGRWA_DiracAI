import json
from rest_framework import serializers
from .models import TeamMember, Project, GalleryItem, Product, ProductGallery

class TeamMemberSerializer(serializers.ModelSerializer):
    joinDate = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = TeamMember
        fields = '__all__'
        extra_kwargs = {
            'education': {'required': False, 'allow_null': True},
            'joinDate': {'required': False, 'allow_null': True},
            'skills': {'required': False},
            'image': {'required': False, 'allow_null': True},
        }

    def validate_status(self, value):
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
        data = data.copy()
        
        json_fields = ['technologies', 'challenges', 'outcomes', 'stats', 'gallery']
        
        for field in json_fields:
            if field in data:
                if isinstance(data[field], str):
                    try:
                        data[field] = json.loads(data[field])
                    except json.JSONDecodeError:
                        if field in ['technologies', 'gallery']:
                            data[field] = [item.strip() for item in data[field].split(',') if item.strip()]
                        elif field in ['challenges', 'outcomes']:
                            data[field] = [item.strip() for item in data[field].split('\n') if item.strip()]
                        else:
                            data[field] = {}
                elif isinstance(data[field], list):
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

# Add ProductGallery Serializer
class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = ['id', 'image', 'created_at']
        read_only_fields = ['id', 'created_at']

# Fixed Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    # Add gallery_images field for reading (not for creation/update)
    gallery_images = ProductGallerySerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'tagline', 'iconText', 'cover', 'description', 
            'fullDescription', 'category', 'status', 'features', 'outcomes',
            'challenges', 'technologies', 'stats', 'gallery_images',  # Changed from 'gallery' to 'gallery_images'
            'platforms', 'integrations', 'support', 'liveUrl', 'demoUrl',
            'documentationUrl', 'featured', 'sortOrder', 'created_at', 'updated_at'
        ]
        extra_kwargs = {
            'description': {'required': False, 'allow_blank': True},
            'fullDescription': {'required': False, 'allow_blank': True},
            'tagline': {'required': False, 'allow_blank': True},
            'iconText': {'required': False, 'allow_blank': True},
            'liveUrl': {'required': False, 'allow_blank': True},
            'demoUrl': {'required': False, 'allow_blank': True},
            'documentationUrl': {'required': False, 'allow_blank': True},
            'cover': {'required': False, 'allow_null': True},
        }

    def to_internal_value(self, data):
        data = data.copy()
        
        # Handle JSON string conversion for array fields (EXCLUDE GALLERY)
        json_fields = [
            'features', 'outcomes', 'challenges', 'technologies', 
            'stats', 'platforms', 'integrations', 'support'
            # REMOVED 'gallery' - we handle gallery images separately via ProductGallery model
        ]
        
        for field in json_fields:
            if field in data:
                if isinstance(data[field], str):
                    try:
                        data[field] = json.loads(data[field])
                    except json.JSONDecodeError:
                        if field in ['technologies', 'platforms', 'integrations', 'support']:
                            data[field] = [item.strip() for item in data[field].split(',') if item.strip()]
                        elif field in ['features', 'outcomes', 'challenges']:
                            data[field] = [item.strip() for item in data[field].split('\n') if item.strip()]
                        elif field == 'stats':
                            if data[field].strip():
                                data[field] = [{"label": "", "value": data[field]}]
                            else:
                                data[field] = []
                        else:
                            data[field] = []
                elif isinstance(data[field], list):
                    data[field] = [item.strip() if isinstance(item, str) else item for item in data[field] if item]
        
        return super().to_internal_value(data)

    def validate_stats(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Stats must be a list")
        
        for stat in value:
            if not isinstance(stat, dict):
                raise serializers.ValidationError("Each stat must be an object")
            if 'label' not in stat or 'value' not in stat:
                raise serializers.ValidationError("Each stat must have 'label' and 'value' fields")
        
        return value

    def create(self, validated_data):
        # Remove gallery_images from validated_data as it's read-only
        validated_data.pop('gallery_images', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Remove gallery_images from validated_data as it's read-only
        validated_data.pop('gallery_images', None)
        return super().update(instance, validated_data)