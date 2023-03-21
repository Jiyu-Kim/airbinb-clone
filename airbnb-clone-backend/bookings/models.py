from django.db import models
from common.models import CommonModel

# Create your models here.

class Booking(CommonModel):
    # Booking Model Definition

    class BookingKindChoices(models.TextChoices):
        ROOM = 'room', 'Room'
        EXPERIENCE = 'experience', 'Experience'

    kind = models.CharField(
        max_length=15, 
        choices=BookingKindChoices.choices
    )

    user = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
    )

    room = models.ForeignKey(
        to='rooms.Room',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    experience = models.ForeignKey(
        to='experiences.Experience',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    guests = models.PositiveIntegerField()
    
    # When an user books a room
    check_in = models.DateField(
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )

    # When an user books an experience
    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        if self.kind == 'room':
            return f'🏠 {self.kind.title()} booking for: {self.user}'
        else:
            return f'🏄‍♀️ {self.kind.title()} booking for: {self.user}'

