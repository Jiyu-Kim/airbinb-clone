from django.db import models
from common.models import CommonModel

# Create your models here.

class Photo(CommonModel):

    file = models.ImageField()

    description = models.CharField(max_length=140,)

    room = models.ForeignKey(
        to='rooms.Room',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    exeprience = models.ForeignKey(
        to='experiences.Experience',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return 'Photo File'

class Video(CommonModel):
    file = models.FileField()

    # video도 하나의 experience에 속하고, experience도 하나의 video만 가질 수 있다. 
    experience = models.OneToOneField(
        to='experiences.Experience',
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return 'Video File'