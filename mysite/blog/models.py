from django.db import models
import uuid
from django.contrib.auth.models import User


class Post(models.Model):
    (DRAFT, PUBLISH) = (0, 1)
    STATUS = [(DRAFT, "Draft"), (PUBLISH, "Publish")]
    book = models.CharField(
        max_length=200, unique=True, verbose_name="book", default="New Book"
    )
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        verbose_name="author",
        unique=False,
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=1000, verbose_name="content")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0, verbose_name="status")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.book

    def clean(self):
        self.slug = str(uuid.uuid4())
