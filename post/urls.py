from django.urls import path
from post.views import hello_view, main_page_view, \
    product_list_view, product_detail_view, categories_list_view, \
    product_create_view, review_create_view, product_update_view


urlpatterns = [
    path('', main_page_view),
    path('hello/', hello_view),
    path('products/', product_list_view, name='products_list'),
    path('products/<int:product_id>/', product_detail_view, name='product_detail'),
    path('products/<int:product_id>/update/', product_update_view, name='product_update'),
    path('products/create/', product_create_view),
    path('products/<int:product_id>/review/', review_create_view, name='review_create'),

    path('categories/', categories_list_view),
]