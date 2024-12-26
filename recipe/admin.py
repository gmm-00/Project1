from django.contrib import admin
from .models import * # Use the name 'Recipe' (with an uppercase 'R')

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
	pass

admin.site.register(Recipe, MemberAdmin)
