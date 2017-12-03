from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.		
class Category(models.Model):
	name = models.CharField('分类', max_length=100)
	
	class Meta:
		verbose_name = '分类'
		verbose_name_plural = '分类'
	
	def __str__(self):
		return self.name
		
class Tag(models.Model):
	name = models.CharField('标签', max_length=100)
	
	class Meta:
		verbose_name = '标签'
		verbose_name_plural = '标签'
	
	def __str__(self):
		return self.name

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户名')
	title = models.CharField('标题', max_length=100)
	body = models.TextField('内容')
	create_time = models.DateTimeField('发布日期', default=timezone.now)
	update_time = models.DateTimeField('最后修改日期', auto_now=True)
	read_amount = models.IntegerField('浏览', default=0)
	category = models.ForeignKey(Category, blank=True, verbose_name='分类')
	tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
	
	class Meta:
		ordering = ('-create_time',)
		#search_fields=['title', 'body']
		verbose_name = '博客'
		verbose_name_plural = '博客'
	
	def __str__(self):
		return self.title