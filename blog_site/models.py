from django.db import models
from django.contrib.auth.models import AbstractUser

import datetime
import os

from django.utils.timezone import now,localtime
from django.utils.timesince import timesince

def getFileName(request, filename):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_filename = '%s%s' %(now_time,filename)
    return os.path.join('uploads', new_filename)

class CustomUser(AbstractUser):
    contact = models.CharField(max_length=10, null=False, blank=False)
    profile_pic = models.ImageField(upload_to=getFileName, null=True, blank=True)
    is_blocked = models.BooleanField(default='False', null=False, blank=False)

class Blog(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogs')
    blog_img = models.ImageField(upload_to=getFileName, null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified']

    @property
    def created_at_local(self):
        # print(self.created_at)
        # print(localtime(self.created_at).strftime('%Y-%m-%d %H::%M::%S'))
        return localtime(self.created_at)

    @property
    def time_since_created(self):
        return f"Last modified {timesince(self.last_modified, now())} ago"
    
class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
    
    class Meta:
        ordering = ['created_at']