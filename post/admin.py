from django.contrib import admin

# Register your models here.
from post.models import Product, Review, Categorie

# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "title", "price", "created_at", "updated_at"]
    list_display_links = ["id", "title"]
    search_fields = ["title", "content"]
    list_filter = ["created_at", "updated_at"]
    list_editable = ["price"]
    fields = ["id", "user", "title", "content", "photo", "categories", "price", "created_at", "updated_at"]
    readonly_fields = ["id", "created_at", "updated_at"]



admin.site.register(Review)
admin.site.register(Categorie)