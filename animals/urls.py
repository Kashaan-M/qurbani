from django.urls import path
from . import views
app_name = "animals"
urlpatterns = [
    path("", views.homepage, name="home"),
    path("goats/", views.BakraListView.as_view(),name = "bakra-list"),
    path("goats/<uuid:pk>/", views.BakraDetailView.as_view(), name="bakra-detail"),
    path("vehras/", views.VehraListView.as_view(),name = "vehra-list"),
    path("vehras/<uuid:pk>/", views.VehraDetailView.as_view(), name="vehra-detail"),
    path("sheeps/", views.SheepListView.as_view(),name = "sheep-list"),
    path("sheeps/<uuid:pk>/", views.SheepDetailView.as_view(), name="sheep-detail"),
    path("camels/", views.CamelListView.as_view(),name = "camel-list"),
    path("camels/<uuid:pk>/", views.CamelDetailView.as_view(), name="camel-detail"),
]