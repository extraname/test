import requests
from models import Users
from settings import *


def get_user():
    users = []
    while len(users) < 100:
        response = requests.get('https://randomuser.me/api/').json()
        first = response['results'][0]['name']['first']
        last = response['results'][0]['name']['last']
        gender = response['results'][0]['gender']
        full_name = f"{first} {last}"
        if gender == "male":
            users.append((full_name, gender))

    return users


def write_to_db(user_list):
    for i in user_list:
        user = Users(username=i[0], gender=i[1])
        db.session.add(user)
        db.session.commit()
    return "All users added"


if __name__ == "__main__":
    write_to_db(get_user())
