import json
from rest_framework import serializers
from django.utils.html import strip_tags

from .models import (
    Testimonial,
    Service,
    TeamMember,
    Project,
    GalleryItem,
    Product,
    ProductGallery,
    Blog,
    BlogCategory,
    BlogComment,
)

# ======================================================
# TEAM MEMBER (UNCHANGED)
# ======================================================

# ======================================================
# ✅ SERVICE SERIALIZER
# ======================================================

class TestimonialSerializer(serializers.ModelSerializer):
    """Serializer for Testimonial model"""
    
    class Meta:
        model = Testimonial
        fields = [
            'id',
            'name',
            'company',
            'role',
            'text',
            'image',
            'linkedin',
            'status',
            'sort_order',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_linkedin(self, value):
        """Validate LinkedIn URL or allow /#"""
        if value and value.strip():
            # Allow "/#" as a special value
            if value == "/#":
                return value
            
            # Also allow empty string
            if value == "":
                return "/#"  # Convert empty string to /# for consistency
            
            # Basic LinkedIn URL validation for actual LinkedIn URLs
            if not (value.startswith('https://linkedin.com/') or 
                    value.startswith('https://www.linkedin.com/')):
                raise serializers.ValidationError(
                    "Please provide a valid LinkedIn URL (starting with https://linkedin.com/) or use /# if not available"
                )
        else:
            # If value is None or empty, use /#
            return "/#"
        return value
    
    def to_representation(self, instance):
        """Ensure /# is returned for empty LinkedIn values"""
        representation = super().to_representation(instance)
        # If linkedin is None or empty in database, return /#
        if not representation.get('linkedin'):
            representation['linkedin'] = "/#"
        return representation

class ServiceSerializer(serializers.ModelSerializer):
    """
    Service Serializer following Product pattern
    """
    
    # Explicit list fields to avoid JSON parsing issues
    features = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_empty=True,
    )
    
    benefits = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_empty=True,
    )
    
    technologies = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_empty=True,
    )
    
    # Developers as IDs (can be extended to nested serializers later)
    developers = serializers.PrimaryKeyRelatedField(
        queryset=TeamMember.objects.all(),
        many=True,
        required=False
    )
    
    class Meta:
        model = Service
        fields = [
            'id',
            'title',
            'description',
            # 'icon_name',
            'image',
            'long_description',
            'features',
            'benefits',
            'technologies',
            'developers',
            'demo_video_url',
            'status',
            'sort_order',
            'created_at',
            'updated_at',
        ]
    
    def to_internal_value(self, data):
        """
        Handle FormData lists like your ProductSerializer
        """
        data = data.copy()
        
        # Handle JSON fields from FormData
        list_fields = ['features', 'benefits', 'technologies', 'developers']
        
        def normalize_string_list(value):
            if isinstance(value, list):
                return [str(item).strip() for item in value if str(item).strip()]
            if isinstance(value, str):
                try:
                    parsed = json.loads(value)
                    if isinstance(parsed, list):
                        return [str(item).strip() for item in parsed if str(item).strip()]
                except json.JSONDecodeError:
                    # Comma-separated or newline-separated strings
                    items = []
                    for line in value.split('\n'):
                        items.extend([item.strip() for item in line.split(',') if item.strip()])
                    return items
            return []
        
        for field in list_fields:
            if field in data:
                data[field] = normalize_string_list(data[field])
        
        return super().to_internal_value(data)

class TeamMemberSerializer(serializers.ModelSerializer):
    joinDate = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = TeamMember
        fields = "__all__"
        extra_kwargs = {
            "education": {"required": False, "allow_null": True},
            "joinDate": {"required": False, "allow_null": True},
            "skills": {"required": False},
            "image": {"required": False, "allow_null": True},
        }

    def validate_status(self, value):
        value = value.lower()
        if value == "active":
            return "Active"
        if value == "alumni":
            return "Alumni"
        raise serializers.ValidationError("Invalid status choice")


# ======================================================
# PROJECT (UNCHANGED)
# ======================================================
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

# ======================================================
# SITE GALLERY (UNCHANGED)
# ======================================================
class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = "__all__"


# ======================================================
# ✅ PRODUCT GALLERY (FINAL – SAFE)
# ======================================================
class ProductGallerySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = ProductGallery
        fields = ["id", "image", "created_at"]
        read_only_fields = fields


# ======================================================
# ✅ PRODUCT SERIALIZER (FINAL FIX)
# ======================================================
class ProductSerializer(serializers.ModelSerializer):
    """
    🔒 EXPLICIT LIST FIELDS
    This avoids DRF JSONField auto-parsing issues with FormData
    """

    features = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_empty=True,
    )

    outcomes = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_empty=True,
    )

    challenges = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_empty=True,
    )

    technologies = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_empty=True,
    )

    stats = serializers.ListField(
        child=serializers.DictField(),
        required=False,
        allow_empty=True,
    )

    platforms = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_empty=True,
    )

    integrations = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_empty=True,
    )

    support = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_empty=True,
    )

    # 🔗 Gallery (read-only, created in view)
    gallery_images = ProductGallerySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "tagline",
            "iconText",
            "cover",
            "description",
            "fullDescription",
            "category",
            "status",
            "features",
            "outcomes",
            "challenges",
            "technologies",
            "stats",
            "platforms",
            "integrations",
            "support",
            "liveUrl",
            "demoUrl",
            "documentationUrl",
            "featured",
            "sortOrder",
            "gallery_images",
            "created_at",
            "updated_at",
        ]


    # --------------------------------------------------
    # 🔥 CRITICAL NORMALIZER (THE REAL FIX)
    # --------------------------------------------------
    def to_internal_value(self, data):
        """
        Accepts:
        - JSON strings: '["React"]'
        - FormData lists: ["React"]
        - Empty strings / junk safely
        """
        data = data.copy()

        list_fields = [
            "features",
            "outcomes",
            "challenges",
            "technologies",
            "stats",
            "platforms",
            "integrations",
            "support",
        ]

        def flatten(items):
            flattened = []
            for item in items:
                if isinstance(item, list):
                    flattened.extend(flatten(item))
                else:
                    flattened.append(item)
            return flattened

        def normalize_string_list(value):
            if isinstance(value, list):
                value = flatten(value)
                cleaned = []
                for item in value:
                    if item in ["", None]:
                        continue
                    if isinstance(item, str):
                        text = item.strip()
                        if text == "":
                            continue
                        try:
                            parsed = json.loads(text)
                        except json.JSONDecodeError:
                            cleaned.append(text)
                            continue
                        if isinstance(parsed, list):
                            cleaned.extend(normalize_string_list(parsed))
                            continue
                        if isinstance(parsed, (str, int, float, bool)):
                            cleaned.append(str(parsed))
                            continue
                        continue
                    if isinstance(item, (int, float, bool)):
                        cleaned.append(str(item))
                        continue
                return cleaned
            if isinstance(value, str):
                text = value.strip()
                if text == "":
                    return []
                try:
                    parsed = json.loads(text)
                except json.JSONDecodeError:
                    return []
                if isinstance(parsed, list):
                    return normalize_string_list(parsed)
                return []
            return []

        def normalize_stats_list(value):
            if isinstance(value, list):
                value = flatten(value)
                cleaned = []
                for item in value:
                    if item in ["", None]:
                        continue
                    if isinstance(item, str):
                        text = item.strip()
                        if text == "":
                            continue
                        try:
                            parsed = json.loads(text)
                        except json.JSONDecodeError:
                            continue
                        if isinstance(parsed, dict):
                            cleaned.append(parsed)
                            continue
                        if isinstance(parsed, list):
                            cleaned.extend(normalize_stats_list(parsed))
                            continue
                        continue
                    if isinstance(item, dict):
                        cleaned.append(item)
                        continue
                return cleaned
            if isinstance(value, str):
                try:
                    parsed = json.loads(value)
                    if isinstance(parsed, list):
                        return normalize_stats_list(parsed)
                except json.JSONDecodeError:
                    return []
            return []

        url_fields = ["liveUrl", "demoUrl", "documentationUrl"]
        for field in url_fields:
            if field not in data:
                continue
            value = data[field]
            if not isinstance(value, str):
                continue
            text = value.strip()
            if len(text) >= 2 and text[0] == "`" and text[-1] == "`":
                text = text[1:-1].strip()
            data[field] = text

        for field in list_fields:
            if field not in data:
                continue

            value = data[field]

            if field == "stats":
                data[field] = normalize_stats_list(value)
                continue

            data[field] = normalize_string_list(value)

        return super().to_internal_value(data)


    # --------------------------------------------------
    # Stats validation (kept strict)
    # --------------------------------------------------
    def validate_stats(self, value):
        for stat in value:
            if not isinstance(stat, dict):
                raise serializers.ValidationError("Each stat must be an object")
            if "label" not in stat or "value" not in stat:
                raise serializers.ValidationError(
                    "Each stat must have 'label' and 'value'"
                )
        return value


    # Prevent nested writes (gallery handled separately)
    def create(self, validated_data):
        validated_data.pop("gallery_images", None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop("gallery_images", None)
        return super().update(instance, validated_data)

     # ============================
# Blog Serializers (NEW)
# ============================



class PublicBlogSerializer(serializers.ModelSerializer):
    """
    Serializer used by frontend (/blog page).
    Safe, explicit, and frontend-compatible.
    """

    tags = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    readingTime = serializers.SerializerMethodField()
    featured = serializers.BooleanField()

    class Meta:
        model = Blog
        fields = [
            "id",
            "slug",
            "title",
            "excerpt",
            "content",
            "category",
            "tags",
            "image",
            "author",
            "date",
            "readingTime",
            "featured",
        ]

    def get_tags(self, obj):
        # Supports CharField or JSONField
        if not obj.tags:
            return []
        if isinstance(obj.tags, list):
            return obj.tags
        return [t.strip() for t in obj.tags.split(",") if t.strip()]

    def get_author(self, obj):
        avatar_url = ""
        if getattr(obj, "author_avatar", None):
            try:
                avatar_url = obj.author_avatar.url
            except Exception:
                avatar_url = ""
        if not avatar_url:
            avatar_url = getattr(obj, "author_avatar_url", "") or ""
        return {
            "name": obj.author_name or "",
            "role": obj.author_role or "",
            "avatar": avatar_url,
        }

    def get_image(self, obj):
        if getattr(obj, "banner_image", None):
            try:
                return obj.banner_image.url
            except Exception:
                pass
        return getattr(obj, "banner_image_url", "") or ""

    def get_date(self, obj):
        # Frontend expects readable string
        return obj.published_at.strftime("%b %d, %Y") if obj.published_at else ""

    def get_readingTime(self, obj):
        # Approx: 200 words per minute
        if not obj.content:
            return 1
        words = len(obj.content.split())
        return max(1, round(words / 200))
# ✅ ADMIN BLOG SERIALIZER (Writable)
class BlogAdminSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_empty=True,
    )

    def to_internal_value(self, data):
        if hasattr(data, "getlist"):
            normalized = {}
            for key in data.keys():
                values = data.getlist(key)
                if len(values) == 1:
                    normalized[key] = values[0]
                else:
                    normalized[key] = values
            data = normalized
        else:
            data = data.copy()

        if "tags" in data:
            value = data["tags"]
            if isinstance(value, str):
                text = value.strip()
                if text:
                    try:
                        parsed = json.loads(text)
                        if isinstance(parsed, list):
                            data["tags"] = [str(x).strip() for x in parsed if str(x).strip()]
                        else:
                            data["tags"] = [t.strip() for t in text.split(",") if t.strip()]
                    except json.JSONDecodeError:
                        data["tags"] = [t.strip() for t in text.split(",") if t.strip()]
                else:
                    data["tags"] = []
            elif isinstance(value, list):
                cleaned = []
                for item in value:
                    if item in ["", None]:
                        continue
                    if isinstance(item, str):
                        s = item.strip()
                        if not s:
                            continue
                        try:
                            parsed = json.loads(s)
                            if isinstance(parsed, list):
                                cleaned.extend([str(x).strip() for x in parsed if str(x).strip()])
                                continue
                        except json.JSONDecodeError:
                            pass
                        cleaned.append(s)
                    else:
                        cleaned.append(str(item).strip())
                data["tags"] = [t for t in cleaned if t]
            else:
                data["tags"] = []

        return super().to_internal_value(data)

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "slug",
            "excerpt",
            "content",
            "category",
            "tags",
            "banner_image",
            "banner_image_url",
            "author_name",
            "author_avatar",
            "author_avatar_url",
            "author_role",
            "status",
            "featured",
            "meta_title",
            "meta_description",
            "canonical_url",
            "allow_indexing",
            "created_at",
            "updated_at",
            "published_at",
        ]
        read_only_fields = ["created_at", "updated_at", "published_at"]


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ["id", "name", "slug"]


class BlogCommentSerializer(serializers.ModelSerializer):
    blog = serializers.SlugRelatedField(read_only=True, slug_field="slug")

    class Meta:
        model = BlogComment
        fields = ["id", "blog", "name", "content", "created_at"]
        read_only_fields = fields


class BlogCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = ["name", "email", "content"]

    def validate_name(self, value):
        value = (value or "").strip()
        if not value:
            raise serializers.ValidationError("Name is required")
        if len(value) > 120:
            raise serializers.ValidationError("Name is too long")
        return value

    def validate_content(self, value):
        value = value or ""
        cleaned = strip_tags(value).strip()
        if not cleaned:
            raise serializers.ValidationError("Content is required")
        if len(cleaned) > 5000:
            raise serializers.ValidationError("Content is too long")
        return cleaned


class BlogCommentAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = [
            "id",
            "blog",
            "user",
            "name",
            "email",
            "content",
            "status",
            "ip_address",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]
