from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
	post_list = Post.objects.all().order_by('-create_time')
    #return HttpResponse(u"欢迎光临 我的博客!")
	return render(request, 'index.html', context={'post_list': post_list})
	
def post_detail(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	return render(request, 'detail.html', context={'post': post})