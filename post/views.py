from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from post.models import Product, Review, Categorie
from post.forms import ProductCreateForm, ProductCreateForm2, ReviewCreateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello, World~!")

def main_page_view(request):
    if request.method == 'GET':
        return render (request, 'index.html')


def product_list_view(request):
    if request.method == 'GET':
        search = request.GET.get('search', '')
        sort = request.GET.get('sort', 'created_at')
        categories = request.GET.get('categorie', '')
        page = request.GET.get('page', 1)

        products = Product.objects.all()
        if request.user.is_authenticated:
            products.exclude(user=request.user)

        if search:
            products = products.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )
            #products = products.filter(title__icontains=search) | products.filter(content__icontains=search)
        if sort:
            products = products.order_by(sort)

        if categories:
            products = products.filter(categories__id=categories)

        limit = 3
        max_pages = products.__len__() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)

        start = (int(page) - 1) * limit
        end = start + limit
        products = products[start:end]


        categories = Categorie.objects.all()
        context = {'products': products, 'categories': categories, 'max_pages': range(1, max_pages + 1)}

        return render(
            request,
            'post/list.html',
            context=context
        )


def product_detail_view(request, product_id):
    if request.method == 'GET':
        form = ReviewCreateForm()
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return HttpResponse("Post not found")

        has_change_permission = product.user == request.user

        context = {'product': product, 'review_form': form, 'has_change_permission': has_change_permission}

        return render(
            request,
            'post/detail.html',
            context=context
        )


def categories_list_view(request):
    if request.method == 'GET':
        categories = Categorie.objects.all()

        return render(
            request,
            'categorie/list.html',
            {"categories": categories}
        )

@login_required
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

@login_required
def product_update_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse("Post not found")

    if product.user != request.user:
        return HttpResponse("Permission denied", status=403)

    if request.method == 'GET':
        form = ProductCreateForm2(instance=product)
        return render(
            request,
            'post/update.html',
            {'form': form}
        )
    elif request.method == 'POST':
        form = ProductCreateForm2(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product_id)
        return render(
            request,
            'post/update.html',
            {'form': form}
        )

@login_required
def review_create_view(request, product_id):
    if request.method == 'POST':
        form = ReviewCreateForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.product_id = product_id
            review.user = request.user
            review.save()

        return redirect('product_detail', product_id=product_id)
