"""hrproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from hrapp.views import index,signup,login_user,logout_user,create_jobpost_view,display_jobpost,profile,sendmail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('signup/',signup,name='signup'),
    path('login/',login_user,name="login_user"),
    path('logout/',logout_user,name="logout_user"),
    path('jobapply/form/',create_jobpost_view,name="jobapply_form"),
    path('jobs/',display_jobpost,name="display_jobpost"),
    path('profile/',profile,name="profile"),
    path('sendmail/',sendmail,name="sendmail"),
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)