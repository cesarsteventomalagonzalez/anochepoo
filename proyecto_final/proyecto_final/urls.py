from django.urls import path,include
from .views import Principal,Linea,Productos
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Principal.as_view(),name="menu"),
    path('linea/',Linea.as_view(),name="linea"),
    path('producto',Productos.as_view(),name="producto"),

    path('sa/',include('Ventas.urls'))
]