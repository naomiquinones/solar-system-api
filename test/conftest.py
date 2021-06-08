import pytest
from app import create_app
from app import db
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def add_two_planets(app):
    venus = Planet(name="venus",description="Planet of love",color="ice blue")
    neptune = Planet(name="neptune",description="Big love more",color="aquamarine marine")

    db.session.add_all([venus,neptune])
    db.session.commit()
