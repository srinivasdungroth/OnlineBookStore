from django.shortcuts import render
from django.http import HttpResponse
from vendor.models import books
# Create your views here.
def home(request):
    return render(request,'home.html')
def about_us(request):
    return render(request,'about_us.html')
def art_photography(request):
    return render(request,'art_&_photography.html')
def award_winning(request):
    return render(request,'award_winning.html')
def best_seller(request):
    return render(request,'best_seller.html')
def biographies_memories(request):
    return render(request,'Biographies_&_Memoirs.html')
def box_sets(request):
    return render(request,'box_sets.html')
def contact(request):
    return render(request,'contact.html')
def dictionaries_language(request):
    return render(request,'Dictionaries_&_Language.html')
def featured_authors(request):
    return render(request,'featured_authors.html')
def fiction_books(request):
    return render(request,'fiction_books.html')
def Fiction(request):
    return render(request,'Fiction.html')
def forgot_password(request):
    return render(request,'forgot_password.html')
def law(request):
    return render(request,'law.html')
def login(request):
    return render(request,'login.html')
def medicine(request):
    return render(request,'medicine.html')
def new_arrivals(request):
    return render(request,'new_arrivals.html')
def request_a_book(request):
    return render(request,'request_a_book.html')
def signup(request):
    return render(request,'signup.html')
def society(request):
    return render(request,'Society.html')
def todays_deals(request):
    return render(request,'todays_deals.html')

def art_photography(request):
    art_photography_books = books.objects.filter(CategoryName="art_&photography")
    return render(request, 'art_&_photography.html', {'art_photography_books': art_photography_books})

def biographies_memories(request):
    biographies_memories_books = books.objects.filter(CategoryName="biographies_&memoirs")
    return render(request, 'Biographies_&_Memoirs.html', {'biographies_memories_books': biographies_memories_books})

def dictionaries_language(request):
    dictionary_languages_books = books.objects.filter(CategoryName="dictionaries_&language")
    return render(request, 'Dictionaries_&_Language.html', {'dictionary_languages_books': dictionary_languages_books})

def fiction(request):
    fiction_books = books.objects.filter(CategoryName="fiction")
    return render(request, 'Fiction.html', {'fiction_books': fiction_books})

def society(request):
    society_books = books.objects.filter(CategoryName="society")
    return render(request, 'Society.html', {'society_books': society_books})

def law(request):
    law_books = books.objects.filter(CategoryName="law")
    return render(request, 'law.html', {'law_books': law_books})

def medicine(request):
    medicine_books = books.objects.filter(CategoryName="medicine")
    return render(request, 'medicine.html', {'medicine_books': medicine_books})

def new_arrivals(request):
    art_photography_books = books.objects.filter(CategoryName="art_&photography")
    return render(request, 'new_arrivals.html', {'art_photography_books': art_photography_books})

def box_sets(request):
    biographies_memories_books = books.objects.filter(CategoryName="biographies_&memoirs")
    return render(request, 'box_sets.html', {'biographies_memories_books': biographies_memories_books})

def best_seller(request):
    dictionary_languages_books = books.objects.filter(CategoryName="dictionaries_&language")
    return render(request, 'best_seller.html', {'dictionary_languages_books': dictionary_languages_books})

def fiction_books(request):
    fiction_books = books.objects.filter(CategoryName="fiction")
    return render(request, 'fiction_books.html', {'fiction_books': fiction_books})




def award_winning(request):
    society_books = books.objects.filter(CategoryName="society")
    return render(request, 'award_winning.html', {'society_books': society_books})


def todays_deals(request):
    law_books = books.objects.filter(CategoryName="law")
    return render(request, 'todays_deals.html', {'law_books': law_books})


