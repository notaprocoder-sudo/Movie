from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import Movie_edit


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    cont = {
        'movielist': movie
    }
    return render(request, 'index.html', cont)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movie})


def add_mov(request):
    if request.method == 'POST':
        name = request.POST.get('Mov_name')
        rel = request.POST.get('Mov_rel')
        descr = request.POST.get('Mov_desc')
        thb = request.FILES['Mov_img']
        mov = Movie(name=name, Release=rel, Description=descr, Movie_Img=thb)
        mov.save()
    return render(request, 'add.html')


def update(request, id):
    mov = Movie.objects.get(id=id)
    form = Movie_edit(request.POST or None, request.FILES, instance=mov)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {'form': form, 'mov': mov})


def delete(request,id):
    if request.method == 'POST':
        mov = Movie.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render(request,'delete.html')