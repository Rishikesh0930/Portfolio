"""
URL configuration for MyPortfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home-page"),
    path('about/', about_page, name="about-page"),
    path('skills/', skills_page, name="skills-page"),
    path('project/', project_page, name="project-page"),
    path('contact/', contact_page, name="contact-page"),
    path('resume/', resume_page, name="resume-page"),
]
