from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('hotel/<int:hotel_id>/rooms/', views.RoomListView.as_view(), name='room_list'),
    path('room/<int:room_id>/book/', views.RoomBookingView.as_view(), name='book_room'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login_view'),
    path('accounts/profile/', views.profile_view, name='profile_view'),
    path('logout/', views.logout_view, name='logout_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)