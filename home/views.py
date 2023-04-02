from django.shortcuts import render

# Create your views here.



def home(request):
    # jobs = Company_detail.objects.all()
    # form = newsletterform(request.POST or None)
    # if form.is_valid():
    #     form.save()

    # context =  {'jobs':jobs, 'form':form}
    return render(request, 'index.html' )


def Login(request):
    # jobs = Company_detail.objects.all()
    # form = newsletterform(request.POST or None)
    # if form.is_valid():
    #     form.save()

    # context =  {'jobs':jobs, 'form':form}
    return render(request, 'login.html' )


def history(request):
    # jobs = Company_detail.objects.all()
    # form = newsletterform(request.POST or None)
    # if form.is_valid():
    #     form.save()

    # context =  {'jobs':jobs, 'form':form}
    return render(request, 'History.html' )

def payment(request):
    # jobs = Company_detail.objects.all()
    # form = newsletterform(request.POST or None)
    # if form.is_valid():
    #     form.save()

    # context =  {'jobs':jobs, 'form':form}
    return render(request, 'payment.html' )


def makeRequest(request):
    # jobs = Company_detail.objects.all()
    # form = newsletterform(request.POST or None)
    # if form.is_valid():
    #     form.save()

    # context =  {'jobs':jobs, 'form':form}
    return render(request, 'requestmoney.html' )
