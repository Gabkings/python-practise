class User:
    """docstring for User"""
    active_user = 0
    @classmethod
    def display_active_user(cls):
        return f'there are currently {cls.active_user} active users in our class'
    def __init__(self, first, last):
        self.name = first
        self.name2 = last
        User.active_user += 1
    def full_name(self):
        return f"{self.name} {self.name2}"


user1 = User('Gab', 'Kings')
user2 = User('Gab2', 'Kings')
user3 = User('Gab3', 'Kings')
user4 = User('Gab4', 'Kings')
print(user1.full_name())
print(User.active_user)
print(User.display_active_user())
