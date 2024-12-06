from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book
from books.forms import BookForm
from django.contrib.auth.decorators import login_required

def index(request):
    books = Book.objects.all()
    search = request.GET.get('search')
    if search:
        books = Book.objects.filter(name__icontains=search)
    context = {
        "books": books
    }
    return render(request, 'index.html', context)


def detail(request, pk):
    book = get_object_or_404(Book.objects.all(), id=pk)
    context = {
        'book': book
    }
    return render(request, 'detail.html', context)


@login_required(login_url='login')
def add(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form
    }
    return render(request, 'add_book.html', context)


@login_required(login_url='login')
def edit(request, pk):
    book = get_object_or_404(Book.objects.all(), id=pk)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(instance=book, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form
    }
    return render(request, 'edit.html', context)


@login_required(login_url='login')
def delete(request, pk):
    book = get_object_or_404(Book.objects.all(), id=pk)
    book.delete()
    return redirect('index')