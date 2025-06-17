"""
URL configuration for WiseMath project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('math/', views.math),
    path('', views.math),
    # path('math/<int:type>/', views.math_type),
    # path('math/<int:a>/<str:op>/<int:b>', views.math_calc),
    # re_path(r'^math/(?P<a>\d+)(?P<op>[^0-9]+)(?P<b>\d+)$', views.math_calc),
    # path('test_request/', views.test_request),
    # path('test_post/', views.test_post),
    path('test_html/', views.test_html),
    path('test_html2/', views.test_html2),
]
