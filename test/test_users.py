from fastapi import status
from routers.user import get_db, get_current_user
from main import app
from models import Todos
from .utils import *

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/user/read")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'admin_test'
    assert response.json()['email'] == 'admin@gmail.com'
    assert response.json()['first_name'] == 'Kasim'
    assert response.json()['last_name'] == 'Jabrayilov'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '0123456789'





def test_change_password(test_user):
    response = client.put("/user/password", json={'password': 'admin_test',
                                                  'new_password': 'admin_test_new'})
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_change_password_invalid_password(test_user):
    response = client.put("/user/password", json={'password': 'admin_test_wrong',
                                                  'new_password': 'admin_test_new'})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'}

def test_phone_number_change(test_user):
    response = client.put("/user/phone_number/0123456789", json={'phone_number': '0123456789'})
    assert response.status_code == status.HTTP_204_NO_CONTENT

