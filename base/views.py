# Create your views here.
# views.py
import pandas as pd
from django.http import JsonResponse
import json
from django.core.cache import cache


from django.views.decorators.csrf import csrf_exempt

from .models import DeviceInfo

@csrf_exempt
def import_device_info_from_excel(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        print(file.name)
        if not file:
            return JsonResponse({"message": "file Not Given"}, status=400)
        try:
            df = pd.read_csv(file)
            for i, row in df.iterrows():
                DeviceInfo.objects.create(
                    device_fk_id=row['device_fk_id'],
                    latitude=row['latitude'],
                    longitude=row['longitude'],
                    time_stamp=row['time_stamp'],
                    created=row['sts'],
                    speed=row['speed']
                )
            return JsonResponse({"message": "data imported successfully"}, status=200)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=500)
    return JsonResponse({"message": "invalid request"}, status=405)

def device_latest_info(request):
    device_id = request.GET.get('device_id')

    cache_key = f"device_latest_info:{device_id}"
    cached_data = cache.get(f"device_latest_info:{device_id}")
    if cached_data:
        print("FROM REDIS CACHE")
        return JsonResponse(cached_data)

    try:
        device_info = DeviceInfo.objects.filter(device_fk_id=device_id).latest('time_stamp')
    except DeviceInfo.DoesNotExist:
        return JsonResponse({'message': 'device info not found'}, status=404)

    response_data = {
        'device_id': device_info.device_fk_id,
        'latitude': device_info.latitude,
        'longitude': device_info.longitude,
        'time_stamp': device_info.time_stamp.isoformat(),
        'speed': device_info.speed,
    }
    cache.set(cache_key, response_data)

    print('FROM DJANGO DATABASE')

    return JsonResponse(response_data, status=200)

def start_end_location(request):
    device_id = request.GET.get('device_id')

    cache_key = f"start_end_location:{device_id}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return JsonResponse(cached_data)

    try:
        start_location = DeviceInfo.objects.filter(device_fk_id=device_id).earliest('time_stamp')
        end_location = DeviceInfo.objects.filter(device_fk_id=device_id).latest('time_stamp')
    except DeviceInfo.DoesNotExist:
        return JsonResponse({'message': 'device info not found'}, status=404)

    response_data = {
        'device_id': device_id,
        'start_location': (start_location.latitude, start_location.longitude),
        'end_location': (end_location.latitude, end_location.longitude),
    }
    cache.set(cache_key, response_data)

    return JsonResponse(response_data)

def location_points(request):
    device_id = request.GET.get('device_id')
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')

    cache_key = f"location_points:{device_id}:{start_time}:{end_time}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return JsonResponse(cached_data)

    try:
        location_points = DeviceInfo.objects.filter(
            device_fk_id=device_id,
            time_stamp__gte=start_time,
            time_stamp__lte=end_time
        ).values('latitude', 'longitude', 'time_stamp')
    except DeviceInfo.DoesNotExist:
        return JsonResponse({'message': 'device info not found'}, status=404)

    response_data = list(location_points)
    cache.set(cache_key, response_data)

    return JsonResponse(response_data, safe=False)  

