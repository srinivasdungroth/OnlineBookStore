from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.http import HttpResponse
from customer.models import users

# Create your views here.
def register(request):
    #get the data
    if request.method == 'POST':
        #get the form fields data 
        usertype=request.POST.get('usertype')
        if usertype == 'Customer':
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            email_customer=request.POST.get('email')
            password=request.POST.get('password')
            confirm_password=request.POST.get('confirm_password')
            address=request.POST.get('address')
            mobile_no=request.POST.get('mobile_no')
            zip_code=request.POST.get('zip_code')
            # Password validation
            if password != confirm_password:
                messages.error(request, "Passwords do not match.")
                return redirect('register') 
            new_customer = users.objects.create(UserType=usertype,FirstName=firstname,LastName=lastname,Username=email_customer,Password=password,Mobile_No=mobile_no,Address=address,Zipcode=zip_code)
            new_customer.save()
            messages.success(request, "You have successfully signed up as a Customer!")
            return redirect('login') 
        elif usertype == 'Vendor':
            company_name=request.POST.get('company_name')
            company_location=request.POST.get('company_location')
            gstno=request.POST.get('gstno')
            email_vendor=request.POST.get('email')
            password=request.POST.get('password')
            confirm_password=request.POST.get('confirm_password')
            address=request.POST.get('address')
            mobile_no=request.POST.get('mobile_no')
            zip_code=request.POST.get('zip_code')
            # Password validation
            if password != confirm_password:
                messages.error(request, "Passwords do not match.")
                return redirect('register') 
            new_vendor = users.objects.create(UserType=usertype,CompanyName=company_name,CompanyLocation=company_location,GST_No=gstno,Username=email_vendor,Password=password,Mobile_No=mobile_no,Address=address,Zipcode=zip_code)
            new_vendor.save()
            messages.success(request, "You have successfully signed up as a Vendor!")
            return redirect('login')  
        else:
         return render(request, 'signup.html')
    
def customer(request):  
    return render(request,'customer.html')

def customer_profileupdate(request):
    user_data = request.session.get('user')
    if user_data:
        user_id = user_data['UserID']
        try:
            user = users.objects.get(UserID=user_id)
            return render(request, 'customer_profileupdate.html', {'user': user})
        except users.DoesNotExist:
            return HttpResponse("User details not found.")
    else:
        return HttpResponse("User details not found.")

def customer_signuplist(request):
    customer_data=users.objects.filter(UserType='Customer')
    mydata={'result':customer_data}
    return render (request, 'customer_signuplist.html', mydata)
    
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usertype = request.POST.get('usertype')
        if usertype:
            user = users.objects.filter(Username=username, Password=password, UserType=usertype).first()
            if user is not None:
                if usertype == 'Customer':
                    request.session['user'] = {'UserID': user.UserID,'FirstName': user.FirstName,'LastName': user.LastName,'Email': user.Username,'Password': user.Password,'MobileNo': user.Mobile_No,'Address': user.Address,'ZipCode': user.Zipcode}
                    return render(request, 'customer.html', {'user': user})
                elif usertype == 'Vendor':
                    request.session['user'] = { 'UserID': user.UserID, 'CompanyName': user.CompanyName, 'CompanyLocation':user.CompanyLocation, 'GST_No':user.GST_No,'Email': user.Username,'Password': user.Password,'MobileNo': user.Mobile_No,'ZipCode': user.Zipcode }
                    return render(request, 'vendor.html', {'user': user})
            else:
                messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def delete_user(request, user_id):
    if request.method == 'POST':
        user = users.objects.get(UserID=user_id)
        user.delete()
        return redirect('customer_signuplist')
    else:
        return redirect('customer_signuplist')


def get_user_data(request, user_id):
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
    


def update_user(request):
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
    

def c_profileupdate(request):
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
            messages.success(request, 'Profile updated successfully.')
            return HttpResponse('Profile updated successfully.')
        except users.DoesNotExist:
            return HttpResponse("User details not found.")
    else:
        return HttpResponse("Invalid request method.")
    
