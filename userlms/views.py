from django.shortcuts import redirect, render
from django.contrib.auth.models import User

def base(request):
    return render(request, "base.html")