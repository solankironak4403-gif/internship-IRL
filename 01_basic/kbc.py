quetions=[
    
    
    ["which language was use to create fb ?", "python","french","javascript","php","non",4],
    ["which language was use to create fb ?", "python","french","javascript","php","non",4],
    ["which language was use to create fb ?", "python","french","javascript","php","non",4],
    ["which language was use to create fb ?", "python","french","javascript","php","non",4],
    ["which language was use to create fb ?", "python","french","javascript","php","non",4],
    ["which language was use to create fb ?", "python","french","javascript","php","non",4],
    ["which language was use to create fb ?", "python","french","javascript","php","non",4],
    ["which language was use to create fb ?", "python","french","javascript","php","non",4],
    ["which language was use to create fb ?", "python","french","javascript","php","non",4],
    ["which language was use to create fb ?", "python","french","javascript","php","non",4],
    ["which language was use to create fb ?", "python","french","javascript","php","non",4],
    ["which language was use to create fb ?", "python","french","javascript","php","non",4],
    ["which language was use to create fb ?", "python","french","javascript","php","non",4],
    ["which language was use to create fb ?", "python","french","javascript","php","non",4],
    ["which language was use to create fb ?", "python","french","javascript","php","non",4],

]

levels=[1000,2000,3000,4000,5000,10000,20000,30000,40000,80000,160000,320000]
money=0
i=0
for i in range(0,len(quetions)):
    quetion = quetions[i]
    print("quetion Rs. {levels[i]}")
    print(f"a.{quetion[1]}            b.{quetion[2]}")
    print(f"c.{quetion[3]}            d.{quetion[4]}")

    replay=int(input("enter you answer (1-4) or 0 quit "))
    if(replay==0):
        money=levels[i-1]
        break


    if (replay == quetion[-1]):
        print(f"correct answer , you have a won {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
        print("wrong answer !")
        break

print(f"totla amount {money}")