"""
URL configuration for obs_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views as h1
from customer import views as a1
from vendor import views as a2
from contact import views as c1

urlpatterns = [
    path('c_profileupdate/', a1.c_profileupdate, name='c_profileupdate'),
    path('vendor_profileupdate/', a2.vendor_profileupdate, name='vendor_profileupdate'),
    path('v_profileupdate/', a2.v_profileupdate, name='v_profileupdate'),
    path('addbook/', a2.addbook, name='addbook'),
    path('add_book/', a2.add_book, name='add_book'),
    path('customer_profileupdate/', a1.customer_profileupdate, name='customer_profileupdate'),
    path('delete_vendoruser/<int:user_id>/', a2.delete_vendoruser, name='delete_vendoruser'),
    path('get_user_vendordata/<int:user_id>/', a2.get_user_vendordata, name='get_user_vendordata'),
    path('update_vendoruser/', a2.update_vendoruser, name='update_vendoruser'),
    path('userlogin/', a1.userlogin, name='userlogin'),
    path('delete_user/<int:user_id>/', a1.delete_user, name='delete_user'),
    path('get_user_data/<int:user_id>/', a1.get_user_data, name='get_user_data'),
    path('update_user/', a1.update_user, name='update_user'),
    path('customer/', a1.customer, name='customer'),
    path('vendor/', a2.vendor, name='vendor'),
    path('customer_signuplist/', a1.customer_signuplist, name='customer_signuplist'),
    path('vendor_signuplist/', a2.vendor_signuplist, name='vendor_signuplist'),
    path('contactus_list/', c1.contactus_list, name='contactus_list'),
    path('requestbook_list/', c1.requestbook_list, name='requestbook_list'),
    path('register/', a1.register, name='register'),
    path('contactus/', c1.contactus, name='contactus'),
    path('requestbook/', c1.request_a_book, name='requestbook'),
    path('admin/', admin.site.urls),
    path('',h1.home, name='home'),
    path('about_us/',h1.about_us, name='about_us'),
    path('art_&_photography/',h1.art_photography,name='art_&_photography'),
    path('award_winning/', h1.award_winning, name='award_winning'),
    path('best_seller/',h1.best_seller,name='best_seller'),
    path('Biographies_&_Memoirs/',h1.biographies_memories,name='Biographies_&_Memoirs'),
    path('box_sets/',h1.box_sets,name='box_sets'),
    path('contact/',h1.contact,name='contact'),
    path('Dictionaries_&_Language/',h1.dictionaries_language,name='Dictionaries_&_Language'),
    path('featured_authors/',h1.featured_authors,name='featured_authors'),
    path('fiction_books/',h1.fiction_books,name='fiction_books'),
    path('Fiction/',h1.fiction,name='Fiction'),
    path('forgot_password/',h1.forgot_password,name='forgot_password'),
    path('law/',h1.law,name='law'),
    path('login/',h1.login,name='login'),
    path('medicine/',h1.medicine,name='medicine'),
    path('new_arrivals/',h1.new_arrivals, name='new_arrivals'),
    path('request_a_book/',h1.request_a_book,name='request_a_book'),
    path('signup/',h1.signup,name='signup'),
    path('Society/',h1.society,name='Society'),
    path('todays_deals/',h1.todays_deals,name='todays_deals'),
]
