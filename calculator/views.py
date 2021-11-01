from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'calculator/home.html')

def calculatorOneView(request):
    # calculator one view
    return render(request, 'calculator/calc1.html')

def calculatorTwoView(request):
    # calculator two view
    return render(request, 'calculator/calc2.html')

def calculatorThreeView(request):
    # calculator three view
    return render(request, 'calculator/calc3.html')