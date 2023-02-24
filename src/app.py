"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure(
    "Jackson", [{"first_name": "John", "age": 33, "lucky_numbers": [7, 13, 22]},
    {"first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3]},
    {"first_name": "Jimmy", "age": 5, "lucky_numbers": 1}])

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints

@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    if not members:
        # Si la lista de miembros está vacía, devolver 404
        return jsonify({"error": "No se encontraron miembros"}), 404

    # Devolver la lista de miembros como objeto JSON con código de estado 200
    return jsonify({"family": members}), 200


@app.route('/members/<int:id>', methods=['GET'])
def get_member_by_id(id):
    member = jackson_family.get_member(id)
    if not member:
        # Si no se encontró el miembro con el ID proporcionado, devolver 404
        return jsonify({"error": "Miembro no encontrado"}), 404

    # Devolver el miembro como objeto JSON con código de estado 200
    return jsonify(member), 200

@app.route('/members', methods=['POST'])
def add_member():
    new_member = request.get_json()
    jackson_family.add_member(new_member)
    response_body = {
        "msg": "Miembro agregado exitosamente",
        "family": jackson_family.get_all_members()
    }
    return jsonify(response_body), 200


@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    deleted = jackson_family.delete_member(id)
    if not deleted:
        # Si el miembro no se pudo eliminar, devolver 404
        return jsonify({"error": "Miembro no encontrado"}), 404

    # Devolver una respuesta de éxito si se eliminó el miembro
    return jsonify({"done": True}), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
