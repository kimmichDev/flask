from app.models.user import db, User


def getUsers() -> list:
    users = User.query.all()
    print(type(users))
    return users


def create(data: dict) -> User:
    newUser = User(username=data['username'], email=data['email'])
    db.session.add(newUser)
    db.session.commit()
    return newUser


def getUser(id: int) -> User:
    user = User.query.filter(User.id == id).first_or_404(
        description='ma twae boo')
    return user
