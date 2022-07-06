import random
choice = input(print('Do you want to start the game? yes/no'))
countp1 = 0
counta1 = 0
if choice == 'yes':
    print('The game starts now')
    while countp1 < 2 or counta1 < 2:
        options = ['rock', 'paper', 'scissors']
        p1 = input(print('What are you choosing? rock / paper / scissors'))
        a1 = random.choice(options)
        print(a1)
        if a1==p1:
            print('remis')
        elif a1 != p1:
            if a1 == "rock" and p1 == "paper":
                countp1 += 1
                print("Paper wins p1=", countp1)
            elif a1 == "rock" and p1 == "scissors":
                counta1 += 1
                print("rock wins a1=", counta1)
            elif a1 == "scissors" and p1 == "paper":
                counta1 += 1
                print("scissors wins a1=", counta1)
            elif a1 == "scissors" and p1 == "rock":
                countp1 += 1
                print("rock wins p1=", countp1)
            elif a1 == "paper" and p1 == "scissors":
                countp1 += 1
                print("scissors wins p1=", countp1)
            elif a1 == "paper" and p1 == "rock":
                counta1 += 1
                print("paper wins a1=", counta1)
                if counta1 == 2:
                    print("a1 wygral")
                    break
                elif countp1 == 2:
                    print("p1 wygral")
                    break
        
            
                
                
                
    
    
    