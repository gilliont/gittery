# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from . import forms

from rango.models import Category, Page


def home(request):
    return HttpResponse("Tango with django app.")

def index(request):
    template_name = 'rango/category_list.html'
    all_categories = Category.objects.all()
    context_dict = {
        'all_categories':all_categories,
        'num_categories':len(all_categories),
    }
    return render(request, template_name, context=context_dict)

def form_category_view(request):
    form = forms.FormCategory()
    form_page = forms.FormPage()
    template_name = 'rango/category_list.html'

    if request.method == 'POST':
        form = forms.FormCategory(request.POST)
        form_page = forms.FormPage(request.POST)

        # if form_page.is_valid():
        #     data = form_page.cleaned_data
        #     print("cleaned page form: ", form_page.cleaned_data)
        #     p, created = Page.objects.get_or_create(
        #     category = data["category"],
        #     title = data["title"],
        #     url = data["url"],
        #     views = data["views"],
        #     )

        if form_page.is_valid():
            form_page.save(commit=True)
            return redirect('myforms')
        else:
            print("Form is not valid.")

        if form.is_valid():
            print("cleaned data: ", form.cleaned_data)
    return render(request, template_name, {'form':form,
                                           'form_page':form_page})


class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'

class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'

class CategoryDetailView(DetailView):
    model = Category
    fields = '__all__'

