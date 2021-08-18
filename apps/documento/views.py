from django.shortcuts import render


def Documento(request):
    return render(request, 'documento/index.html')
