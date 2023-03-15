from django.db import models

# Create your models here.
class House(models.Model):

    #Model Definition for houses

    name = models.CharField(max_length=140) #name should be string within 140 length.
    price_per_night = models.PositiveIntegerField(verbose_name="Price", help_text="Positive numbers only") #price should be positive integer.
    description = models.TextField() # description should be text.
    address = models.CharField(max_length=140)
    pet_allowed = models.BooleanField(
        verbose_name="Pets Allowed?",
        default=True ,
        help_text="Does this house allowed pets?"
    )

    def __str__(self):
        return self.name