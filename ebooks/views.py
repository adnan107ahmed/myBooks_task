from django.shortcuts import render,get_object_or_404, redirect
from .models import  myBooks

def home(request):
    books=myBooks.objects.all()
    context={'books':books}
    return render (request, 'index.html', context)

def delete_book(request, book_id):
    book = get_object_or_404(myBooks, id=book_id)  
    book.delete()
    return redirect('home')

def create_or_update_book(request, book_id=None):
    if book_id:  
        book = get_object_or_404(myBooks, id=book_id)
    else:  
        book = None

    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        price = request.POST.get('price')
        stock = request.POST.get('stock')

        if book:  
            book.title = title
            book.author = author
            book.genre = genre
            book.price = price
            book.stock = stock
            book.save()
        else:  
            myBooks.objects.create(
                title=title,
                author=author,
                genre=genre,
                price=price,
                stock=stock
            )
        return redirect('home')
    return render(request, 'form.html', {'book': book})
