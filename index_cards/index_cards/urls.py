"""index_cards URL Configuration

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
from api import views as api_views

from django.contrib import admin
from django.urls import path, re_path

from gui import views as gui_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/topics/', api_views.topic_list),
    path('api/topic/<int:pk>', api_views.topic_detail),
    path('api/cards/', api_views.card_list),
    path('api/cards/<int:topic>', api_views.card_list_topic),
    path('api/card/<int:pk>', api_views.card_detail),
    path('api/practisesessions/', api_views.practise_session_list_all),
    path('api/practisesessions/<int:topic>', api_views.practise_session_list_topic),
    path('api/practisesession/<int:pk>', api_views.practise_session_detail),
    path('api/sessioncards/<int:practise_session>', api_views.session_card_list),
    path('api/sessioncard/<int:pk>', api_views.session_card_detail),
    re_path(r'^.*', gui_views.index),
]
