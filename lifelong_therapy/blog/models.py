import datetime

from django.db import models
from django.utils import timezone

class Author(models.Model):
    author_name = models.CharField(max_length = 40)
    registered_date = models.DateTimeField("date registered")

    def __str__(self):
        return self.author_name

    def was_registered_recently(self):
        return self.registered_date >= timezone.now() - datetime.timedelta(days = 5)
    

class Post(models.Model):
    post_header = models.CharField(max_length = 200)
    published_date = models.DateTimeField("date published")
    votes = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # TODO tinymce integration
    # TODO amazon S3 integration

    def __str__(self):
        return self.post_header

    def was_published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days = 1)


