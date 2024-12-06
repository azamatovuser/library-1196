from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='book_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    file = models.FileField(upload_to='book_pdfs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name