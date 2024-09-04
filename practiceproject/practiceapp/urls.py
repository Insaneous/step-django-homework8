from django.urls import path
from practiceapp import views


urlpatterns = [
    path('', views.view, name='index'),
    path("add", views.add_store, name="add"),
    path("add_cat", views.add_cat, name="add_cat"),
    path('add_prod', views.add_prod, name="add_prod"),
    path('edit_prod', views.edit_prod, name="edit_prod"),
    path('del_prod', views.del_prod, name="del_prod"),
    path("store/<slug:store_slug>", views.store_info, name="store_info"),
    path('products/<slug:cat_slug>/<slug:store_slug>', views.products, name='store_products')
]
