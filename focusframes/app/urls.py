from django.urls import path
from .import views

urlpatterns = [
    path('',views.e_shop_login),
    path('shop_home',views.shop_home),
    path('logout',views.e_shop_logout),
    path('add_product/',views.add_product),
    path('edit_product/<pid>',views.edit_product),
    path('delete_product/<pid>',views.delete_product),
    # path('category/<int:category_id>/', views.category_view),
    path('add_cate',views.add_category),
 
    # Other URLs...





#######################user##################
    path('register/',views.Register),
    path('user_home',views.user_home),
    path('about/',views.about),
    path('contact/',views.contact),
    # path('women_frames/', views.women_frames),
    # path('men_frames/', views.men_frames),
    # path('kids_frames/', views.kids_frames),


]