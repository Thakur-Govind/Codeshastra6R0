from django.shortcuts import render,get_object_or_404
from .models import ngo
# Create your views here.
def home(request):
    ngos = ngo.objects
    return render(request, 'ngo/home.html', {'ngos':ngos})
def ngo_det(request,ng_id):
    ngo1 = get_object_or_404(ngo, pk = ng_id)
    return render(request,'ngo/ngdet.html', {'ngo':ngo1})
def donate(request, ng_id):
    ngo1 = get_object_or_404(ngo, pk = ng_id)
    
