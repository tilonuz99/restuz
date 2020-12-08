from flask import Flask, request, jsonify
from geopy import Nominatim
import requests
import warnings
app = Flask(__name__)
def point_to_adress(lon, lat):
    return Nominatim(user_agent='Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHT').reverse(str(lat) + ', ' +str(lon), language='uz').raw['address']

@app.route('/get', methods=['GET'])
def respond():
    lat = request.args.get("lat", None)
    long = request.args.get("long",None)
    if lat and long:
    	return jsonify(point_to_adress(long, lat))
    
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
