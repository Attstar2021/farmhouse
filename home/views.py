from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import (authenticate, login, logout)
from django.contrib import messages, auth
from django.http import HttpResponseRedirect, JsonResponse
from .models import (Amenities, Hotel, HotelBooking)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.


def check_booking(start_date, end_date, uid, room_count):
    qs = HotelBooking.objects.filter(
        start_date__lte=start_date, end_date__gte=end_date, hotel__uid=uid
        )

    if len(qs) >= room_count:
        return False

    return True


def user_profile(request):
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})


def home(request):
    amenities_objs = Amenities.objects.all()
    hotels_objs = Hotel.objects.all()

    sort_by = request.GET.get('sort_by')
    search = request.GET.get('search')
    amenities = request.GET.getlist('amenities')
    print(amenities)
    
    if search:
        hotels_objs = hotels_objs.filter(
            Q(hotel_name__icontains=search) |
            Q(description__icontains=search))

    if len(amenities):
        hotels_objs = hotels_objs.filter(
            amenities__amenity_name__in=amenities
            ).distinct()

    context = {
        'amenities_objs': amenities_objs,
        'hotels_objs': hotels_objs,
        'sort_by': sort_by,
        'search': search,
        'amenities': amenities}
    return render(request, 'home.html', context)


def hotel_detail(request, uid):
    hotel_obj = Hotel.objects.get(uid=uid)

    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        hotel = Hotel.objects.get(uid=uid)
        if not check_booking(checkin, checkout, uid, hotel.room_count):
            messages.warning(request, 'Hotel is already booked in these dates')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        HotelBooking.objects.create(
            hotel=hotel, user=request.user,
            start_date=checkin, end_date=checkout,
            booking_type='Pre Paid'
        )

        messages.success(request, 'Your booking has been saved')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'hotel_detail.html', {
        'hotels_obj': hotel_obj
    })


@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('home'))


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if not user_obj.exists():
            messages.warning(request, 'Account not found')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user_obj = authenticate(username=username, password=password)
        if not user_obj:
            messages.warning(request, 'Invalid password ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        login(request, user_obj)
        return redirect('/')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'login.html')



# def login page is up change to login(request):
#     """Return a login page"""
#     if request.user_obj.is_authenticated:
#         return redirect(reverse('home'))
#     if request.method == "POST":
#         login_page = UserLoginForm(request.POST)

#         if login_form.is_valid():
#             user = auth.authenticate(username=request.POST['username'],
#             password=request.POST['password'])
#             messages.success(request, "You have successfully logged in!")

#             if user:
#                 auth.login(user=user, request=request)
#                 return redirect(reverse('home'))
#             else:
#                 login_form.add_error(None, "Your username or password is incorrect")
#     else:
#         login_form = login(request.POST)
#     return render(request, 'login.html', {'login_form': login_form})


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if user_obj.exists():
            messages.warning(request, 'Username already exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return redirect('/')

    return render(request, 'register.html')
