from notes.views import add_note, delete_note, edit_note, home_page, note_details
from django.urls import path


urlpatterns = [
    path('', home_page, name='home'),
    path('add/', add_note, name='add'),
    path('edit/<int:pk>', edit_note, name='edit'),
    path('delete/<int:pk>', delete_note, name='delete'),
    path('details/<int:pk>', note_details, name='details'),
]