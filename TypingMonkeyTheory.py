string = ('')
from random import*
import time
word_to_find = input('word to find?')
times = []
for p in range (10):
    start = time.clock()
    try:
        string = ''
        while not string == word_to_find:
            string = ''
            for i in range (len(word_to_find)):
                string = str(string) + str(chr(randint(97, 122)))
    except Exception as inst:
        print('Stoped because of hi'  + inst)
    finally:
        end = time.clock()
        print('Trying to find: {0}'.format(word_to_find))
        print('Last found string: {0}'.format(string)) 
        print('Time taken: {:0.5f} seconds\n'.format(end - start))
        times.append(end - start)
mean = 1
for time in times:
    mean = mean + time
mean = mean / len(times)
print('\nhMean time: {:0.5} seconds'.format(mean))
    
    
        
