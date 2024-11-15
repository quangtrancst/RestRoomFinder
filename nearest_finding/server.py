from flask import Flask, request, jsonify
from flask_cors import CORS
try:
    from utils import find_nearby_restrooms
except ImportError:
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from utils import find_nearby_restrooms

app = Flask(__name__)
CORS(app)  # Thêm dòng này để cấu hình CORS

@app.route('/find_nearby_restrooms', methods=['GET'])
def get_nearby_restrooms():
    user_lat = float(request.args.get('lat'))
    user_lon = float(request.args.get('lon'))
    radius = float(request.args.get('radius', 1.0))
    result = find_nearby_restrooms(user_lat, user_lon, radius)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)