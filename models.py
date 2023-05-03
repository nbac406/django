from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.

class Category(models.Model) : 
    name = models.CharField(max_length = 100, help_text = '입력 필요')

    def __str__(self) : 
        return self.name


class Post(models.Model) : 
    title = models.CharField(max_length = 100)
    title_image = models.ImageField(blank = True)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add = True)
    updateDate = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(Category)

    def __str__(self) : 
        return self.title

    def get_absolute_url(self) : 
        return reverse('post', args = [str(self.id)])

    def is_content_more300(self) : 
        return len(self.content) > 300

    def get_content_under300(self) : 
        return self.content[:300]