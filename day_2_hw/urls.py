from django.contrib import admin
from django.urls import path
from products.views import main_page_view, products_page_view, product_detail_view, create_product_view
from users.views import register_view, login_view, logout_view
from day_2_hw import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main_page_view),
    path('admin/', admin.site.urls),

    # Products
    path('products/', products_page_view),
    path('products/<int:id>/', product_detail_view),
    path('products/create/', create_product_view),

    # Auth
    path('users/register/', register_view),
    path('users/login/', login_view),
    path('users/logout/', logout_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)