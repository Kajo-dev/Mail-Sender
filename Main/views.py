from django.shortcuts import render

def v_welcome(request):   
    return render(request,'welcome.html',{})


