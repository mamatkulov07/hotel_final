from django.urls import path
from .views import *

urlpatterns = [
    path('', UserProfileViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='userprofile_list'),

    path('userprofile/<int:pk>/', UserProfileViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='userprofile_detail'),

    path('hotel/', HotelViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='hotel_list'),

    path('hotel/<int:pk>/', HotelViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='hotel_detail'),

    path('image/', ImageViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='image_list'),

    path('image/<int:pk>/', ImageViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='image_detail'),

    path('room/', RoomViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='room_list'),

    path('room/<int:pk>/', RoomViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='room_detail'),

    path('imageroom/', ImageRoomViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='imageroom_list'),

    path('imageroom/<int:pk>/', ImageRoomViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='imageroom_detail'),

    path('comment/', CommentViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='comment_list'),

    path('comment/<int:pk>/', CommentViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='comment_detail'),

    path('booking/', BookingViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='booking_list'),

    path('booking/<int:pk>/', BookingViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='booking_detail'),

]
