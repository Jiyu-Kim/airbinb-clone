from django.db import models
from common.models import CommonModel

# Create your models here.

class Wishlist(CommonModel):

    # Wishlist Model Definition
    name = models.CharField(
        max_length=150,
    )

    rooms = models.ManyToManyField(
        to='rooms.Room',
    )

    experiences = models.ManyToManyField(
        to='experiences.Experience',
    )

    user = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.name

