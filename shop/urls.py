from django.urls import path, include
from . import views

urlpatterns = [

    path('cart/add/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('search/', views.search, name='search'),
    path('personal-page/', views.personal_page, name='personal_page'),
    path('', views.index, name='main'),
    path('de-scripts/', views.de_scripts, name='bases_des'),
    path('cakes/', views.cake, name='cakes'),
    path('cupcake/', views.cupcake, name='cupcakes'),
]