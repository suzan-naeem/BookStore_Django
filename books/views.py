from django.shortcuts import render ,redirect
# from django.http import HttpResponse
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

@login_required(login_url="/login")
@permission_required(["books.view_book"], raise_exception=True)  #app.action_model , kda msh hi5ly users elly b creat hom yshofo saf7t index b3d ma 3mlo login ela lw adito prmession mn admin panel
def index(request):
    # return HttpResponse("heloooooo")
    # return render (request, "books/index.html")
    books = Book.objects.all()
    # books = Book.objects.filter(category__in=["IT","DevOps"])  #filter btrg3 array f lazm ast5dm for each
    # books = Book.objects.filter(category__name__in=["IT","DevOps"])
    # books = Book.objects.filter(category__name__exact="IT")
    
    return render(request,"books/index.html",{
        "books": books
    })

def create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request,"books/create.html",{
            "form": form
        })


def edit(request, id):
    book = Book.objects.get(pk=id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request,"books/edit.html",{
            "form": form,
            "book": book
        })


def delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect("index")
