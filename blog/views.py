from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Deal
# Create your views here.


def home(request):
    return render(request,'blog/home.html')


def rules(request):
    return render(request,'blog/rules.html')


def admn(request):
    return render(request,'blog/admins.html')



class DealListView(ListView):
    model=Deal
    ordering=['-publish']

    context_object_name='Deal'



class DealDetailView(DetailView):
    model=Deal
