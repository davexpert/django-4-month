
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from post.views import hello_view, main_page_view, \
    product_list_view, product_detail_view, categories_list_view, \
    product_create_view, review_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('hello/', hello_view),
    path('products/', product_list_view, name='products_list'),
    path('products/<int:product_id>/', product_detail_view, name='product_detail'),
    path('products/create/', product_create_view),
    path('products/<int:product_id>/review/', review_create_view, name='review_create'),

    path('categories/', categories_list_view),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
