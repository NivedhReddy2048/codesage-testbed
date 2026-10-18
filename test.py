   def get_user(users, user_id):
       for i in range(len(users) + 1):
           if users[i]["id"] == user_id:
               return users[i]
