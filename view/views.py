from django.shortcuts import render, get_object_or_404
from onenote.models import Note
from django.http.request import HttpRequest
from .forms import NoteForm
from django.conf import settings

def create_note(request:HttpRequest):
    form = NoteForm(request.POST)
    context = {'form':form}
    if form.is_valid():
        form.save()
        context['content'] = 'فرم به درستی ارسال شد.'
        context['url'] = settings.BASE_URL+'view/'+Note.objects.last().slug
    return render(request,'view/create.html',context)

def home_page(request:HttpRequest):
    return render(request,'view/home.html')

def about_page(request:HttpRequest):
    return render(request,'view/about.html')

def view_note(request:HttpRequest, slug):
    print(slug,'\n\n\n\n\n\n')
    note:Note = get_object_or_404(Note, slug=slug)
    note.count -= 1
    note.save()
    if note.count == 0:
        note.delete()
    context={'note':note}
    return render(request,'view/view_note.html',context)