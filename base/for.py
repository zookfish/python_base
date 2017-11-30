

for i in range(1,5):
    print(i)
else:
    print('The loop is over')

# range 每次只会产生一个数字

print(list(range(1,5,2)))



while True:
    s = input('Enter something : ')
    if s =='quit':
        break
    if len(s) < 3:
        print('to small')
        continue
    print('Input is of sufficient length!')
