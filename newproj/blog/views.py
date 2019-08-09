from django.shortcuts import render
from datetime import datetime


posts = [
	{
		'author': 'Steve Wolfe',
		'title': 'Blog post 1',
		'content': 'Check out the Post Content',
		'date_posted': datetime.now()
	},
	{
		'author': 'Steve Wolfe',
		'title': 'Blog poast 2',
		'content': 'More Post Content',
		'date_posted': datetime.now()
	}
]


def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About the Project'})