from django.shortcuts import render
#from .models import *
from .forms import comments_section

def HomeView(request):
    form = comments_section(request.POST or None)
    if form.is_valid():
        form.save()
        form = comments_section()
    context = {'form':form}
    return render(request, 'home.html', context)