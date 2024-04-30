
pin=1234
acc_num=9385437492
acc_bal=60000.00
print("enter the pin no:")
pinno=int(input())
while True:
    if pin==pinno:
        print("1.Deposit\n2.Withdraw\n3.mini statement\n4.check balance\n5.exit")
        choice=int(input("choose one:"))
        if choice==1:
            print("--------------------------------------")
            deposit_amount=int(input("enter amount: "))
            acc_bal+=deposit_amount
            print("your account balance after deposit:",acc_bal)
            print("--------------------------------------")
        elif choice==2:
            print("--------------------------------------")
            if acc_bal>1000:
                withdraw_amount=int(input("enter withdraw amount:"))
                rem_bal=acc_bal-withdraw_amount
                if rem_bal<1000:
                    print("sorry minimum balance reached")
                else:
                    print("amount sucessfully withdrawn\nThe acc_bal=",rem_bal)
                    acc_bal=rem_bal
            else:
                print("your balance reach the minimum balance")
            print("--------------------------------------")
        elif choice==3:
            print("--------------------------------------")
            print("account number:",acc_num)
            print("account balance:",acc_bal)
            print("--------------------------------------")
        elif choice==4:
            print("--------------------------------------")
            print("account balance:",acc_bal)
            if acc_bal<70000:
                diff =70000-acc_bal
                print(diff,"amount only can be deposit")
            else:
                print("deposit limit reached")
            print("--------------------------------------")
        elif choice==5:
            break
