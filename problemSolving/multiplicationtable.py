print('MULTIPLICATION TABLE')
num = int(input('Enter a number: '))
limit = int(input('Multiply until: '))

if limit < 0:
    print('error.')
elif limit == 0:
    print('Nothing to multiply')
else:
    for i in range(1, limit+1):
        print(f'{num} x {i} = {num * i}')
