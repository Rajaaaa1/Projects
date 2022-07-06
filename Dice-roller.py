import random
#dice roller
print('Gra w której zostanie wylosowana kość')
while True:
    print(random.randrange(1,6))
    wybor = input(print('Chcesz kontynuowac gre? tak/nie '))
    if wybor == "nie":
        break
