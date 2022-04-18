from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/health',methods=['GET'])
def index():
    return jsonify({'STATUS':'UP'})
@app.route('/alert', methods=['POST'])
def create_alert():
    request_data = request.get_json()

    externalURL = None
    alertsLength = None

    if request_data:
        if 'externalURL' in request_data:
            externalURL = request_data['externalURL']

        if 'alerts' in request_data:
            alertsLength = len(request_data['alerts'])
            print(alertsLength)

    return '''
           The language value is: {}
           The boolean value is: {}'''.format(externalURL, alertsLength)
app.run(debug=True, port=5000)
