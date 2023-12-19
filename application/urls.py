from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('google_earth/', views.google_earth, name='google_earth'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
<<<<<<< HEAD
    path('about_us/', views.about_us, name='about_us'),
=======
    path('map/', views.map_data, name='map'),
    path('google_earth_old/', views.google_earth_old, name='google_earth_old'),
>>>>>>> 4411a582a64715377c5c4cb4da18fdb946208d63
]
