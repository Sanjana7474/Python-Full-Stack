moves=15
winning_point=int(input("Tell me how me moves is required: "))
while moves>=1:
    if 15-winning_point==moves:
        print("you won the game")
        break
    print(f"{moves} are left")
    moves-=1
else:
    print("Game over")
