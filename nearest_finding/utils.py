import math
import random
from typing import List, Dict, Tuple

# Công thức Haversine để tính khoảng cách giữa hai tọa độ (tính bằng km)
def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371  # Radius of the Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# Hàm tạo các điểm ngẫu nhiên quanh một tọa độ trung tâm
def generate_random_points(center_lat: float, center_lon: float, num_points: int, radius: float) -> List[Dict[str, float]]:
    points = []
    for _ in range(num_points):
        # Tạo ngẫu nhiên một khoảng cách và góc
        distance = random.uniform(0, radius)
        angle = random.uniform(0, 2 * math.pi)
        
        # Tính toán tọa độ mới
        delta_lat = distance / 111  # 1 độ vĩ tuyến ~ 111 km
        delta_lon = distance / (111 * math.cos(math.radians(center_lat)))
        
        new_lat = center_lat + (distance / 111) * math.cos(angle)
        new_lon = center_lon + (distance / (111 * math.cos(math.radians(center_lat)))) * math.sin(angle)
        
        points.append({
            "lat": new_lat,
            "lon": new_lon,
            "address": f"Random Address {len(points) + 1}",
            "description": "Randomly generated restroom"
        })
    return points

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

# Thêm các điểm ngẫu nhiên quanh các quận Bình Tân, Bình Thạnh và Thủ Đức
binh_tan_points = generate_random_points(10.762622, 106.656123, 3, 5)  # 5 km radius
binh_thanh_points = generate_random_points(10.8142, 106.7070, 10, 5)  # 5 km radius
thu_duc_points = generate_random_points(10.8491, 106.7537, 15, 5)  # 5 km radius

restroom_locations.extend(binh_tan_points)
restroom_locations.extend(binh_thanh_points)
restroom_locations.extend(thu_duc_points)

# Hàm tìm nhà vệ sinh gần trong bán kính cho trước (tính bằng km)
def find_nearby_restrooms(user_lat: float, user_lon: float, radius: float = 2.0) -> List[Dict[str, Tuple]]:
    nearby_restrooms = []
    for restroom in restroom_locations:
        distance = haversine(user_lat, user_lon, restroom["lat"], restroom["lon"])
        if distance <= radius:
            restroom_info = {
                "coordinates": (restroom["lat"], restroom["lon"]),
                "address": restroom["address"],
                "description": restroom["description"],
                "distance_km": round(distance, 2)
            }
            nearby_restrooms.append(restroom_info)
    
    # Sắp xếp các điểm theo khoảng cách
    nearby_restrooms.sort(key=lambda x: x["distance_km"])
    
    if not nearby_restrooms:
        print("Bạn đang quá xa với các nhà vệ sinh công cộng.")
    else:
        print("Nearby restrooms:")
        for restroom in nearby_restrooms:
            print(f"- {restroom['address']} ({restroom['distance_km']} km): {restroom['description']}")
    
    return nearby_restrooms