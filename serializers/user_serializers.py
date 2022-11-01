from configurations.database import db
from models.user_model import UserModel


class UserSerializer:
    def __init__(self, **data):
        self.data = data.get('data')
        self.has_errors = False
        self.errors = {}
        self.name = self.data.get('name')
        self.lastname = self.data.get('lastname')
        self.email = self.validate_email(self.data.get('email'))

    def validate_email(self, value):
        # Email is required. Return an error if it was not sent
        if not value:
            self.has_errors = True
            self.errors['error'] = 'email field is required'
        else:
            obj = UserModel.query.filter(UserModel.email == value).first()
            if obj:
                self.has_errors = True
                self.errors['error'] = 'Email duplicated'
        return value

    def create(self):
        if not self.has_errors:
            user = UserModel(self.name, self.lastname, self.email)
            db.session.add(user)
            db.session.commit()


class UserListSerializer:
    def __init__(self, values):
        self.values = values
        self.data = self.serialize()

    def serialize(self):
        result = []
        user = {}
        for item in self.values:
            # If UserModel changes add new fields here
            user['id'] = item.id
            user['name'] = item.name
            user['lastname'] = item.lastname
            user['email'] = item.email
            # Append and re-initialize
            result.append(user)
            user = {}

        return result
