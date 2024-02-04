from api.v1.views import app_views
from models import storage
from models.state import State
from flask import abort, request, jsonify

@app_views.route("/states", methods=["GET"], strict_slashes=False)
@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def get_states(state_id=None):
    states_list = []
    if state_id is None:
        all_objs = storage.all(State).values()
        states_list = [v.to_dict() for v in all_objs]
        return jsonify(states_list)
    else:
        result = storage.get(State, state_id)
        if result is None:
            abort(404)
        return jsonify(result.to_dict())

@app_views.route("/states/<state_id>", methods=["DELETE"], strict_slashes=False)
def delete_state(state_id):
    obj = storage.get(State, state_id)
    if obj is None:
        abort(404)
    storage.delete(obj)
    storage.save()
    return jsonify({}), 204  # Use 204 No Content for successful DELETE

@app_views.route("/states", methods=["POST"], strict_slashes=False)
def create_state():
    data = request.get_json(force=True)
    if not data or "name" not in data:
        abort(400, "Invalid JSON or missing 'name' field")
    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201

@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state(state_id):
    obj = storage.get(State, state_id)
    if obj is None:
        abort(404)
    data = request.get_json(force=True)
    if not data:
        abort(400, "Invalid JSON")
    obj.name = data.get("name", obj.name)
    obj.save()
    return jsonify(obj.to_dict()), 200
