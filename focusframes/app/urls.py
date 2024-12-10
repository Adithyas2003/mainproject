from django.urls import path
from .import views

urlpatterns = [
    path('',views.e_shop_login),
    path('shop_home',views.shop_home),
    path('logout',views.e_shop_logout),
    path('add_product',views.add_product),


#######################user##################
    path('register/',views.Register),
    path('user_home',views.user_home),
    path('women_frames',views.women_frames),
    path('about',views.about),
]