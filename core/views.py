from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos.</h1>'. format(nome, idade))
def soma(request, a, b):
    soma = a + b
    return HttpResponse('<h1>A soma de {}+{} = {}.</h1>'.format(a, b, soma))
def subtracao(request, a, b):
    subtracao = a - b
    return HttpResponse('<h1>A subtração de {}-{} = {}.</h1>'.format(a, b, subtracao))
def multiplicacao(request, a, b):
    multiplicacao = a * b
    return HttpResponse('<h1>A multiplicação de {}x{} = {}.</h1>'.format(a, b, multiplicacao))
def divisao(request, a, b):
    divisao = a / b
    return HttpResponse('<h1>A divisão de {}/{} = {}.</h1>'.format(a, b, divisao))

