from django.shortcuts import render, get_object_or_404
from .forms import DonerForm
from .models import Doner, Resource
from django.shortcuts import redirect
from django.utils import timezone

def blood_main(request):
    return render(request, 'blood/main.html', {})

def doner_list(request):
    doners = Doner.objects.order_by('name')
    return render(request, 'blood/doner_list.html', {'doners':doners})

def doner_detail(request, pk):
    doner = get_object_or_404(Doner, pk=pk)
    return render(request, 'blood/doner_detail.html', {'doner': doner})

def doner_new(request):
     if request.method == "POST":
         form = DonerForm(request.POST)
         if form.is_valid():
             doner = form.save(commit=False)
             doner.donating_date = timezone.now()
             doner.save()
             return redirect('doner_detail', pk=doner.pk)
     else:
         form = DonerForm()
     return render(request, 'blood/doner_edit.html', {'form': form})

def doner_edit(request, pk):
     doner = get_object_or_404(Doner, pk=pk)
     if request.method == "POST":
         form = DonerForm(request.POST, instance=doner)
         if form.is_valid():
             doner = form.save(commit=False)
             doner.donating_date = timezone.now()
             doner.save()
             return redirect('doner_detail', pk=doner.pk)
     else:
         form = DonerForm(instance=doner)
     return render(request, 'blood/doner_edit.html', {'form': form})

def resource_list(request):
    resources = Resource.objects.order_by('description')
    return render(request, 'blood/resource_list.html', {'resources':resources})

def resource_detail(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    return render(request, 'blood/resource_detail.html', {'resource': resource})