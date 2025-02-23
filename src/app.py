"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import (
    db,
    User,
    Character,
    Vehicle,
    Planet,
    FavoriteCharacter,
    FavoritePlanet,
    FavoriteVehicle,
)

# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url.replace(
        "postgres://", "postgresql://"
    )
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# generate sitemap with all your endpoints
@app.route("/")
def sitemap():
    return generate_sitemap(app)


@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))
    return jsonify(all_users), 200


@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    if user == None:
        raise APIException("User Not Found", status_code=404)
    return jsonify(user.serialize()), 200


@app.route("/users", methods=["POST"])
def create_user():
    request_body_user = request.get_json()
    user1 = User(
        email=request_body_user["email"],
        password=request_body_user["password"],
        is_active=request_body_user["is_active"],
    )
    db.session.add(user1)
    db.session.commit()
    return jsonify({"message": "User has been created"}), 200


@app.route("/people", methods=["GET"])
def get_characters():
    characters = Character.query.all()
    all_characters = list(map(lambda x: x.serialize(), characters))
    return jsonify(all_characters), 200


@app.route("/people/<int:id>", methods=["GET"])
def get_character(id):
    character = Character.query.get(id)
    if character == None:
        raise APIException("Character Not Found", status_code=404)
    return jsonify(character.serialize()), 200


@app.route("/people", methods=["POST"])
def create_character():
    request_body_character = request.get_json()
    character1 = Character(
        name=request_body_character["name"],
        url=request_body_character["url"],
        height=request_body_character["height"],
        mass=request_body_character["mass"],
        hair_color=request_body_character["hair_color"],
        skin_color=request_body_character["skin_color"],
        eye_color=request_body_character["eye_color"],
        birth_year=request_body_character["birth_year"],
        gender=request_body_character["gender"],
        homeworld=request_body_character["homeworld"],
        created=request_body_character["created"],
        edited=request_body_character["edited"],
        img=request_body_character["img"],
    )
    db.session.add(character1)
    db.session.commit()
    return jsonify({"message": "Character has been created"}), 200


@app.route("/vehicles", methods=["GET"])
def get_vehicles():
    vehicles = Vehicle.query.all()
    all_vehicles = list(map(lambda x: x.serialize(), vehicles))
    return jsonify(all_vehicles), 200


@app.route("/vehicles", methods=["POST"])
def create_vehicles():
    request_body_vehicle = request.get_json()
    vehicle1 = Vehicle(
        name=request_body_vehicle["name"],
        url=request_body_vehicle["url"],
        model=request_body_vehicle["model"],
        vehicle_class=request_body_vehicle["vehicle_class"],
        manufacturer=request_body_vehicle["manufacturer"],
        cost_in_credits=request_body_vehicle["cost_in_credits"],
        length=request_body_vehicle["length"],
        crew=request_body_vehicle["crew"],
        passengers=request_body_vehicle["passengers"],
        max_atmosphering_speed=request_body_vehicle["max_atmosphering_speed"],
        cargo_capacity=request_body_vehicle["cargo_capacity"],
        consumables=request_body_vehicle["consumables"],
        created=request_body_vehicle["created"],
        edited=request_body_vehicle["edited"],
        img=request_body_vehicle["img"],
    )
    db.session.add(vehicle1)
    db.session.commit()
    return jsonify({"message": "Vehicle has been created"}), 200


@app.route("/vehicles/<int:id>", methods=["GET"])
def get_vehicle(id):
    vehicle = Vehicle.query.get(id)
    if vehicle == None:
        raise APIException("Vehicle Not Found", status_code=404)
    return jsonify(vehicle.serialize()), 200


@app.route("/planets", methods=["GET"])
def get_planets():
    planets = Planet.query.all()
    all_planets = list(map(lambda x: x.serialize(), planets))
    return jsonify(all_planets), 200


@app.route("/planets", methods=["POST"])
def create_planets():
    request_body_planet = request.get_json()
    planet1 = Planet(
        name=request_body_planet["name"],
        url=request_body_planet["url"],
        diameter=request_body_planet["diameter"],
        rotation_period=request_body_planet["rotation_period"],
        orbital_period=request_body_planet["orbital_period"],
        gravity=request_body_planet["gravity"],
        population=request_body_planet["population"],
        climate=request_body_planet["climate"],
        terrain=request_body_planet["terrain"],
        surface_water=request_body_planet["surface_water"],
        created=request_body_planet["created"],
        edited=request_body_planet["edited"],
        img=request_body_planet["img"],
    )
    db.session.add(planet1)
    db.session.commit()
    return jsonify({"message": "Planet has been created"}), 200


@app.route("/planets/<int:id>", methods=["GET"])
def get_planet(id):
    planet = Planet.query.get(id)
    if planet == None:
        raise APIException("Planet Not Found", status_code=404)
    return jsonify(planet.serialize()), 200


@app.route("/favorite/people", methods=["GET"])
def get_favoritesCharacters():
    favorites_characters = FavoriteCharacter.query.all()
    all_favorites_characters = list(map(lambda x: x.serialize(), favorites_characters))
    return jsonify(all_favorites_characters), 200


@app.route("/favorite/people/<int:user_id>", methods=["GET"])
def get_favoriteUserCharacters(user_id):
    favorites_characters = FavoriteCharacter.query.all()
    all_favorites_characters = list(map(lambda x: x.serialize(), favorites_characters))
    all_favorites_characters = [
        favorite_character
        for favorite_character in all_favorites_characters
        if favorite_character["user_id"] == user_id
    ]
    return jsonify(all_favorites_characters), 200

@app.route("/favorite/people", methods=["POST"])
def create_favorite_character():
    request_body_character = request.get_json()
    favorite_character1 = FavoriteCharacter(
        user_id=request_body_character["user_id"],
        character_id=request_body_character["character_id"],
    )
    db.session.add( favorite_character1)
    db.session.commit()
    return jsonify({"message": "Favorite character has been added"}), 200

@app.route("/favorite/people/<int:favorite_id>", methods=["DELETE"])
def delete_favoriteCharacter(favorite_id):
    favorite_character = FavoriteCharacter.query.get(favorite_id)
    if favorite_character == None:
        raise APIException("Favorite Not Found", status_code=404)
    db.session.delete(favorite_character)
    db.session.commit()
    return jsonify({"message" : "Favorite deleted"}), 200

@app.route("/favorite/vehicles", methods=["GET"])
def get_favoritesVehicles():
    favorites_vehicles = FavoriteVehicle.query.all()
    all_favorites_vehicles = list(map(lambda x: x.serialize(), favorites_vehicles))
    return jsonify(all_favorites_vehicles), 200

@app.route("/favorite/vehicles/<int:user_id>", methods=["GET"])
def get_favoriteUserVehicles(user_id):
    favorites_vehicles = FavoriteVehicle.query.all()
    all_favorites_vehicles = list(map(lambda x: x.serialize(), favorites_vehicles))
    all_favorites_vehicles = [
        favorite_vehicle
        for favorite_vehicle in all_favorites_vehicles
        if favorite_vehicle["user_id"] == user_id
    ]
    return jsonify(all_favorites_vehicles), 200

@app.route("/favorite/vehicles", methods=["POST"])
def create_favorite_vehicle():
    request_body_vehicle = request.get_json()
    favorite_vehicle1 = FavoriteVehicle(
        user_id=request_body_vehicle["user_id"],
        vehicle_id=request_body_vehicle["vehicle_id"],
    )
    db.session.add( favorite_vehicle1)
    db.session.commit()
    return jsonify({"message": "Favorite vehicle has been added"}), 200

@app.route("/favorite/vehicles/<int:favorite_id>", methods=["DELETE"])
def delete_favoriteVehicle(favorite_id):
    favorite_vehicle = FavoriteVehicle.query.get(favorite_id)
    if favorite_vehicle == None:
        raise APIException("Favorite Not Found", status_code=404)
    db.session.delete(favorite_vehicle)
    db.session.commit()
    return jsonify({"message" : "Favorite deleted"}), 200

@app.route("/favorite/planets", methods=["GET"])
def get_favoritesPlanets():
    favorites_planets = FavoritePlanet.query.all()
    all_favorites_planets = list(map(lambda x: x.serialize(), favorites_planets))
    return jsonify(all_favorites_planets), 200


@app.route("/favorite/planets/<int:user_id>", methods=["GET"])
def get_favoriteUserPlanets(user_id):
    favorites_planets = FavoritePlanet.query.all()
    all_favorites_planets = list(map(lambda x: x.serialize(), favorites_planets))
    all_favorites_planets = [
        favorite_planet
        for favorite_planet in all_favorites_planets
        if favorite_planet["user_id"] == user_id
    ]
    return jsonify(all_favorites_planets), 200

@app.route("/favorite/planets", methods=["POST"])
def create_favorite_planet():
    request_body_planet = request.get_json()
    favorite_planet1 = FavoritePlanet(
        user_id=request_body_planet["user_id"],
        planet_id=request_body_planet["planet_id"],
    )
    db.session.add( favorite_planet1)
    db.session.commit()
    return jsonify({"message": "Favorite planet has been added"}), 200

@app.route("/favorite/planets/<int:favorite_id>", methods=["DELETE"])
def delete_favoritePlanet(favorite_id):
    favorite_planet = FavoritePlanet.query.get(favorite_id)
    if favorite_planet == None:
        raise APIException("Favorite Not Found", status_code=404)
    db.session.delete(favorite_planet)
    db.session.commit()
    return jsonify({"message" : "Favorite deleted"}), 200

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=PORT, debug=False)
