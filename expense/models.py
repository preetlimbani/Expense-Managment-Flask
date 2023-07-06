from expense import mongo


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        mongo.db.users.insert_one({
            'username': self.username,
            'password': self.password
        })

    def find_by_username(username):
        return mongo.db.users.find_one({'username': username})

    def verify_password(existing_password, password):
        return existing_password == password

class Expense:
    def __init__(self, user_id, amount, title):
        self.user_id = user_id
        self.amount = amount
        self.title = title

    def save(self):
        mongo.db.expenses.insert_one({
            'user_id': self.user_id,
            'amount': self.amount,
            'title': self.title
        })
