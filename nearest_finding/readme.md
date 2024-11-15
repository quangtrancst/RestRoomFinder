# Nearest Restrooms Finder

Dự án này giúp bạn tìm kiếm các nhà vệ sinh công cộng gần nhất xung quanh vị trí của bạn. Dự án bao gồm các tệp sau:

- `utils.py`: Chứa các hàm hỗ trợ, bao gồm hàm tính khoảng cách giữa hai tọa độ và hàm tạo các điểm ngẫu nhiên.
- `server.py`: Chứa mã nguồn của server Flask để xử lý các yêu cầu từ client và trả về danh sách các nhà vệ sinh gần nhất.
- `index.html`: Tệp HTML để hiển thị bản đồ và các nút chức năng.
- `script.js`: Chứa mã JavaScript để tương tác với bản đồ và gửi yêu cầu đến server.

## Hướng dẫn sử dụng

### Bước 1: Thực thi `server.py`

1. Đảm bảo rằng bạn đã cài đặt Python và các thư viện cần thiết:

   ```sh
   pip install flask flask-cors
   ```

2. Chạy server Flask:

   ```sh
   python server.py
   ```

3. Server sẽ chạy trên `http://127.0.0.1:5000`.

### Bước 2: Thực thi `index.html`

1. Mở tệp `index.html` trong trình duyệt của bạn.

### Các tính năng của dự án

- **Bản đồ**: Hiển thị vị trí hiện tại của bạn và các nhà vệ sinh công cộng gần nhất.
- **Nút "Tìm kiếm"**: Gửi yêu cầu đến server để tìm kiếm các nhà vệ sinh công cộng trong phạm vi 2km xung quanh vị trí của bạn.
- **Nút "Vị trí hiện tại"**: Lấy vị trí hiện tại của bạn dựa trên định vị từ thiết bị của bạn và cập nhật bản đồ.

### Mô tả chi tiết các tệp

#### `utils.py`

- Chứa các hàm hỗ trợ:
  - `haversine(lat1, lon1, lat2, lon2)`: Tính khoảng cách giữa hai tọa độ.
  - `generate_random_points(center_lat, center_lon, num_points, radius)`: Tạo các điểm ngẫu nhiên quanh một tọa độ trung tâm.
  - `find_nearby_restrooms(user_lat, user_lon, radius)`: Tìm các nhà vệ sinh gần nhất trong phạm vi cho trước.

#### `server.py`

- Chứa mã nguồn của server Flask để xử lý các yêu cầu từ client và trả về danh sách các nhà vệ sinh gần nhất.
- Định nghĩa endpoint `/find_nearby_restrooms` để nhận yêu cầu GET với các tham số `lat`, `lon`, và `radius`.

#### `index.html`

- Tệp HTML để hiển thị bản đồ và các nút chức năng.
- Bao gồm các thẻ `<button>` để tìm kiếm và lấy vị trí hiện tại.

#### `script.js`

- Chứa mã JavaScript để tương tác với bản đồ và gửi yêu cầu đến server.
- Sử dụng thư viện Leaflet để hiển thị bản đồ và các marker.
- Xử lý sự kiện khi nhấn các nút "Tìm kiếm" và "Vị trí hiện tại".

### Hướng dẫn chi tiết

1. **Thực thi `server.py`**:

   - Mở terminal và điều hướng đến thư mục chứa tệp `server.py`.
   - Chạy lệnh `python server.py` để khởi động server Flask.
   - Server sẽ chạy trên `http://127.0.0.1:5000`.

2. **Thực thi `index.html`**:

   - Mở tệp `index.html` trong trình duyệt của bạn.
   - Bản đồ sẽ hiển thị vị trí hiện tại của bạn và các nhà vệ sinh công cộng gần nhất.

3. **Sử dụng các nút chức năng**:
   - **Nút "Tìm kiếm"**: Nhấn vào nút này để gửi yêu cầu đến server và tìm kiếm các nhà vệ sinh công cộng trong phạm vi 2km xung quanh vị trí của bạn.
   - **Nút "Vị trí hiện tại"**: Nhấn vào nút này để lấy vị trí hiện tại của bạn dựa trên định vị từ thiết bị của bạn và cập nhật bản đồ.

Chúc bạn thành công với dự án Nearest Restrooms Finder!
