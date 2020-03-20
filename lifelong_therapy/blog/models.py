import datetime

from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Author(models.Model):
    author_name = models.CharField(max_length = 40)
    registered_date = models.DateTimeField("date registered")

    def __str__(self):
        return self.author_name

    def was_registered_recently(self):
        return self.registered_date >= timezone.now() - datetime.timedelta(days = 5)
    

class Post(models.Model):
    post_header = models.CharField(max_length = 200)
    post_image = models.ImageField(blank=True)
    post_content = RichTextField(blank=True)
    published_date = models.DateTimeField("date published")
    votes = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_header

    def was_published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days = 1)

class Subscriber(models.Model):
    # Newsletter records go to here. Be sneaky enough to save contact people to newsletter signup
    subscriber_name = models.CharField(max_length = 40)
    subscriber_email = models.EmailField(max_length = 32)
    subcriber_phone = models.CharField(max_length = 10, blank = True)

    def __str__(self):
        return self.subscriber_name


