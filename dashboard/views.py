from django.shortcuts import render
from growthTest.models import *

# Create your views here.
def dashboard(request):
    r = Result.objects.all()
    return render(request, "dashboard/tables.html", {"result_list":r})