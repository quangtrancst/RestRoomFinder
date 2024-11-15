let map;
let userMarker;
let userLocation = [10.775, 106.7]; // Vị trí mặc định
let restroomMarkers = [];

// Kiểm tra xem trình duyệt có hỗ trợ Geolocation API không
if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(
    function (position) {
      userLocation = [position.coords.latitude, position.coords.longitude];
      initializeMap(userLocation);
    },
    function (error) {
      console.error("Error getting location: ", error);
      initializeMap(userLocation);
    }
  );
} else {
  console.error("Geolocation is not supported by this browser.");
  initializeMap(userLocation);
}

function initializeMap(location) {
  map = L.map("map").setView(location, 15);

  // Sử dụng tile miễn phí của OpenStreetMap
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 18,
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

  // Thêm marker cho vị trí người dùng
  userMarker = L.marker(location, { color: "red" })
    .addTo(map)
    .bindPopup("<b>Your Location</b>")
    .openPopup();

  // Cập nhật vị trí người dùng khi nhấp vào bản đồ
  map.on("click", function (e) {
    if (userMarker) {
      map.removeLayer(userMarker);
    }
    userMarker = L.marker(e.latlng, { color: "red" })
      .addTo(map)
      .bindPopup("<b>Your Location</b>")
      .openPopup();
    userLocation = [e.latlng.lat, e.latlng.lng];
  });

  // Xử lý sự kiện khi nhấn nút tìm kiếm
  document.getElementById("searchButton").addEventListener("click", function () {
    // Xóa các marker cũ
    restroomMarkers.forEach((marker) => map.removeLayer(marker));
    restroomMarkers = [];

    // Gửi yêu cầu đến API để tìm nhà vệ sinh gần nhất
    fetch(
      `http://localhost:5000/find_nearby_restrooms?lat=${userLocation[0]}&lon=${userLocation[1]}&radius=2.0`
    )
      .then((response) => response.json())
      .then((data) => {
        console.log(data); // Log dữ liệu trả về từ API
        data.forEach((restroom) => {
          const marker = L.marker([
            restroom.coordinates[0],
            restroom.coordinates[1],
          ])
            .addTo(map)
            .bindPopup(
              `<b>${restroom.address}</b><br>${
                restroom.description
              }<br>Distance: ${restroom.distance_km.toFixed(2)} km`
            );
          restroomMarkers.push(marker);
        });
      })
      .catch((error) => console.error("Error:", error));
  });

  // Xử lý sự kiện khi nhấn nút vị trí hiện tại
  document.getElementById("locateButton").addEventListener("click", function () {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        function (position) {
          userLocation = [position.coords.latitude, position.coords.longitude];
          map.setView(userLocation, 15);
          if (userMarker) {
            map.removeLayer(userMarker);
          }
          userMarker = L.marker(userLocation, { color: "red" })
            .addTo(map)
            .bindPopup("<b>Your Location</b>")
            .openPopup();
        },
        function (error) {
          console.error("Error getting location: ", error);
        }
      );
    } else {
      console.error("Geolocation is not supported by this browser.");
    }
  });
}