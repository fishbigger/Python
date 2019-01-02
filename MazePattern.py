from random import randint
def random():
    if randint(1,2) == 1:
        return('/')
    else:
        return('\\')
line = ''
for i in range(100):
    line = ''
    for p in range(100):
        line += random()
    print(line)
        

