from django.db import models
#
# Create your models here.

# class Post(models.Model):
#     photo = models.ImageField(upload_to="post_photos/%Y/%m/%d", null=True)
#     title = models.CharField(max_length=100)
#     content = models.TextField(null=True, blank=True)
#     rate = models.FloatField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f'{self.id} - {self.title}'

class Product(models.Model):
    photo = models.ImageField(upload_to="post_photos/%Y/%m/%d", null=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.name} - {self.price}'

