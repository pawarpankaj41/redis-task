from django.urls import path
from .views import import_device_info_from_excel, location_points, device_latest_info, start_end_location

urlpatterns = [
    path("bulk_import/", import_device_info_from_excel),
    path("location_points/", location_points),
    path("latest_info/", device_latest_info),
    path("start_end_location/", start_end_location),

]
