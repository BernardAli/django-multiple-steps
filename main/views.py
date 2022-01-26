from django.shortcuts import render, reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import MultiStepFormModel
# Create your views here.


def index_view(request):
    return render(request, 'index.html')


def multistepformexample(request):
    return render(request, "multistepformexample.html")


def multistepformexample_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("multistepformexample"))
    else:
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        phone = request.POST.get("phone")
        twitter = request.POST.get("twitter")
        facebook = request.POST.get("facebook")
        gplus = request.POST.get("gplus")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        cpass = request.POST.get("cpass")
        if password != cpass:
            messages.error(request, "Confirm Password Doesn't Match")
            return HttpResponseRedirect(reverse('multistepformexample'))

        try:
            multistepform = MultiStepFormModel(fname=fname, lname=lname, phone=phone,twitter=twitter,facebook=facebook,gplus=gplus,email=email,password=password)
            multistepform.save()
            messages.success(request,"Data Save Successfully")
            return HttpResponseRedirect(reverse('multistepformexample'))
        except:
            messages.error(request,"Error in Saving Data")
            return HttpResponseRedirect(reverse('multistepformexample'))

