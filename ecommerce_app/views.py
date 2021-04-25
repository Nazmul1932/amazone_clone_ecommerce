from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse


def demoPage(request):
    return HttpResponse("demo Page")


def demoPageTemplate(request):
    return render(request, "demo.html")


def adminLogin(request):
    return render(request, 'admin/signin.html')


def adminLoginProcess(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(request=request, username=username, password=password)
    if user is not None:
        login(request=request, user=user)
        return HttpResponseRedirect(reverse("admin-home"))
    else:
        messages.error(request, "Invalid login credentials")
        return HttpResponseRedirect(reverse("admin-login"))


def adminLogoutProcess(request):
    logout(request)
    messages.success(request, "Logout Successfully!")
    return HttpResponseRedirect(reverse("admin-login"))