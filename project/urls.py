from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('', include('hotel.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('manager/', include('manager.urls'))
]