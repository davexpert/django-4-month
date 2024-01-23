from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
'''
FVC (function-based view) - представления, основанные на функциях
CBV (class based view) - представления, основанные на классах
'''

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello, World~!")

def current_date_view(request):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Current date and time: {current_date}")

def goodby_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbuy user")

def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')

# def post_list_view(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#
#         return render(
#             request,
#             'post/list.html',
#             context={'posts': posts},
#         )
# def post_detail_view(request, post_id):
#     if request.method == 'GET':
#         post = Post.objects.get(id=post_id)
#
#         return render(
#             request,
#             'post/detail.html',
#             context={'post': post}
#         )

def product_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        return render(
            request,
            'product/index.html',
            context={'prducts': products},
        )
def product_view(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        return render(
            request,
            'product/products.html',
            context={'product': product}
        )