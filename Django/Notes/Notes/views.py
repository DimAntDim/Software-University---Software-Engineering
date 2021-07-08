from notes.forms import AddNoteForm, DeleteNoteForm, EditNoteForm
from profiles.forms import FormCreateProfile
from notes.models import Note
from profiles.models import Profile
from django.shortcuts import redirect, render


def home_page(request):
    user = Profile.objects.first()
    if user:
        notes = Note.objects.all()
        context = {
            'notes': notes
        }
        return render(request, 'home-with-profile.html', context)
    else:
        if request.method == 'POST':
            form = FormCreateProfile(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {
            'form': FormCreateProfile()
        }
        return render(request, 'home-no-profile.html', context)

def add_note(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': AddNoteForm()
    }
    return render(request, 'note-create.html', context)

def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditNoteForm(initial=note.__dict__)

    context = {
        'note': note,
        'form': form,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteNoteForm(
            initial=note.__dict__,
            )
        return render(request, 'note-delete.html', {'form': form})
    else:
        note.delete()
        return redirect('home')

def note_details(request, pk):
    context = {
        'note': Note.objects.get(pk=pk),
    }
    return render(request, 'note-details.html', context)

