class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 1

    def follow(self, user):
        user.followers += 1
        user.following += 1

user1 = User("001", "Daniel")
# user1.id = "001"
# user1.username = "Daniel"

print(user1.username)
print(user1.followers)

User2 = User("002", "Angela")

User2.follow(user1)

print(user1.followers)