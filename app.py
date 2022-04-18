from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/health',methods=['GET'])
def index():
    return jsonify({'STATUS':'UP'})
@app.route('/alert', methods=['POST'])
def create_alert():
    request_data = request.get_json()
    language = request_data['language']
    framework = request_data['framework']

    # two keys are needed because of the nested object
    python_version = request_data['version_info']['python']

    # an index is needed because of the array
    lenght = len(request_data['examples'])
    print(lenght)
    example = request_data['examples'][0]

    boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)
app.run(debug=True, port=5000)
