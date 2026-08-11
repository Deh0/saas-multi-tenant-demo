from django.shortcuts import render
from django.http import HttpResponse

def tenant_list(request):
    return HttpResponse("Lista de tenants")