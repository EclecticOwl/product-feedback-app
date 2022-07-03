from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from core import views

urlpatterns = [
    path('', views.api_root),

    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),

    path('feedback/', views.FeedbackList.as_view(), name='feedback_list'),
    path('feedback/<int:pk>/', views.FeedbackDetail.as_view(), name='feedback_detail'),
]



urlpatterns = format_suffix_patterns(urlpatterns)