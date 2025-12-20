from django.shortcuts import render

from products.models import Film

# Create your views here.
def index(request):
    films = Film.objects.all()
    return render(request, 'home/index.html', {'films': films})