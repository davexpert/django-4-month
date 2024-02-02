from django.db import models

class Categorie(models.Model):

    title = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.id} - {self.title}'

class Product(models.Model):
    photo = models.ImageField(upload_to="post_photos/%Y/%m/%d", null=True,
                              verbose_name="Фото")
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(
        Categorie,
        related_name="products"
    )

    def __str__(self):
        return f'{self.id} - {self.title}'

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.text[:20]}'


