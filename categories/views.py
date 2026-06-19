from django.shortcuts import render,redirect
from .models import Category
from .forms import CategoryForm


def category_list(request):

    categories = Category.objects.all()

    return render(
        request,
        'categories/category_list.html',
        {
            'categories':categories
        }
    )


def add_category(request):

    if request.method=="POST":

        form = CategoryForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect('category_list')

    else:

        form = CategoryForm()

    return render(
        request,
        'categories/add_category.html',
        {
            'form':form
        }
    )

