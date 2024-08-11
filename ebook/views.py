from django.shortcuts import render, redirect
from .models import Ebook
from django.http import Http404
from django.contrib import messages

from .forms import EbookForm


def index_view(request):
    ebooks = Ebook.objects.all()
    context = {
        'ebooks' : ebooks
    }

    return render(request, 'ebook/index.html', context)

def detail_view(request, ebook_id):
    try:
        ebook = Ebook.objects.get(pk=ebook_id)
        context = {
            'ebook' : ebook
        }

    except Ebook.DoesNotExist:
        raise Http404("Book Not Found")
    
    return render(request, 'ebook/detail.html', context)

def create_view(request):
    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES or None)

        if form.is_valid():
            new_ebook = EbookForm(request.POST)

            new_ebook.save()

            messages.success(request, 'Succes to add new book')

            return redirect ('ebook:index')
        
    else:
        form = EbookForm()

    return render(request, 'ebook/form.html', {'form' : form})


def update_view(request, ebook_id):
    try:
        ebook = Ebook.objects.get(pk=ebook_id)
    except Ebook.DoesNotExist:
        raise Http404("Can not found ebook")
    
    if request.method == 'POST':
        form = EbookForm(request.POST or None, request.FILES or None,instance=ebook)
        if form.is_valid():
            form.save()
            messages.success(request, 'E-Book updated')
            return redirect('ebook:index')
        
    else:
        form = EbookForm(instance=ebook)

    return render(request, 'ebook/form.html', {'form': form})


def delete_view(request, ebook_id):
    try:
        ebook = Ebook.objects.get(pk=ebook_id)
        ebook.delete()
        messages.success(request, 'Ebook Deleted')
        return redirect('ebook:index')
    
    except Ebook.DoesNotExist:
        raise Http404("Can not find the book")