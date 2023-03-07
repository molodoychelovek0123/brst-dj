from django.conf import settings
from django.urls import path, include
from . import views 
app_name = 'shop'
urlpatterns = [
 path('collections/<int:id_coll>/type/<int:id_type>/products/<int:id_prod>/', views.product_detail),
 path('collections/<int:id_coll>/type/<int:id_type>/', views.product_detail),
 path('collections/<int:id_coll>/', views.collection_detail),
 path('collections/', views.collections),
 path('accounts/', include('allauth.urls')),
 path('about/', views.about),
 path('lookbooks/', views.lookbooks),
 path('', views.home),
]
