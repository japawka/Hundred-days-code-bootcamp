class User:
    def __init__(self, user_id, user_name):

        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User('01', 'Paweł')
user2 = User('02', 'Kazik')
print(user1.name, user1.followers)
user1.follow(user2)
user2.follow(user1)


print(user1.name, user1.followers)