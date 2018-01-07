from markdown import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger

# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    after_range_num = 3        # 当前页前显示3页
    before_range_num = 3       # 当前页后显示3页
    num_of_displaypages = 11   # 显示页数
    first = False              # 显示左边省略号
    last = False               # 显示右边省略号

    try:
        page = int(request.GET.get("page", 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(post_list, 10)
    count = paginator.count
    try:
        post_list = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        post_list = paginator.page(paginator.num_pages)
    # 总页数小于等于显示页数时，则将总页数全部显示
    if paginator.num_pages <= num_of_displaypages:
        page_range = range(1, paginator.num_pages + 1)
    # 第一种情况
    elif post_list.number <= num_of_displaypages - after_range_num - 2:
        last = True
        page_range = range(1, post_list.number + after_range_num + 1)
    # 第二种情况
    elif num_of_displaypages - after_range_num - 2 < post_list.number < paginator.num_pages - after_range_num - 2:
        first = True
        last = True
        page_range = range(post_list.number - before_range_num, post_list.number + after_range_num + 1)
    # 第三种情况
    else:
        first = True
        page_range = range(post_list.number - before_range_num, paginator.num_pages + 1)
        #page_range = range(1,10)
    context = {'post_list': post_list,
               'page_range': page_range,
               'count': count,
               'first': first,
               'last': last
               }

    #return HttpResponse(u"欢迎光临 我的博客!")
    return render(request, 'index.html', context=context)
	
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