from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length = 40)
    registered_date = models.DateTimeField("date registered")

    def __str__(self):
        return self.author_name


class Post(models.Model):
    post_header = models.CharField(max_length = 200)
    published_date = models.DateTimeField("date published")
    votes = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_header


