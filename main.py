from flask import Flask, jsonify

app = Flask(__name__)
# app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>'

@app.route('/connect/<configKey>', methods=['Get'])
def connect(configKey):
    # write_data.py
    data_to_write = "Hello, this data will be stored in a volume!"

    with open("/data/python-app/data.txt", "w") as file:
        file.write(data_to_write)

    return jsonify({'result':f'The config value from source call is {configKey}.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Make the app accessible from outside the container