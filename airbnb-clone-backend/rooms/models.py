from django.db import models
from common.models import CommonModel

# Create your models here.

class Room(CommonModel):

    # Room Model Definition

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ('entire_place', 'Entire Place')
        PRIVATE_ROOM = ('private_room', 'Private Room')
        SHARED_ROOM = 'shared_room', 'Shared Room'

    name = models.CharField(max_length=180, default='')
    country = models.CharField(max_length=50, default='South Korea',)
    city = models.CharField(max_length=80, default='Seoul',)
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilet = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250,)
    pet_friendly = models.BooleanField(default=True,)
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices,)
    owner = models.ForeignKey(to='users.User', on_delete=models.CASCADE,)
    amenities = models.ManyToManyField('rooms.Amenity')
    category = models.ForeignKey(
        to='categories.Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self) -> str:
        return self.name
    

class Amenity(CommonModel):
    # Amenity model definition

    name = models.CharField(max_length=150,)
    description = models.CharField(max_length=150, null=True, blank=True,)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Amenities'