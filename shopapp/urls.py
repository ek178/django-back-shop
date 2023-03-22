from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenRefreshView,)

urlpatterns = [

    path('', views.index),

    path('registertest/',views.ProfileViewSet.as_view({'post': 'create'})),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('profiles/',views.ProfileView.as_view(), name='profile-oo'),
    path('profiles/<int:pk>/', views.ProfileView.as_view(), name='profile-detail'),

    path('profiles2/',views.ProfileView2.as_view(), name='profile-2'),
    path('profiles2/<int:pk>/', views.ProfileView2.as_view(), name='profile-detail2'),

    path('departments/',views.CategoryView.as_view(), name='deparments'),
    path('departments/<int:pk>/', views.CategoryView.as_view(), name='departments2'),

    path('products/',views.ProductView.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductView.as_view(), name='products2'),

    path('order/',views.OrderView.as_view(), name='order'),
    path('order/<int:pk>/', views.OrderView.as_view(), name='order2'),

    path('orderover/',views.OrderSerView.as_view(), name='orderover'),
    path('orderover/<int:pk>/', views.OrderSerView.as_view(), name='orderover2'),

    path('delivery/',views.DeliveryView.as_view(), name='delivery'),
    path('delivery/<int:pk>/', views.DeliveryView.as_view(), name='delivery2'),

    path('review/',views.ReviewView.as_view(), name='review'),
    path('review/<int:pk>/', views.ReviewView.as_view(), name='review2'),

    ]