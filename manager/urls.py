from django.urls import path,re_path,include
from . import views


urlpatterns = [
    path("", views.manager, name="manager"),
    path("1", views.manager1, name="1"),
    path("2", views.manager2, name="2"),
    path("3", views.manager3, name="3"),
    path("delete1/<room_id>", views.delete1, name="delete1"),
    path("delete2/<cab_id>", views.delete2, name="delete2"),
    path("delete3/<com_id>", views.delete3, name="delete3"),
    path("cross_off2/<cab_id>", views.cross_off2, name="cross_off2"),
    path("cross_off1/<room_id>", views.cross_off1, name="cross_off1"),
    path("cross_off3/<com_id>", views.cross_off3, name="cross_off3"),
    path("uncross1/<room_id>", views.uncross1, name="uncross1"),
    path("uncross2/<cab_id>", views.uncross2, name="uncross2"),
    path("uncross3/<com_id>", views.uncross3, name="uncross3"),
]

