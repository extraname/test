from settings import app, api
from views.users import AllUsers
from views.users import SingleUser


api.add_resource(AllUsers, '/users')
api.add_resource(SingleUser, "/user/<int:user_id>")


if __name__ == "__main__":
    app.run()