# from django.shortcuts import render

# Create your views here.
def login(requset):
    error_msg = ''
    if requset.method == 'post':
        print(requset.POST['email'])
        email = requset.POST.get('email', None)