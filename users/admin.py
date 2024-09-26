from django.contrib import admin
from .models import Profile
# Register your models here.
#from .models import User

from django.contrib.auth import get_user_model
User = get_user_model()

admin.site.register(User)
# Path: backend/users/models.py

admin.site.register(Profile)
