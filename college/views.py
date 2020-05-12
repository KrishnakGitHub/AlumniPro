from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from college.models import Notice, Profile
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.template.backends.django import Template


# Create your views here.

class HomeView(TemplateView):
    template_name = "college/home.html"
    
class AboutView(TemplateView):
    template_name = "college/about.html"


class ContactView(TemplateView):
    template_name = "college/contact.html"


class Contribute(TemplateView):
    template_name = "college/contribute.html"


@method_decorator(login_required, name="dispatch")
class NoticeListView(ListView):
    model = Notice

    def get_queryset(self):
        si = self.request.GET.get('si')
        if si == None:
            si = ''
        if self.request.user.is_superuser:
            return Notice.objects.filter(Q(msg__icontains=si) | Q(subject__icontains=si)).order_by('-id')
        else:
            return Notice.objects.filter(Q(branch__isnull=True) | Q(branch=self.request.user.profile.branch)).filter(
                Q(msg__icontains=si) | Q(subject__icontains=si)).order_by('-id')


@method_decorator(login_required, name="dispatch")
class NoticeDetailView(DetailView):
    model = Notice


@method_decorator(login_required, name="dispatch")
class MyProfileUpdateView(UpdateView):
    model = Profile
    fields = ["name", "age", "address", "status", "gender", "phone_no", "description", "pic"]


class RegisterView(TemplateView):
    template_name = "college/insideregistration.html"
