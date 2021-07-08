from profiles.views import profile_info, profile_delete
from django.urls import path


urlpatterns = [
    path('', profile_info, name='profile'),
    path('delete/', profile_delete, name='delete')
]