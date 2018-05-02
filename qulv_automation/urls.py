"""qulv_automation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from app_api_test.pro_sys.pro_case import pro_case_views
from web_site.home.index import index, home, login, logout
from web_site.sys_menu.user_account_views import user_account_page, user_from, user_add, user_delete, user_list

urlpatterns = [

    # -------------------------      Qulv 自动化测试      ---------------------------- #

    # --------------- Django ------------- #
    url(r'^admin/', admin.site.urls),
    # --------------- Main --------------- #
    url(r'^$', login),
    url(r'^index/$', index),
    url(r'^home/$', home),
    url(r'^logout/$', logout),
    # -------------- System -------------- #
    url(r'^sys_user/$', user_account_page),
    url(r'^user_list/$', user_list),
    url(r'^user_from/$', user_from),
    url(r'^user_from/add/', user_add),
    url(r'^user_from/delete/', user_delete),


    # --------------API Test-------------------#
    url(r'^app_api_test/',include('app_api_test.urls')),

]
