from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('check_booking/', check_booking),
    path('', home, name='home'),
    path('hotel-detail/<uid>/', hotel_detail, name="hotel_detail"),
    path('login/', login, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('profile/', user_profile, name="profile"),
    path('logout/', logout, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )


urlpatterns += staticfiles_urlpatterns()
