
import random
coins = int(input('How many coins '))

counter = 0
counter2 = 0
for el in range (coins):
    el = (random.randint(0,1))
    if el == 0:
        counter += 1
        print(el, counter)
    if el == 1:
        counter2 += 1
        print(el, counter2)

print(f'количество решек  {counter}, количество орлов {counter2}')
print(f'минимальное количество переворотов {min(counter, counter2)}')


