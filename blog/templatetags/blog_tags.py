from django import template
from ..models import Post, Category, Tag
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_reading_posts(num=5):
	return Post.objects.all().order_by('-read_amount')[:num]

@register.simple_tag
def archives():
	return Post.objects.datetimes('create_time', 'month', order='DESC')

@register.filter
def get_archives_num(date):
	return Post.objects.filter(create_time__year=date.year, create_time__month=date.month).count()	

@register.simple_tag
def get_categories():
	# 别忘了在顶部引入 Category 类
	#return Category.objects.all()
	return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag	
def get_tag():
	return Tag.objects.annotate(num_posts=Count('post'))