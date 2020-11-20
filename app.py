from flask import Flask, request, jsonify
import requests
import warnings
app = Flask(__name__)
def point_to_adress(lon, lat):
    url = "https://nominatim.openstreetmap.org/reverse?format=jsonv2&lon=" + str(lon) + "&lat=" + str(lat)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        r = requests.get(url=url).json()['address']
        return r

@app.route('/get/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    lat = request.args.get("lat", None)
    long = request.args.get("long",None)
    response = {}
    if lat and long:
    	response["city"] = point_to_adress(long, lat)

    # Return the response in json format
    return jsonify(response)
    
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
