from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.admindash, name = 'admindash'),
    path('projects/', views.projects, name='projects'),
    # path('add_item/', views.add_item, name='add_item'),
    # path('front_carousel/', views.carousel, name='carousel'),
    # path('add_carousel/<pk>', views.add_carousel, name = 'add_carousel'),
    # path('lower_banner/', views.lower_banner_view, name='lower_banner'),
    # path('add_banner/<pk>', views.add_banner, name = 'add_banner'),
    # path('orders/', views.orders, name='orders'),
    # path('order-item/<pk>', views.order_item, name='order_item'),
    # path('coupon/', views.coupon, name='coupon'),
    # path('add-coupon/', views.add_coupon, name='add_coupon'),
    # path('delete-coupon/<int:pk>', views.delete_coupon, name = 'delete_coupon'),
    # path('edit_item/<pk>', views.edit_item, name = 'item_edit'),
    # path('delete/<int:pk>', views.delete_item, name = 'item_delete'),
]