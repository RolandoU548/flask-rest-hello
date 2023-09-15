from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    height = db.Column(db.String(50), nullable=False)
    mass = db.Column(db.String(50), nullable=False)
    hair_color = db.Column(db.String(50), nullable=False)
    skin_color = db.Column(db.String(50), nullable=False)
    eye_color = db.Column(db.String(50), nullable=False)
    birth_year = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    homeworld = db.Column(db.String(50), nullable=False)
    created = db.Column(db.String(50), nullable=False)
    edited = db.Column(db.String(50), nullable=False)
    img = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<Character %r>" % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld,
            "created": self.created,
            "edited": self.edited,
            "img": self.img,
            # do not serialize the password, its a security breach
        }


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    vehicle_class = db.Column(db.String(50), nullable=False)
    manufacturer = db.Column(db.String(50), nullable=False)
    cost_in_credits = db.Column(db.String(50), nullable=False)
    length = db.Column(db.String(50), nullable=False)
    crew = db.Column(db.String(50), nullable=False)
    passengers = db.Column(db.String(50), nullable=False)
    max_atmosphering_speed = db.Column(db.String(50), nullable=False)
    cargo_capacity = db.Column(db.String(50), nullable=False)
    consumables = db.Column(db.String(50), nullable=False)
    created = db.Column(db.String(50), nullable=False)
    edited = db.Column(db.String(50), nullable=False)
    img = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<Vehicle %r>" % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "created": self.created,
            "edited": self.edited,
            "img": self.img,
            # do not serialize the password, its a security breach
        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    diameter = db.Column(db.String(50), nullable=False)
    rotation_period = db.Column(db.String(50), nullable=False)
    orbital_period = db.Column(db.String(50), nullable=False)
    gravity = db.Column(db.String(50), nullable=False)
    population = db.Column(db.String(50), nullable=False)
    climate = db.Column(db.String(50), nullable=False)
    terrain = db.Column(db.String(50), nullable=False)
    surface_water = db.Column(db.String(50), nullable=False)
    created = db.Column(db.String(50), nullable=False)
    edited = db.Column(db.String(50), nullable=False)
    img = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<Planet %r>" % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "created": self.created,
            "edited": self.edited,
            "img": self.img,
            # do not serialize the password, its a security breach
        }


class FavoriteCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
    character_id = db.Column(db.Integer(), db.ForeignKey("character.id"))
    user = db.relationship("User")
    character = db.relationship("Character")

    def __repr__(self):
        return "<Favorite %r>" % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            # do not serialize the password, its a security breach
        }


class FavoriteVehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
    vehicle_id = db.Column(db.Integer(), db.ForeignKey("vehicle.id"))
    user = db.relationship("User")
    vehicle = db.relationship("Vehicle")

    def __repr__(self):
        return "<Favorite %r>" % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehicle_id": self.vehicle_id,
            # do not serialize the password, its a security breach
        }


class FavoritePlanet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
    planet_id = db.Column(db.Integer(), db.ForeignKey("planet.id"))
    user = db.relationship("User")
    planet = db.relationship("Planet")

    def __repr__(self):
        return "<Favorite %r>" % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            # do not serialize the password, its a security breach
        }
