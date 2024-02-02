from django.shortcuts import render, redirect
from django.http import HttpResponse
from post.models import Product, Review, Categorie
from post.forms import ProductCreateForm, ProductCreateForm2, ReviewCreateForm
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
        form = ReviewCreateForm()
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return HttpResponse("Post not found")

        return render(
            request,
            'post/detail.html',
            context={'product': product, 'review_form': form}
        )

def categories_list_view(request):
    if request.method == 'GET':
        categories = Categorie.objects.all()

        return render(
            request,
            'categorie/list.html',
            {"categories": categories}
        )

def product_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm2()
        }

        return render(
            request,
            'post/create.html',
            context=context
        )

    elif request.method == 'POST':
        form = ProductCreateForm2(request.POST, request.FILES)

        if form.is_valid():
            # Product.objects.create(**form.cleaned_data)
            form.save()
            return redirect('products_list')

        context = {
            'form': form
        }

        return render(
            request,
            'post/create.html',
            context=context
        )

def review_create_view(request, product_id):
    if request.method == 'POST':
        form = ReviewCreateForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.product_id = product_id
            review.save()

        return redirect('product_detail', product_id=product_id)
