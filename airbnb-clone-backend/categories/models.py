from django.db import models
from common.models import CommonModel

# Create your models here.

class Category(CommonModel):
    # Room or Experience Category

    class CategoryChoices(models.TextChoices):
        ROOMS = ('rooms', 'Rooms')
        EXPERIENCES = ('experiences', 'Experiences')

    name = models.CharField(max_length=50,)
    kind = models.CharField(max_length=15, choices=CategoryChoices.choices)

    def __str__(self) -> str:
        return f'{self.kind.title()}: {self.name}'
    

    class Meta:
        verbose_name_plural = 'Categories'