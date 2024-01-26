from django.contrib import admin

# Register your models here.
from post.models import Product, Review, Categorie

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Categorie)