"""ekonomi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [ # pylint: disable=C0103
    path('', views.ExpenseIndex.as_view(), name='root'),
    path('expense', views.ExpenseIndex.as_view(), name='expense-list'),
    path('expense/add', views.ExpenseCreate.as_view(), name='expense-create'),
    path('expense/<int:pk>/', views.ExpenseUpdate.as_view(), name='expense-update'),
    path('expense/<int:pk>/delete', views.ExpenseDelete.as_view(), name='expense-delete'),
    path('upload', views.UploadIndex.as_view(), name='upload-list'),
    path('upload/add', views.UploadCreate.as_view(), name='upload-create'),
    path('upload/<int:pk>/', views.UploadUpdate.as_view(), name='upload-update'),
    path('upload/<int:pk>/delete', views.UploadDelete.as_view(), name='upload-delete'),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
