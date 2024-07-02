from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
# Used to securely store your API key
# from google.colab import userdata

# Create your views here.
def home(request):
    return render(request, "index.html")

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        print(uname ,email,pass1,pass2)

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'login.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('login_username')
        pass1=request.POST.get('login_password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


#google collab module is not installing ... having package issue ...
# def geminii(request):

        
#         # Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
#         GOOGLE_API_KEY = userdata.get('AIzaSyDLW0ZzUp32rgwCYVMsnTGNwuhn1ZOTels')

#         genai.configure(api_key=GOOGLE_API_KEY)

#         for m in genai.list_models():
#             if 'generateContent' in m.supported_generation_methods:
#                 print(m.name)
#         model = genai.GenerativeModel('gemini-1.5-flash')

#         response = model.generate_content("What is the meaning of life?")

        
#         return HttpResponse("google colab is not working !!")
