from django.db import models
from django.urls import reverse

# Create your models here.
class Film(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('Horror', 'Horror'),
        ('Romance', 'Romance'),
        ('Sci-Fi', 'Sci-Fi'),
        # Tambahkan genre lainnya jika diperlukan
    ]

    judul = models.CharField(max_length=100, verbose_name="Judul Film")  # Nama Film
    sinopsis = models.TextField(blank=True, verbose_name="Sinopsis")  # Deskripsi
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, verbose_name="Genre")
    tahun_rilis = models.IntegerField(verbose_name="Tahun Rilis")
    sutradara = models.CharField(max_length=50, verbose_name="Sutradara")  # Panjang nama lebih fleksibel
    pemeran = models.TextField(blank=True, verbose_name="Daftar Pemeran")  # Atau gunakan JSONField jika formatnya lebih terstruktur
    poster = models.ImageField(upload_to='film/posters/', verbose_name="Poster Film")  # Path lebih deskriptif

    def __str__(self):
        return self.judul
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Film-Film"
        ordering = ['-tahun_rilis']

class Komentar(models.Model):
    film = models.ForeignKey('Film', on_delete=models.CASCADE, related_name='komentar', verbose_name="Film")
    nama_pengunjung = models.CharField(max_length=50, verbose_name="Nama Pengunjung")
    isi_komentar = models.TextField(verbose_name="Isi Komentar")
    tanggal_komentar = models.DateTimeField(auto_now_add=True, verbose_name="Tanggal Komentar")

    def __str__(self):
        return f"Komentar oleh {self.nama_pengunjung} untuk {self.film}"

    class Meta:
        verbose_name = "Komentar"
        verbose_name_plural = "Komentar-Komenter"
        ordering = ['-tanggal_komentar']  # Komentar terbaru muncul pertama

