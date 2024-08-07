from django.forms import fields, models
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.views.generic.edit import UpdateView
from .models import Vendor, Review, Images, Service, Contact, MembershipForm, QuoteRequest
from django.contrib import messages
from django.views.generic import CreateView, ListView, DetailView, UpdateView
# from .forms import PostService


# Create your views here.
def index(request):
    reviews = Review.objects.all()

    images = Images.objects.all()

    return render(request, 'twpn/index.html', {'reviews': reviews, 'images':images})

def about(request):
    return render(request, 'twpn/about.html')

def studios(request):
    images = Images.objects.all()

    kvendors = Vendor.objects.filter(vendor_district__exact="Kathmandu")
    bvendors = Vendor.objects.filter(vendor_district__exact="Bhaktapur")
    lvendors = Vendor.objects.filter(vendor_district__exact="Lalitpur")
    return render(request, 'twpn/studios.html', {'images':images, 'bvendors': bvendors, 'kvendors': kvendors, 'lvendors': lvendors,})

def gallery(request):
    images = Images.objects.all()

    return render(request, 'twpn/gallery.html', {'images':images})

def membership(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        bname = request.POST['bname']
        weburl = request.POST['weburl']
        email = request.POST['email']
        contact = request.POST['contact']
        district = request.POST['district']
        address = request.POST['address']
        msg = request.POST['info']

        print(fname, lname, bname, weburl, email, contact, district, address, msg)

    return render(request, 'twpn/membership.html')

def dashboard(request):
    images = Images.objects.all()
    vendors = Vendor.objects.all()
    return render(request, 'twpn/dashboard.html', {'images':images, 'vendors': vendors})

def kathmandu(request):
    images = Images.objects.all()
    kvendors = Vendor.objects.filter(vendor_district__exact="Kathmandu")
    return render(request, 'twpn/kathmandu.html', {'images':images, 'kvendors': kvendors})

def selectvendor(request):
    if request.method == 'POST':
        vendorid = request.POST['vendor_id']

        images = Images.objects.all()
        vendors = Vendor.objects.all()
        return render(request, 'twpn/selectvendor.html', {'images':images, 'vendors': vendors, 'vendorid':vendorid})

def comparetable(request):
    if request.method == 'POST':
        vendor_id1 = request.POST['vendorid']
        vendor_id2 = request.POST['vendor_id']

        services = Service.objects.all()
        vendorid1 = Vendor.objects.filter(vendor_id=vendor_id1)
        vendorid2 = Vendor.objects.filter(vendor_id=vendor_id2)
        return render(request, 'twpn/comparetable.html', {'services':services, 'vendorid1': vendorid1, 'vendorid2':vendorid2})

def lalitpur(request):
    images = Images.objects.all()
    lvendors = Vendor.objects.filter(vendor_district__exact="Lalitpur")
    return render(request, 'twpn/lalitpur.html', {'images':images, 'lvendors': lvendors})

def bhaktapur(request):
    images = Images.objects.all()
    bvendors = Vendor.objects.filter(vendor_district__exact="Bhaktapur")
    return render(request, 'twpn/bhaktapur.html', {'images':images, 'bvendors': bvendors})

def studioview(request):
    if request.method == 'POST':
        vendorid = request.POST['vendor_id']
        print(vendorid)

    images = Images.objects.all()
    vendors = Vendor.objects.filter(vendor_id=vendorid)
    return render(request, 'twpn/studioview.html', {'images':images, 'vendors': vendors})

def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact(name=name, number=number, email=email, content=message)
        contact.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def requestid(request):
    if request.method == 'POST':
        vendorname = request.POST['vendor_id']
    return render(request, 'twpn/requestquote.html', {'vendor_id':vendorname})

def requestquote(request):
    if request.method == 'POST':
        vendorid = request.POST['vendor_id']
        fname = request.POST['fname']
        lname = request.POST['lname']
        number = request.POST['contact']
        email = request.POST['email']
        message = request.POST['info']

        quote = QuoteRequest(vendor_id=vendorid, fname = fname, lname = lname, contact=number, email=email, msg=message)
        quote.save()
    
    images = Images.objects.all()
    vendors = Vendor.objects.filter(vendor_id=vendorid)
    return render(request, 'twpn/studioview.html', {'images':images, 'vendors': vendors})

def addreview(request):
        if request.method == 'POST':
            vendor = request.POST['vendors']
            rate = request.POST['rating']
            fname = request.POST['fname']
            lname = request.POST['lname']
            uname = fname + lname
            email = request.POST['email']
            servicedate = request.POST['userservicedate']
            userreview = request.POST['info']
            # print(vendor, rate, uname, email, servicedate, userreview)
            userReview = Review(vendor_name=vendor, rating = rate, user_name = uname, user_email=email, user_serviceDate = servicedate, review=userreview)
            userReview.save()
    
        vendors = Vendor.objects.all()
        # vendors = Vendor.objects.filter(vendor_id=vendorid)
        return render(request, 'twpn/addreview.html', {'vendors': vendors})



# def editprofile(request):
#     images = Images.objects.all()
#     vendors = Vendor.objects.all()
#     return render(request, 'twpn/editprofile.html', {'vendors':vendors, 'images': images})

def viewreview(request):
    images = Images.objects.all()
    vendors = Vendor.objects.all()
    reviews = Review.objects.all()
    print(reviews)
    return render(request, 'twpn/viewreview.html', {'reviews': reviews, 'vendors':vendors, 'images': images})

def viewquote(request):
    images = Images.objects.all()
    vendors = Vendor.objects.all()
    quotes = QuoteRequest.objects.all()
    print(quotes)
    return render(request, 'twpn/viewquote.html', {'quotes': quotes, 'vendors':vendors, 'images': images})


class AddServiceView(CreateView):
    model = Service
    template_name = 'twpn/addservice.html'
    fields = '__all__'

class AddImageView(CreateView):
    model = Images
    template_name = 'twpn/addimage.html'
    fields = '__all__'

class ServiceView(ListView):
    model = Service
    template_name = 'twpn/viewservice.html'
    fields = '__all__'

class ServiceEdit(UpdateView):
    model = Service
    template_name = 'twpn/editservice.html'
    fields = ['service_name', 'service_price', 'service_desc']

class ProfileEdit(UpdateView):
    model = Vendor
    template_name = 'twpn/editprofile.html'
    fields = ['vendor_name', 'vendor_address', 'vendor_district', 'vendor_contact', 'vendor_email', 'vendor_desc']