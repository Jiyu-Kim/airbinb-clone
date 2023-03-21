from django.contrib import admin
from .models import Experience, Participation

# Register your models here.

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display =(
        'name',
        'price',
        'start_at',
        'end_at',
        'created_at',
        'updated_at'
    )

    list_filter = (
        'category',
    )

@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at',
        'updated_at'
    )
