from flask import Flask, request, jsonify
from flask_cors import CORS
import math
from typing import List, Dict, Tuple

app = Flask(__name__)
CORS(app)  # Thêm dòng này để cấu hình CORS

# Công thức Haversine để tính khoảng cách giữa hai tọa độ (tính bằng km)
def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371  # Radius of the Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# Các vị trí nhà vệ sinh mẫu với tọa độ, địa chỉ và mô tả
restroom_locations = [
    {"lat": 10.775, "lon": 106.700, "address": "123 A St", "description": "Clean and spacious"},
    {"lat": 10.776, "lon": 106.701, "address": "456 B St", "description": "Recently renovated"},
    {"lat": 10.774, "lon": 106.702, "address": "789 C St", "description": "Wheelchair accessible"},
    {"lat": 10.773, "lon": 106.703, "address": "101 D St", "description": "Family-friendly"},
    {"lat": 10.778, "lon": 106.704, "address": "202 E St", "description": "Well-maintained"},
    {"lat": 10.779, "lon": 106.705, "address": "303 F St", "description": "Open 24/7"},
    {"lat": 10.772, "lon": 106.706, "address": "404 G St", "description": "Close to shopping areas"},
    {"lat": 10.771, "lon": 106.707, "address": "505 H St", "description": "Child-friendly"},
    {"lat": 10.780, "lon": 106.708, "address": "606 I St", "description": "Includes hand sanitizers"},
    {"lat": 10.781, "lon": 106.709, "address": "707 J St", "description": "Good for quick stops"},
]

# Hàm tìm nhà vệ sinh gần trong bán kính cho trước (tính bằng km)
def find_nearby_restrooms(user_lat: float, user_lon: float, radius: float = 1.0) -> List[Dict[str, Tuple]]:
    nearby_restrooms = []
    for restroom in restroom_locations:
        distance = haversine(user_lat, user_lon, restroom["lat"], restroom["lon"])
        print(f"Distance to {restroom['address']}: {distance} km")  # Log khoảng cách
        if distance <= radius:
            restroom_info = {
                "coordinates": (restroom["lat"], restroom["lon"]),
                "address": restroom["address"],
                "description": restroom["description"],
                "distance_km": round(distance, 2)
            }
            nearby_restrooms.append(restroom_info)
    print(f"Nearby restrooms: {nearby_restrooms}")  # Log các nhà vệ sinh gần
    return nearby_restrooms

@app.route('/find_nearby_restrooms', methods=['GET'])
def get_nearby_restrooms():
    user_lat = float(request.args.get('lat'))
    user_lon = float(request.args.get('lon'))
    radius = float(request.args.get('radius', 1.0))
    result = find_nearby_restrooms(user_lat, user_lon, radius)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)