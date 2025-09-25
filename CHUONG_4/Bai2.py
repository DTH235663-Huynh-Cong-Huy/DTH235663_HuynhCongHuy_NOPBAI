from random import randrange
while True:
    somay = randrange(1,101)
    solandoan = 0
    win = False
    while solandoan < 7:
        solandoan+=1
        songuoi = int (input("máy đoán [1...100], mời bạn đoán"))
        print("bạn đoán lần thứ ",solandoan)
        if somay == songuoi:
            print("chúc mừng bạn đoán đúng, số máy là=",somay)
            win = True
            break
        if somay >songuoi:
            print("Bạn đoán sai, số máy > số bạn")
        elif somay < songuoi:
            print("Bạn đoán sai, số máy < số bạn")
    if win == False:
        print("Game over!, số máy =",somay)
    hoi = input("Tiếp Không?")
    if hoi == "k":
        break
print("Cám ơn bạn đã chơi game!")