from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Olá, Você está na index do app pesquisas.")


def dizer_oi(request):
    return HttpResponse("Oi")


def dizer_tchau(request):
    return HttpResponse("Oi")


def somar_numeros(request):
    a = 5
    b = 10
    resultado = a + b
    return HttpResponse(f"A soma de {a} e {b} é {resultado}.")
