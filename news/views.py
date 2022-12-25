from django.shortcuts import render
from .models import New

# Create your views here.

def news(request):
    news=New.objects.all().order_by('-date')
    context = {"news":news}
    return render(request, 'news/news.html', context)

