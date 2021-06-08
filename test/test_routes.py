def test_get_all_planets(client):
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_single_planet(client,add_two_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "color": "ice blue",
        "name": "venus",
        "description": "Planet of love"
    }

def test_get_no_planet_return_404(client):
    response = client.get("/planets/55")

     # Assert
    assert response.status_code == 404
    assert response.get_data(as_text= True) == "Planet not found"
   
def test_return_valid_data_for_all_planet(client,add_two_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "id":1,
        "color": "ice blue",
        "name": "venus",
        "description": "Planet of love"
    },
    {
        "id":2,
        "color": "aquamarine marine",
        "name": "neptune",
        "description": "Big love more"
    }]

def test_add_a_planet(client):

    planet_info={
        "color": "brown",
        "name": "Uranus",
        "description": "Crappy time"
    }
    response=client.post("/planets",json=planet_info)

    assert response.status_code == 201
