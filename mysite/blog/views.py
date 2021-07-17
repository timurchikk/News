from django.shortcuts import render
from .models import *


def main(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news' : news,
        'titlle' : 'Список новостей',
        'categories' : categories,
    }

    return render(request, template_name='blog/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news' : news,
        'categories' : categories,
        'category' : category,
    }

    return render(request, template_name='blog/category.html', context=context)
