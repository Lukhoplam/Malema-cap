from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.

def biography(request):
    return render(request, 'biography.html')

def life_education(request):
    return render(request, 'life_education.html')

def anc_youth(request):
    return render(request, 'anc_youth.html')

def function_name(parameter1, parameter2):
    """
    Brief description of what the function does.

    Parameters:
    parameter1 (type): Description of the first parameter.
    parameter2 (type): Description of the second parameter.

    Returns:
    return_type: Description of what the function returns.
    """
    pass
