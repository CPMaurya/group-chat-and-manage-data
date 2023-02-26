"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views

from oauth.views import CustomOAuthTokenView

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('chat.urls')),

    path('login/', CustomOAuthTokenView.as_view(), name='oauth-token-view'),

    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'},
         name='logout')

]

# lx7x7U477hyfG8P5aTw0qdpA999xaXDYl1eOXes4 --- client id
# 9Y8hVgl7hJU1V2Sv6DgyT4qLoIWXEBCOkQ4wHeniPpBLrCNcoyojGYuvezqAT5aXNRZ5MFvAk1Drwi66EF0ldLJqfQvlZTFFi6WeETj7nNeMbiZ8WdDztxW0Q5KWDH3o -- client secret