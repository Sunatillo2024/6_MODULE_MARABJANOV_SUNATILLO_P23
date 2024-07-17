from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from apps.views import SingUpView, Product_listView, ProfileDetailView, Product_ListView

urlpatterns = [
    path('Sig_up', SingUpView.as_view(), name='sid_up'),
    path('',Product_listView.as_view(), name='product_list'),
    path('profile',ProfileDetailView.as_view(), name='profile'),
    path('login',LoginView.as_view(), name='login'),
    path('logout',LogoutView.as_view(), name='logout'),
    path('porduct_up',Product_ListView.as_view(), name='product_up'),
]
