from django.contrib import admin
from django.urls import path
from products.views import MainPageCBV, ProductsCBV, ProductDetailCBV, CreateProductCBV
from users.views import RegisterCBV, LoginCBV, LogoutCBV
from day_2_hw import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainPageCBV.as_view()),
    path('admin/', admin.site.urls),

    # Products
    path('products/', ProductsCBV.as_view()),
    path('products/<int:id>/', ProductDetailCBV.as_view()),
    path('products/create/', CreateProductCBV.as_view()),

    # Auth
    path('users/register/', RegisterCBV.as_view()),
    path('users/login/', LoginCBV.as_view()),
    path('users/logout/', LogoutCBV.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)