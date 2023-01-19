from django.contrib import admin
from django.urls import path, include
from .views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    #path('register/', include('registerUser.urls'))
    path('request/', include('request.urls'))
]
