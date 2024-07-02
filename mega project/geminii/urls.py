from django.urls import path,include
from . import views 
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('home', views.home, name = 'home' ),
    path('signup/',views.SignupPage,name='signup'),
    path('',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)