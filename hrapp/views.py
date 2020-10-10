from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from .forms import SignupForm,JobpostForm
from .models import Jobpost
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.urls import reverse
import random
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q



# Create your views here.
def index(request):
    return render(request,'hrapp/index.html')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    else:
        
        jobs = Jobpost.objects.filter(user=request.user)
        context = {
            'jobs':jobs
        }
        return render(request,"hrapp/profile.html",context)


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login_user')
    
    else:
        form = SignupForm()
    
    context = {'form':form}
    return render(request,'hrapp/signup.html',context)



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'hrapp/login.html', {})
    

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))




def create_jobpost_view(request):

    if not request.user.is_authenticated:

        return redirect('login_user')

    else:

        if request.method == "POST":

            fm = JobpostForm(request.POST, request.FILES)

            if fm.is_valid():
                referal = fm.save(commit=False)
                referal.user = request.user
                referal.referal_code = get_random_string(length=8) #random.randint(1000,10000)
                referal.save()
                return redirect('display_jobpost')

        else:
            fm = JobpostForm()

        return render(request,'hrapp/jobapply.html',{'form':fm})


def display_jobpost(request):

    jobposts = Jobpost.objects.all()
    

    return render(request,'hrapp/joblisting2.html',{'jobs':jobposts})



def sendmail(request):
    #referal_code = Jobpost.objects.get(id=id)

    #jobs = Jobpost.objects.get(id=id)
    #receiver_email = request.user.email
    emails = User.objects.get(is_active=True).values_list('email', flat=True)
    from_email = settings.EMAIL_HOST_USER
    subject = 'Selection EMail'
    message = 'Congrulations'
    send_mail(
        subject,
        message,
        from_email,
        [emails],
        fail_silently=False
    )

    return HttpResponse("Send Successfully")


def search_title_company(request):
    query = request.GET.get('q','')
    if query:
            queryset = (Q(company_name__icontains=query)|Q(designation__icontains=query))
            results = Jobpost.objects.filter(queryset).distinct()
    else:
       results = []
    return render(request, 'hrapp/search_title_company.html', {'results':results, 'query':query})



def search_place(request):
    query = request.GET.get('q','')
    if query:
            queryset = (Q(place=query))
            results = Jobpost.objects.filter(queryset).distinct()
    else:
       results = []
    return render(request, 'hrapp/search_place.html', {'results':results, 'query':query})