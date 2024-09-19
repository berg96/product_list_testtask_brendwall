from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductCreateView.as_view(), name='create'),
    path('list/', views.ProductListView.as_view(), name='list'),
]
