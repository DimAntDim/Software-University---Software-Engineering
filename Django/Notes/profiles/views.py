from notes.models import Note
from profiles.models import Profile
from django.shortcuts import redirect, render


def get_profile():
    return Profile.objects.first()

def profile_info(request):
    user = get_profile()
    notes = Note.objects.all()
    context = {
        'user': user,
        'all_notes': len(notes),
    }
    return render(request, 'profile.html', context)
    
def profile_delete(request):
    Profile.objects.all().delete()
    Note.objects.all().delete()
    return redirect('home') 

