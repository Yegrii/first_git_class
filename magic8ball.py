import random
random_number = random.randint(1, 9)
name = 'Yego'
question = 'Do we need to end it?'
answer = ''

if random_number == 1:
    answer = 'Yes - definitely.'
elif random_number == 2:
    answer = 'It is decidedly so.'
elif random_number == 3:
    answer = 'Without a doubt.'
elif random_number == 4:
    answer = 'Reply hazy, try again.'
elif random_number == 5:
    answer = 'Ask again later.'
elif random_number == 6:
    answer = 'Better not tell you now.'
elif random_number == 7:
    answer = 'My sources say no.'
elif random_number == 8:
    answer = 'Outlook not so good.'
elif random_number == 9:
    answer = 'Very doubtful.'
else:
    print('ERROR')

if random_number == 1:
    print('''
   11111  
     1
     1
     1
     1
     1
   11111''')
elif random_number == 2:
    print('''
    22222
        2
       2
      2
    22222  ''')
elif random_number == 3:
    print('''
    33333
        3
      333
        3
    33333''')
elif random_number == 4:
    print('''
    4   4
    4   4
    44444
        4
        4''')
elif random_number == 5:
    print('''
    55555
    5
    55555
        5
        5
    55555''')
elif random_number == 6:
    print('''
    66666
    6
    66666
    6   6
    66666''')
elif random_number == 7:
    print('''
    77777
       7
      7
      7
      7
       ''')
elif random_number == 8:
    print('''
    88888
    8   8
    88888
    8   8
    88888''')
elif random_number == 9:
    print('''
    99999
    9   9
    99999
        9
        9''')

print(name, 'asks: ', question)
print(answer)