from flask import Flask, jsonify, abort, make_response
from flask import request

gyms = [
    {
        "id": 1,
        "name": "Florian Martial Arts Center",
        "Leader": "Kenny Florian",
        "Location": "Boston"
    },
    {
        "id": 2,
        "name": "Dynamix Martial Arts",
        "Leader": "Other Guy",
        "Location": "Los Angeles"
    }
]

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/lfd/api/v1.0/gyms", methods=['GET'])
def get_gyms():
    return jsonify({'gyms':gyms})

@app.route("/lfd/api/v1.0/gyms", methods=['POST'])
def create_gym():
    if not request.json or not 'name' in request.json:
        abort(400)
    gym = {
        'id': gyms[-1]['id'] + 1,
        'name': request.json['name'],
        'Leader': request.json.get('Leader', ""),
        'Location': request.json.get('Location', "")
    }
    gyms.append(gym)
    return jsonify({'gym': gym}), 201

@app.route("/lfd/api/v1.0/gyms/<int:gym_id>", methods=['GET'])
def get_gym(gym_id):
    gym = [gym for gym in gyms if gym['id'] == gym_id]
    if len(gym) == 0:
        abort(404)
    return jsonify({'gym':gym[0]})

@app.route("/lfd/api/v1.0/gyms/<int:gym_id>", methods=['POST'])
def get_gym(gym_id):
    gym = [gym for gym in gyms if gym['id'] == gym_id]
    if len(gym) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)
    if 'Leader' in request.json and type(request.json['Leader']) is not unicode:
        abort(400)
    if 'Location' in request.json and type(request.json['Location']) is not bool:
        abort(400)
    gym[0]['name'] = request.json.get('name', gym[0]['name'])
    gym[0]['Leader'] = request.json.get('Leader', gym[0]['Leader'])
    gym[0]['Location'] = request.json.get('Location', gym[0]['done'])
    return jsonify({'gym':gym[0]})

@app.route('/lfd/api/v1.0/gyms/<int:gym_id>', methods=['DELETE'])
def delete_gym(gym_id):
    gym = [gym for gym in gyms if gym['id'] == gym_id]
    if len(gym) == 0:
        abort(404)
    gyms.remove(gym[0])
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)



if __name__ == '__main__':
    app.run(debug=True)
