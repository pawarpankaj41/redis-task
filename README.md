# redis-task
Redis Task Assignment


This is the Assignment Task.

**Endpoint 1: /base/location_points/**

#### CURL 1

```
curl  -X GET \
  'https://redis-task.vercel.app/base/location_points/?device_id=25029&start_time=2021-04-08T07%3A30%3A10Z&end_time=2022-04-08T07%3A30%3A10Z' \
  --header 'Accept: */*' \
  --header 'User-Agent: Thunder Client (https://www.thunderclient.com)'
```

##### Request

**HTTP Method**: GET

**Endpoint**: `https://redis-task.vercel.app/base/location_points/`

**Parameters**:
- `device_id`: (integer) The ID of the device. Example: 25029
- `start_time`: (string, optional) The start time for the location data. Example: "2023-07-01T00:00:00Z"
- `end_time`: (string, optional) The end time for the location data. Example: "2023-07-15T23:59:59Z"




**Endpoint 2: /base/latest_info/**


### CURL 2


```
curl -X GET \
  'https://redis-task.vercel.app/base/latest_info/?device_id=25029' \
  --header 'Accept: */*' \
  --header 'User-Agent: Thunder Client (https://www.thunderclient.com)'
```

##### Request

**HTTP Method**: GET

**Endpoint**: `https://redis-task.vercel.app/base/latest_info/`

**Parameters**:
- `device_id`: (integer) The ID of the device. Example: 25029




**Endpoint 3: /base/start_end_location/**


### CURL 3


#### CURL 3

```
curl -X GET \
  'https://redis-task.vercel.app/base/start_end_location/?device_id=25029' \
  --header 'Accept: */*' \
  --header 'User-Agent: Thunder Client (https://www.thunderclient.com)'
```

##### Request

**HTTP Method**: GET

**Endpoint**: `https://redis-task.vercel.app/base/start_end_location/`

**Parameters**:
- `device_id`: (integer) The ID of the device. Example: 25029


