from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from .models import Film, Komentar
from datetime import datetime
import json
import locale

locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
# Create your views here.
def home(request):
    searchByTitle = request.GET.get('query')
    searchByGenre = request.GET.get('genre')
    respons = Komentar.objects.all()
    objects = Film.objects.all()
    redirect = 'home.html'
    # Filter berdasarkan judul jika ada
    if searchByTitle:
        redirect = 'base.html'
        objects = objects.filter(judul__icontains=searchByTitle)
    
    # Filter berdasarkan genre jika ada
    if searchByGenre:
        redirect = 'base.html'
        objects = objects.filter(genre__icontains=searchByGenre)
    
    return render(request, redirect, {'movies': objects, 'reviews': respons})

def detail(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    searchByTitle = request.GET.get('query')
    searchByGenre = request.GET.get('genre')
    objects = Film.objects.all()
    respons = Komentar.objects.all()
    # Filter berdasarkan judul jika ada
    if searchByTitle:
        objects = objects.filter(judul__icontains=searchByTitle)
    
    # Filter berdasarkan genre jika ada
    if searchByGenre:
        objects = objects.filter(genre__icontains=searchByGenre)
    
    if request.method == 'POST':
        nama_pengunjung = request.POST.get('nama_pengunjung')
        isi_komentar = request.POST.get('isi_komentar')
        
        # Menyimpan komentar ke dalam database
        komentar = Komentar(
            film=film,
            nama_pengunjung=nama_pengunjung,
            isi_komentar=isi_komentar
        )
        komentar.save()
        
        # Redirect setelah komentar disimpan
        return redirect('detail', film_id=film.id)
    
    context = {
        'movies': objects,
        'movie': film,
        'reviews': respons,
    }
    return render(request, 'detail.html', context)

def load_more(request):
    offset = int(request.GET.get('offset', 3))
    limit = int(request.GET.get('limit', 3))

    # Ambil data sesuai dengan offset dan limit
    movies = Film.objects.all()[offset:offset+limit]
    
    movie_data = []
    for movie in movies:
        movie_data.append({
            'judul': movie.judul,
            'genre': movie.genre,
            'tahun_rilis': movie.tahun_rilis,
            'sinopsis': movie.sinopsis,
            'poster_url': movie.poster.url,
            'sutradara': movie.sutradara,
            'pemeran': movie.pemeran,
            'detail_url': movie.get_absolute_url(),  # Pastikan ada method get_absolute_url() di model Film
            'sutradara_image': '/static/assets/img/team/team-3.jpg',  # Ganti dengan image sutradara jika ada
        })
    # Cek hasil JSON
    print(json.dumps({'movies': movie_data}, indent=2))
    return JsonResponse({'movies': movie_data})
