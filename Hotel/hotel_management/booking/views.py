from datetime import datetime

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Hotel, Room, Booking, CustomUser
from .forms import HotelForm, RoomForm, BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from .forms import CustomUserCreationForm
from django.views import View
from django.contrib import messages


def index(request):
    search_query = request.GET.get('search')
    if search_query:
        hotels = Hotel.objects.filter(name__icontains=search_query)
    else:
        hotels = Hotel.objects.all()
    return render(request, 'booking/index.html', {'hotels': hotels})


@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile_view')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', 'index'))


class RoomListView(View):
    def get(self, request, hotel_id):
        hotel = get_object_or_404(Hotel, id=hotel_id)
        rooms = hotel.rooms.all()
        return render(request, 'booking/room_list.html', {'hotel': hotel, 'rooms': rooms})


class RoomBookingView(View):
    def get(self, request, room_id):
        room = get_object_or_404(Room, id=room_id)
        return render(request, 'booking/book_room.html', {'room': room})

    def post(self, request, room_id):
        room = get_object_or_404(Room, id=room_id)
        user = request.user

        guest_name = request.POST.get("guest_name")
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")

        check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
        check_out_date = datetime.strptime(check_out, '%Y-%m-%d').date()

        if check_in_date >= check_out_date:
            messages.error(request, "Дата виїзду повинна бути пізніше дати заїзду.")
            return redirect('book_room', room_id=room.id)

        booking = Booking(
            user=user,
            room=room,
            start_date=check_in_date,
            end_date=check_out_date,
            guest_name=guest_name
        )

        booking.save()

        messages.success(request, "Ви успішно забронювали кімнату!")
        return redirect('booking_list')

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/booking_list.html', {'bookings': bookings})
