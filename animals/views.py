from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Animal

# Create your views here.
def homepage(request):
    animals = Animal.objects.all().order_by('-create_date')
    return render(request,'animals/home.html', {'animals':animals})

class BakraListView(ListView):
    model = Animal
    template_name = 'animals/animal_list.html'
    queryset = Animal.objects.filter(category='b')
    context_object_name = 'animals'

class BakraDetailView(DetailView):
    model = Animal
    template_name = 'animals/animal_detail.html'
    context_object_name = 'animal'

class VehraListView(ListView):
    model = Animal
    template_name = 'animals/animal_list.html'
    queryset = Animal.objects.filter(category='v')
    context_object_name = 'animals'

class VehraDetailView(DetailView):
    model = Animal
    template_name = 'animals/animal_detail.html'
    context_object_name = 'animal'

class SheepListView(ListView):
    model = Animal
    template_name = 'animals/animal_list.html'
    queryset = Animal.objects.filter(category='d')
    context_object_name = 'animals'

class SheepDetailView(DetailView):
    model = Animal
    template_name = 'animals/animal_detail.html'
    context_object_name = 'animal'

class CamelListView(ListView):
    model = Animal
    template_name = 'animals/animal_list.html'
    queryset = Animal.objects.filter(category='c')
    context_object_name = 'animals'

class CamelDetailView(DetailView):
    model = Animal
    template_name = 'animals/animal_detail.html'
    context_object_name = 'animal'