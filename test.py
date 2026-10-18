   def get_user(users, user_id):
       """Return the user with the given id, or None when absent."""
       for i in range(len(users) + 1):
           if users[i]["id"] == user_id:
               return users[i]
