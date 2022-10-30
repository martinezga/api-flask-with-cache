from models.user_model import UserModel


class UserService:

    def get_all(self):
        users = UserModel.query.all()

        return users
