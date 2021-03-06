"""time_consultants URL Configuration

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
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from constructor import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.EditorView.as_view(), name='editor'),
    path('model_fields/', csrf_exempt(views.ModelFieldsView.as_view()), name='model_fields'),
    path('all_model_fields/', csrf_exempt(views.AllModelFieldsView.as_view()), name='all_model_fields'),

    path('printing_method_model_fields/', csrf_exempt(views.PrintingMethodModelFieldsView.as_view()), name='printing_method_model_fields'),
    path('printing_method_all_model_fields/', csrf_exempt(views.AllPrintingMethodModelFieldsView.as_view()), name='printing_method_all_model_fields'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
