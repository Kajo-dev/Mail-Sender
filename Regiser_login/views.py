from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .models import User


def v_register(request):
    error_list=[]
    if request.method == 'POST':
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if not email:
            error_list.append('Adres e-mail jest wymagany, ')
        if not lastname:
            error_list.append('Imie jest wymagane, ')
        if not firstname:
            error_list.append('Nazwisko jest wymagane, ')
        if password1 != password2:
            error_list.append('Hasła nie są takie same, ')
        if len(password1)<6:
            error_list.append('Hasło jest zbyt krótkie, ')
        data_front={
            'error_list':error_list
        }
        if len(error_list)==0:
            newUser = User.objects.create_user(email=email,firstname=firstname,lastname=lastname,password=password1)
            newUser.save()
            return render(request,'login.html',data_front)

    data_front={
        'error_list':error_list
    }
    return render(request,'Register.html',data_front)


def v_login(request):
    error_list=[]
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            return redirect('welcome_page')
        else:
            error_list.append('Dane do logowania są nieprawidłowe')
            data_front={
                'error_list':error_list
            }
            return render(request,'login.html',data_front)
    data_front={
        'error_list':error_list
    }
    return render(request,'login.html',{})