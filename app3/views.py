from django.shortcuts import render

# Create your views here.
#httpResponse is used for responding a string
#render fun is used for responding an entire html file
#syntax of render fun
    #render(request,'html filename along with extension')

def temp(request):
    return render(request,'h1.html')
def select(request):
    return render(request,'h2.html')    
