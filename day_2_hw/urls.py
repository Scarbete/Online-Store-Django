from django.contrib import admin
from django.urls import path
from products.views import main_page_view, products_page_view, product_detail_view, create_product_view
from day_2_hw import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main_page_view),
    path('products/', products_page_view),
    path('admin/', admin.site.urls),
    path('products/<int:id>', product_detail_view),
    path('products/create', create_product_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)