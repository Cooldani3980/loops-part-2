for i in range(0,1001):
    if i % 3==0:
        print('Fuzz')
    elif i %5==0:
        print('Buzz')
    elif i %3==0 and i%5==0:
        print('FuzzBuzz')