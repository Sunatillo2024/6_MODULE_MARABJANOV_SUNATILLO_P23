from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, ListView, DetailView

from apps.models import Product, Profile, Category


class SingUpView(LoginView):
    template_name = 'apps/auth/Sing_up.html'


class Product_listView(ListView):
    model = Product
    queryset = Category
    template_name = 'apps/product_fild/Product.html'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'apps/product_fild/profile.html'


class Product_ListView(ListView):
    model = Product
    template_name = 'apps/product_fild/product_update.html'


class Cast_LoginView(LoginView):
    template_name = 'apps/auth/Login.html'

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(email=request.POST['email'], username=request.POST['username'])
        if not user:
            return messages.error(request, 'User not found')
        else:
            user = user.first().save()
            return messages.success(request, 'Login successful')
