import django
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
# Create your views here.
# Create your views here.
from django.template import loader, RequestContext
from django.utils import timezone
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from MyApplication.models import *
import json
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

@django.views.decorators.csrf.csrf_exempt

# def index(request):
#     latest_question_list = Question.objects.order_by('published_date')
#     template = loader.get_template('MyApplication/index.html')
#     context =  RequestContext(request,{'latest_question_list',latest_question_list})
#     output = ','.join([p.question_text for p in latest_question_list])
#     context ={'latest_question_list',latest_question_list}
#     return render(request,'MyApplication/index.html',context)
    # return HttpResponse(template.render(context))
    # return HttpResponse("Hello, You are at View")

def detail(request, question_id):
    question =get_object_or_404(Question, pk=question_id)
    return render(request,'MyApplication/detail.html',{'question':question})
    # try:
    #     question=Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    #     return render(request,'polls/detail.htnl',{'question':question})
    # return HttpResponse("You are looking at Question %s" %question_id)

def result(request, question_id):
     return HttpResponse("You're seeing result on question %s." %question_id)


def vote(request, question_id):
    p=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=p.choice_set.get(pk=request.POST["choice"])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'MyApplication/detail.html',{'question' : p,'error_message' : "Please select a choice"})
    else:
        selected_choice+=1
        selected_choice.save()
    # return HttpResponse("You're voting on question %s." %question_id)
        return HttpResponseRedirect(reverse('MyApplication:result',args=(p.id,)))

class IndexView(generic.ListView):
    template_name = 'MyApplication/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')[:5]


def user_register(request):
    return render(request,'MyApplication/register.html')


def register_submit(request):
    if len(request.POST["username"])==0 or len(request.POST["email"])==0 or len(request.POST["contact"])==0 or len(request.POST["password"])==0:
        return render(request,'MyApplication/register.html',{'error_message' : "Please fill all fields"})
    else:
        userName=request.POST.get("username")
        userEmail=request.POST.get("email")
        userContact=request.POST.get("contact")
        userPassword=request.POST.get("password")
        UserInfo.objects.create(user_name=userName,user_email=userEmail,user_contact=userContact,user_password=userPassword)

        return render(request,'MyApplication/login.html')

def user_login(request):
    return render(request,'MyApplication/login.html')


def index(request):
    return render(request,'MyApplication/home.html')

def network(request):
    return render(request,'MyApplication/network.html')

def base(request):
    context={
        'user_email':UserInfo.objects.all(),
        'user_contact':UserInfo.objects.all()
    }
    return render(request,'MyApplication/base.html',context)
# class auth_complete(View):
#     def get(self, request, *args, **kwargs):
#         backend=kwargs.pop('backend')
#         try:
#             return complete(request, backend,*args,**kwargs)
#         except AuthFailed:
#             messages.error(request, "Your Google Apps domain isn't authorized for this app")
#             return HttpResponseRedirect(reverse('login'))
#
# class LoginError(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse(status=401)
# All definition takes name as parameter,
# like contact=request.post.get('name which is contact in index.html')

def request_home(request):
    if request.POST:
        if request.POST.get('contact')=="" or request.POST.get('password')=="":
            return render(request,'MyApplication/login.html',{'error_message' : "Please fill all details"})
        else:
            contact=request.POST.get('contact')
            password=request.POST.get('password')
            user=UserInfo.objects.get(user_contact=contact)
            if(user.user_password_detail()==password):
                return render(request,'MyApplication/index.html')
            else:
                return render(request,'MyApplication/login.html',{'error_message' : 'Details are not correct'})




#//////////////////////Minovate////////////////////////////////////////////////////////

def index_minovate(request):
    return render(request,'minovate/index.html')

def login_minovate(request):
    return render(request,'minovate/login.html')

def signup_minovate(request):
    return render(request,'minovate/signup.html')


def forget_password(request):
    return render(request,'minovate/forgotpass.html')