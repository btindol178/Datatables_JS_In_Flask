from flask import *

from flask import jsonify

app = Flask(__name__)

@app.route('/page_test')                                                                                  
def page_test():
    #meas = [{"MeanCurrent": 0.05933, "Temperature": 15.095, "YawAngle": 0.0, "MeanVoltage": 0.67367, "VoltageDC": 3.18309, "PowerSec": 0.06923, "FurlingAngle": -0.2266828184, "WindSpeed": 1.884, "VapourPressure": 1649.25948, "Humidity": 0.4266, "WindSector": 0, "AirDensity": 1.23051, "BarPressure": 1020.259, "time": "2015-04-22 20:58:28", "RPM": 0.0, "ID": 1357}]
    meas = {"MeanCurrent": 0.05933, "Temperature": 15.095, "YawAngle": 0.0, "MeanVoltage": 0.67367, "VoltageDC": 3.18309, "PowerSec": 0.06923, "FurlingAngle": -0.2266828184, "WindSpeed": 1.884, "VapourPressure": 1649.25948, "Humidity": 0.4266, "WindSector": 0, "AirDensity": 1.23051, "BarPressure": 1020.259, "time": "2015-04-22 20:58:28", "RPM": 0.0, "ID": 1357}
    return jsonify(meas)#jsonify({'data': meas})


if __name__ == "__main__":
    app.run(debug=True)