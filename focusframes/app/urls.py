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
    path('view_pro/<pid>',views.view_product),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('view_cart',views.view_cart),
    path('bookings',views.bookings),
    path('pro_buy/<pid>',views.pro_buy),
    path('cart_pro_buy/<cid>',views.cart_pro_buy),
    path('qty_in/<cid>',views.qty_in),
    path('qty_dec/<cid>',views.qty_dec),
    # path('women_frames/', views.women_frames),
    # path('men_frames/', views.men_frames),
    # path('kids_frames/', views.kids_frames),


]