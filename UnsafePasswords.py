f1 = open('users', 'r')
f2 = open('passwords', 'r')         
users = f1.read()
passwords = f2.read()
f1.close()
f2.close()
Loggeduser = input('Username:  ')
if  Loggeduser in users:
    password = input('password:  ')
    i = (0)
    for u in users:
        if Loggeduser == u:
            break
        i = i + 1
    if passwords[i] == password:
        print ('your logged in')
    else:
        print ('incorrect password')
else:
    print ('Invalid username')


