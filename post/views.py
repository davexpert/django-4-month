from django.shortcuts import render
from django.http import HttpResponse
from post.models import Product, Review, Categorie
# Create your views here.
def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello, World~!")

def main_page_view(request):
    if request.method == 'GET':
        return render (request, 'index.html')


def product_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        return render(request,
                      'post/list.html',
                      context={'products': products}
                      )
def product_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return HttpResponse("Post not found")



        return render(
            request,
            'post/detail.html',
            context={'product': product}
        )

def categories_list_view(request):
    if request.method == 'GET':
        categories = Categorie.objects.all()

        return render(
            request,
            'categorie/list.html',
            {"categories": categories}
        )