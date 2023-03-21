from django.db import models
from common.models import CommonModel

# Create your models here.

class Experience(CommonModel):
    # Experience Model Definition

    country = models.CharField(
        max_length=50, 
        default='South Korea',
    )

    city = models.CharField(
        max_length=80, 
        default='Seoul',
    )

    name = models.CharField(
        max_length=250,
    )

    host = models.ForeignKey(
        to='users.User', 
        on_delete=models.CASCADE
    )

    price = models.PositiveIntegerField()

    address = models.CharField(
        max_length=250,
    )

    start_at = models.TimeField()

    end_at = models.TimeField()

    description = models.TextField()

    participations = models.ManyToManyField(
        'experiences.Participation'
    )

    category = models.ForeignKey(
        to='categories.Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self) -> str:
        return self.name



class Participation(CommonModel):
    # Hot to Participate in an experience
    
    name = models.CharField(max_length=100, null=True, blank=True,)
    explanation = models.TextField(null=True, blank=True,)

    def __str__(self) -> str:
        return self.name