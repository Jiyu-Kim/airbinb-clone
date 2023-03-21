from django.db import models
from common.models import CommonModel
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(CommonModel):
    # Review from a User to a Room or Experience

    user = models.ForeignKey(
        to='users.User',
        null=True, 
        on_delete=models.SET_NULL,
    )

    room= models.ForeignKey(
        to='rooms.Room',
        null=True,
        blank=True, 
        on_delete=models.CASCADE,
    )

    experience = models.ForeignKey(
        to='experiences.Experience',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    payload = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

    def __str__(self) -> str:
        if self.rating < 3:
            return f'👎 {self.user} / {self.rating}'
        elif self.rating == 3:
            return f'👌 {self.user} / {self.rating}'
        else:
            return f'👍 {self.user} / {self.rating}'

