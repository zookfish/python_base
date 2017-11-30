

number = 23;
guess = int(input('Enter an integer '))

if guess == number:
    print('Conguration,you guess it!')
    print('but you do not win any prizes!')

elif guess < number:
    print('No, it is a little higher than that')

else:
    print('No,it is a little lower than that')

print('Done')



running = True

while running:
    guess = int (input('Enter an another Integer :'))

    if (guess ==number ):
        print('Congratulations, you guess it again!')

        running = False

    elif guess < number:
        print('No, it is a little higher than that!')

    else:
        print('nothing, only you wrong!')


