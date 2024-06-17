from django.shortcuts import render
from django.http import HttpResponse
from contact.models import contact
from contact.models import requestbook


#create your views for contactus page
def contactus(request):
    if request.method == 'POST':
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        mobile_no=request.POST.get('mobile_no')
        location=request.POST.get('location')
        message=request.POST.get('message')
        contact.objects.create(FullName=fullname,Email=email,Mobile_No=mobile_no,Location=location,Message=message)
        return HttpResponse("Form submitted successfully!")

    else:
        return render(request, 'contact.html')
    

#create your views for requesting book page
def request_a_book(request):
    if request.method == 'POST':
        isbn_no=request.POST.get('isbn_no')
        booktitle=request.POST.get('booktilte')
        authorname=request.POST.get('authorname')
        quantity=request.POST.get('quantity')
        emailid=request.POST.get('emailid')
        mobileno=request.POST.get('mobileno')
        requestbook.objects.create(ISBN_No=isbn_no,BookTitle=booktitle,AuthorName=authorname,Quantity=quantity,EmailID=emailid,Mobile_No=mobileno)
        return HttpResponse("Form submitted successfully!")

    else:
        return render(request, 'request_a_book.html')
#creating form views

def contactus_list(request):
    data=contact.objects.all()
    mydata={'result':data}
    return render(request,'contactus_list.html', mydata)


def requestbook_list(request):
    data=requestbook.objects.all()
    yourdata={'result':data}
    return render(request, 'requestbook_list.html', yourdata)