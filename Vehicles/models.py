
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def get_default_profile_image():
    return "codingwithmitch/instlogodefault.png"

class VehiclePermit(models.Model):
    BUILDING_CHOICES = [
        ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'),
        ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'),
        ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'),
        ('M', 'M'), ('N', 'N'), ('O', 'O'), ('P', 'P'),
        ('Q', 'Q'), ('R', 'R'), ('S', 'S'), ('T', 'T'),
        ('U', 'U'), ('Villa', 'Villa'),
    ]

    VEHICLE_TYPE_CHOICES = [
        ('Car', 'Car'),
        ('Bike', 'Bike'),
    ]

    VEHICLE_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Suspended', 'Suspended'),
    ]

    permit_id = models.CharField(max_length=1000, blank=True, null=True, unique=True)
    houseno = models.CharField(max_length=1000, blank=True, null=True)
    building_name = models.CharField(
        max_length=1000,
        choices=BUILDING_CHOICES,
        blank=True,
        null=True,
        default='Main Building'
    )
    description = models.CharField(max_length=1000, blank=True, null=True)
    vehicleno = models.CharField(max_length=1000, blank=True, null=True)
    vehicle_image = models.ImageField(
        max_length=255,
        upload_to='images/',
        null=True,
        blank=True,
        default=get_default_profile_image
    )
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPE_CHOICES, blank=True, null=True)
    status = models.CharField(max_length=10, choices=VEHICLE_STATUS_CHOICES, blank=True, null=True, default='Active')
    house_owner_name = models.CharField(max_length=1000, blank=True, null=True)
    owner_mobile_number = models.CharField(max_length=1000, blank=True, null=True)
    tenant_name = models.CharField(max_length=1000, blank=True, null=True)
    tenant_mobile_number = models.CharField(max_length=1000, blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return self.permit_id or "Unnamed"

    def save(self, *args, **kwargs):
        if self.houseno and self.building_name and self.vehicle_type:
            # Get all vehicles for the house
            permits = VehiclePermit.objects.filter(houseno=self.houseno, building_name=self.building_name)

            # Exclude the current record if it exists (for updates)
            if self.pk:
                permits = permits.exclude(pk=self.pk)

            # Count vehicle types
            car_count = permits.filter(vehicle_type='Car').count()
            bike_count = permits.filter(vehicle_type='Bike').count()

            if self.vehicle_type == 'Car' and car_count >= 1:
                raise ValidationError("A house can have only 1 car.")

            if self.vehicle_type == 'Bike' and bike_count >= 2:
                raise ValidationError("A house can have only 2 bikes.")

        super().save(*args, **kwargs)




