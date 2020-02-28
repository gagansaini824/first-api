from werkzeug.security import safe_str_cmp
from user import User

#users = [
#         User(1, 'jose', 'asdf'),
#         User(2, 'asd', 'asdf'),
#         User(3, 'fgd', 'asdf'),
#         User(4, 'dgfs', 'asdf')
#        ]
#
#
#username_mapping= {u.username: u for u in users}
#userid_mapping= {u.id: u for u in users}


def authenticate(username = 'bob', password = 'asdf'):
    user = User.find_by_username.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user
    
def identity(payload):
    user_id = payload['identity']
    return User.find_by_id.get(user_id, None)
    
    