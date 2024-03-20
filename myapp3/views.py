
from django.shortcuts import render
from .forms import FiboForm
from django.http import HttpResponse


def fibo(n):
 if n == 0:
  return 0
 elif n == 1:
   return 1
 else:
   return(fibo(n-1)+fibo(n-2))
 
def index(request):
    if request.method == 'POST':
        form = FiboForm(request.POST)
        if form.is_valid():
            num = form.cleaned_data['num']
            num = int(num)
            
            FibList=[]
            for i in range(num+1):
                FibList.append(fibo(i))
            b=str(FibList)
            return HttpResponse(b)
            return HttpResponse(b)
    else:
        form = FiboForm()
    return render(request, 'myapp3/Fibo.html', {'form': form})




