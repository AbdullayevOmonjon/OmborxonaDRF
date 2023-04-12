"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from asosiy_app.views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('mahsulotlar',MahsulotSetview),
router.register('kilentlar',ClintModelSetView),
router.register('oborxona',OmborModelSetView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('get_token/',TokenObtainPairView.as_view(),name='token_olish'),
    path('token_yangilash/',TokenRefreshView.as_view(),name='token_yangilash'),
    # path('klintlar/',ClintAPIView.as_view(),name='klintlar'),
    # path('klint/<int:pk>/',ClintAPIView.as_view(),name='kilent_u'),
    # path('mahsulotlar/',MahsulotSetview.as_view(),name='mahsulotlar'),
    # path('ombor/',OmborxonaAPIView.as_view(),name='ombor'),
    # path('omboru/<int:pk>/',OmborxonaAPIView.as_view(),name='omboru'),
    
]
