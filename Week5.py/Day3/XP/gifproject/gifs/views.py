from django.shortcuts import render
from .forms import CategoryForm,GifForm
from .models import Category,Gif
from django.http import HttpResponse
from datetime import datetime


# This page output all gifs from my database
def homepage(request):
    all_gifs = Gif.objects.all()
    context = {'all_gifs': all_gifs}
    return render(request, 'homepage.html', context)


def add_gif_view(request):

    gif_form = GifForm()

    # GET mode - getting content out

    if request.method == 'POST':
        print("POST data: ", request.POST)
        print('POSTING DATA')
        gif_filled_form = GifForm(request.POST)  # put the data from the request into the ModelForm

        if gif_filled_form.is_valid():  # check if all fields contain the correct data
            gif_filled_form.save()  # save data into database
            return HttpResponse("SUCCESSFULLY SAVED")

    if request.method == 'GET':
        gif_form = GifForm()
        print("GET data: ", request.GET)  # data associated with the GET method
        print("GETTING DATA OUT")
        context = {'form': gif_form}

    return render(request, 'add_gif.html', context)

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            newcategory = Category(name = data['name'])
            newcategory.save()
            message = 'New category added'
        else:
            form = CategoryForm()
            message ='Error'
    else:
        form = CategoryForm()
        message = ''
    context = {'form':form,
               'message':message,
               }
    return render(request,'addcategory.html',context)

def gif_view(request, id):
    all_gifs = Gif.objects.all()
    context = {
        'all_gifs': all_gifs,
        'id':id
    }

    return render(request,'gifview.html',context)

def categories(request):
    allcategory = Category.objects.all()
    context = {
        'all_categories': allcategory,
    }

    return render(request, 'categories.html',context)

def category_view(request, cat_id):
    category = Category.objects.get(id = cat_id)
    all_gifs = Gif.objects.all()
    list_gifs = []
    for gif in category.gifs.all():
        list_gifs.append(gif)
    context = {
        'gifs_list': list_gifs,
        'all_gifs': all_gifs,
        'category': category.gifs.all(),
        'cat_id': cat_id,
    }
    return render(request, 'categoryview.html', context)


