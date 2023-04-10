"""student URL Configuration

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
from django.contrib import admin
from django.urls import path
from attendance import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', views.signupPage, name="signup"),
    path('login', views.loginPage, name="login"),
    path('', views.homePage, name="home"),
    path('student', views.studentpage, name="student"),
    path('record', views.displayPage, name="record"),
    path('attendance', views.attendancePage, name="attendance"),
    path('attendancerecord', views.attendanceRecordPage, name="attendancerecord"),
    path('download', views.downloadData, name="download"),
    path('edit/<int:Id>', views.editpage, name="edit"),
    path('edit/editrecord/<int:id>', views.editrecord, name='editrecord'),
    


    

]
