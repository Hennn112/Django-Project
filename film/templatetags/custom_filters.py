# di dalam templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def truncate_words(value, word_count):
    """Memotong string hingga n kata"""
    words = value.split()  # Pisahkan berdasarkan spasi
    return ' '.join(words[:word_count])  # Ambil kata hingga yang ke-20

@register.filter(name='next_word')
def next_word(value, next_word_count):
    """
    Filter untuk menampilkan sinopsis setelah potongan pertama.
    Menggunakan truncate_words untuk memotong kata dan menampilkan sisanya.
    """
    # Potong sinopsis setelah 16 kata pertama
    words = value.split()
    if len(words) > next_word_count:
        return ' '.join(words[next_word_count:])  # Mengembalikan sisa sinopsis setelah kata ke-16
    return value  # Jika tidak lebih dari 16 kata, kembalikan sinopsis utuh