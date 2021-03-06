"""BACS383 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from .views import home, calculatorOneView, calculatorTwoView, calculatorThreeView

urlpatterns = [
    path('', home, name="home"),
    path('calculator/1/', calculatorOneView, name="calc1"),
    path('calculator/2/', calculatorTwoView, name="calc2"),
    # path('calculator/3/', calculatorThreeView),
]
