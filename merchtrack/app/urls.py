from django.conf import settings
from django.views.static import serve
from django.urls import path,re_path, include
from . import views
from .view import product, order

urlpatterns = [
    path("", views.home, name='home'),
    path("trackOrder", views.trackOrder, name='trackOrder'),
    path("aboutUs", views.aboutUs, name='aboutUs'),
    path("contactUs", views.contactUs, name='contactUs'),
    path("order-entry", views.orderEntry, name='order-entry'),
    path('adminTracker', views.adminTracker, name='adminTracker'),
    path('student-info', views.studentInfo, name='student-info'),
    path('registration', views.register, name='registration'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('messages', views.messages, name='messages'),
    path('success', views.success, name='success'),

    path('create-product', product.create_product, name='create_product'),
    path('products', product.product_list, name='product_list'),
    path('edit-product/<int:product_id>/', product.edit_product, name='edit_product'),
    path('delete-product/<int:product_id>/', product.delete_product, name='delete_product'),

    path('create_order/', order.create_order, name='create_order'),
    path('api/customer_info/', views.customer_info, name='customer_info'),

    path('order_list', order.order_list, name='order_list'),
    path('order_detail/<int:order_id>/', order.order_detail, name='order_detail'),
    path('edit_order/<int:order_id>/', order.edit_order, name='edit_order'),
    path('delete_order/<int:order_id>/', order.delete_order, name='delete_order'),
    path('sales_report', order.sales_report, name='sales_report'),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^.*$', views.not_found, name='404'),
]