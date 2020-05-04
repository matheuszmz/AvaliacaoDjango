from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import products_list, products_new, products_update, products_delete

urlpatterns = [
    path('', products_list, name='products_list'),
    path('new', products_new, name='products_new'),
    path('update/<int:id>', products_update, name='products_update'),
    path('delete/<int:id>', products_delete, name='products_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
