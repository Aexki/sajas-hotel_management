from django.urls import path,re_path,include
from . import views


urlpatterns = [
    path("register", views.register ,name="register"),
    path("login", views.login ,name="login"),
    path("preference", views.preference, name="preference"),
    path("feature", views.feature, name="feature"),
    path("business_feature", views.business_feature, name="business_feature"),
    path("cab", views.cab, name="cab"),
    path("thanku", views.thanku, name="thanku"),
    path("bthanku", views.bthanku, name="bthanku"),
    path("food", views.food, name="food"),
    path("logout", views.logout, name="logout")
]

