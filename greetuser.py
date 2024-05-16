#Define a function greet_user() which should receive the name of the user as an argument like greet_user('dale').

#It should print a message like HEY DALE!.

#Note that the argument can be anything from Dale, dale, etc. but the output should be like HEY DALE! i.e. in all caps! And the names will be given randomly.

def greet_user(user):
    user = user.upper()
    print('HEY ' + user + '!')
    