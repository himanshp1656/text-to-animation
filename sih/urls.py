"""sih URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from appss import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home,name='home'),
    path('', views.home,name='home'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.login_view,name='login'),
    path('teachersubmit/', views.teacher_submit,name='teacher'),
    path('search/', views.search,name='search'),
    path('chat_with_gpt/', views.chat_with_gpt, name='chat_with_gpt'),
    path('chat/', views.chat_view, name='chat'),
    path('roadmap/', views.roadmap, name='chat'),
    path('teacherprofile/<int:teacher_id>/', views.teacherprofie, name="riderorderdetails"),
    
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# teacher application , gpt wala , index, roadmap