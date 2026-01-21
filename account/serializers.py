import json
from rest_framework import serializers
from .models import (
    TeamMember,
    Project,
    GalleryItem,
    Product,
    ProductGallery,
)

# ======================================================
# TEAM MEMBER (UNCHANGED)
# ======================================================
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
