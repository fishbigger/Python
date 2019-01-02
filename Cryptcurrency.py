while True:
    whofrom = input('Who from')
    amount = input('How much?')
    whoto = input('to')
    netPeople = ['bob', 'alice' ,'eve']
    netBalances = [100, 100, 100]
    for i in range (len(netPeople)):
        if whofrom == netPeople[i]:
            index = i
            break
    if whoto and whofrom in netPeople:
        if int(netBalances[index]) >= int(amount):
            print('Sending {}?cryptocurrency? to {}...'.format(amount, whoto))
            print('')
            netBalances[index] = int(netBalances[index]) + int(amount)
            netBalances[index] = (int(netBalances[index]) - int(amount))
            print(netBalances)
        else:
            print('{} doesnt have enough money for that transaction'.format(whofrom))
    elif whoto in netPeople:
        print('{} is not on the network'.format(whoto))
        print('')
        
    else:
        print('{} is not on the network'.format(whofrom))
        print('')

