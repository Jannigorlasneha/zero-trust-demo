# demo backend code for zero trust project

def get_user(username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    execute(query)


