from django.urls import path
from . import views


app_name = 'portal'

urlpatterns = [
    # path('',views.portal, name="portal"),
    path('generate_new_table',views.generate_new_table, name="generate_new_table"),
    path('update_table',views.update_table, name="update_table"),
    path('generate_geojson',views.generate_geojson, name="generate_geojson"),
    path('getcounties_view',views.getcounties_view, name="getcounties_view"),
    path('getstates_view',views.getstates_view, name="getstates_view"),
]