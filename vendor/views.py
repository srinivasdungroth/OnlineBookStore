from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.http import HttpResponse
from customer.models import users
from vendor.models import books 
from django.contrib.auth.models import User

def vendor(request):
    return render(request,'vendor.html')


def vendor_signuplist(request):
    vendor_data=users.objects.filter(UserType='Vendor')
    mydata={'result':vendor_data}
    return render (request, 'vendor_signuplist.html', mydata)

def delete_vendoruser(request, user_id):
    if request.method == 'POST':
        user = users.objects.get(UserID=user_id)
        user.delete()
        return redirect('customer_signuplist')
    else:
        return redirect('customer_signuplist')


def get_user_vendordata(request, user_id):
    try:
        user = users.objects.get(UserID=user_id)
        data = {
            'UserID': user.UserID,
            'FirstName': user.FirstName,
            'LastName': user.LastName,
            'Username': user.Username,
            'Password': user.Password,
            'Mobile_No': user.Mobile_No,
            'Address': user.Address,
            'Zipcode': user.Zipcode
        }
        return JsonResponse(data)
    except users.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    


def update_vendoruser(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile_no = request.POST.get('mobile_no')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')

        try:
            user = users.objects.get(UserID=user_id)
            user.FirstName = firstname
            user.LastName = lastname
            user.Username = email
            user.Password = password
            user.Mobile_No = mobile_no
            user.Address = address
            user.Zipcode = zip_code
            user.save()
            return JsonResponse({'success': 'User data updated successfully'})
        except users.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
def add_book(request):
    user = request.session.get('user')
    if user:
        return render(request, 'add_book.html', {'user': user})
    else:
        return HttpResponse("User details not found.")


def addbook(request):
    if request.method == 'POST':
        image=request.POST.get('image')
        category=request.POST.get('category')
        booktitle=request.POST.get('booktitle')
        authorname=request.POST.get('authorname')
        isbn=request.POST.get('isbn')
        unitprice=request.POST.get('unitprice')
        cutprice=request.POST.get('cutprice')
        quantityavailable=request.POST.get('quantityavailable')
        bindingtype=request.POST.get('bindingtype')
        vendor_id = request.POST.get('vendorID')
        soldby = request.POST.get('soldby')
        books.objects.create(Image=image,CategoryName=category,BookTitle=booktitle,AuthorName=authorname,ISBN=isbn,UnitPrice=unitprice,CutPrice=cutprice,QuantityAvailable=quantityavailable,BindingType=bindingtype,vendorID_id=vendor_id,SoldBy=soldby)
        return HttpResponse("form submitted successfilly!")
    else:
        return render(request, 'add_book.html')
    
def vendor_profileupdate(request):
    user_data = request.session.get('user')
    if user_data:
        user_id = user_data['UserID']
        try:
            user = users.objects.get(UserID=user_id)
            return render(request, 'vendor_profileupdate.html', {'user': user})
        except users.DoesNotExist:
            return HttpResponse("User details not found.")
    else:
        return HttpResponse("User details not found.")
    
def v_profileupdate(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        company_name = request.POST.get('company_name')
        company_location= request.POST.get('company_location')
        gstno = request.POST.get('gstno')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile_no = request.POST.get('mobile_no')
        zip_code = request.POST.get('zip_code')
        try:
            user = users.objects.get(UserID=user_id)
            user.FirstName = company_name
            user.LastName = company_location
            user.Address = gstno
            user.Username = email
            user.Password = password
            user.Mobile_No = mobile_no
            user.Zipcode = zip_code
            user.save()
            messages.success(request, 'Profile updated successfully.')
            return HttpResponse('Profile updated successfully.')
        except users.DoesNotExist:
            return HttpResponse("User details not found.")
    else:
        return HttpResponse("Invalid request method.")