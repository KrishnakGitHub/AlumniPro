from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from college import views
from django.views.generic.base import RedirectView
urlpatterns = [ 
    path('home/', views.HomeView.as_view()),
    path('about/', views.AboutView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('notice/', views.NoticeListView.as_view()),
    path('profile/edit/<int:pk>', views.MyProfileUpdateView.as_view(success_url="/college/home")),
    path('profile/',views.MyProfileUpdateView.as_view(success_url="/college/home")),
    path('registration_form/',views.RegisterView.as_view()),
    path('notice/<int:pk>', views.NoticeDetailView.as_view()),
    path('contribute/',views.Contribute.as_view()),
    path('myprofile/edit/<int:pk>', views.MyProfileUpdateView.as_view(success_url="/college/home")),
    path('', RedirectView.as_view(url="home/")),

]
