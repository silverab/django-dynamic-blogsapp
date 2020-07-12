from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
	posts = Post.objects.all()
	context = {'posts': posts}
	return render(request, 'post/home.html', context)
