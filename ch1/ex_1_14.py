class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def __repr__(self):
        return 'User({}, {})'.format(self.name, self.id)

users = [User("Jill", 45), User("Alex", 3), User("Joe", 7)]

print(sorted(users, key=lambda u: u.id))
from operator import attrgetter
print(sorted(users, key=attrgetter('name')))
