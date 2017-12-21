from markdown import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag

# Create your views here.
def index(request):
	post_list = Post.objects.all().order_by('-create_time')
    #return HttpResponse(u"欢迎光临 我的博客!")
	return render(request, 'index.html', context={'post_list': post_list})
	
def post_detail(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	post.yueduliang()
	# 记得在顶部引入 markdown 模块
	post.body = markdown(post.body, ['extra', 'codehilite'])
	return render(request, 'detail.html', context={'post': post})
	
def archives(request, year, month):
	post_list = Post.objects.filter(create_time__year=year,
									create_time__month=month).order_by('-create_time')
	return render(request, 'index.html', context={'post_list': post_list})
	
def category(request, category_id):
	# 记得在开始部分导入 Category 类
	cate = get_object_or_404(Category, id=category_id)
	post_list = Post.objects.filter(category=cate).order_by('-create_time')
	return render(request, 'index.html', context={'post_list': post_list})
	
def tag(request, tag_id):
	tag = get_object_or_404(Tag, id=tag_id)
	post_list = Post.objects.filter(tags=tag)
	return render(request, 'index.html', context={'post_list': post_list})
	
def get_rss(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	text = '<strong><h2>[%s] %s</h2></strong>' % (post.category, post.title)
	text += '%s' % markdown(post.body, ['extra', 'codehilite'])
	return HttpResponse(text) 