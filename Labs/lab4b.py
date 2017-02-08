def main():
    print("Welcome to SoftwarePirates Inc., payroll manager!")
    name=input("First lets start off with your name: ")
    timeW=int(input("How many months have you worked with this company?: "))
    vacDays=int(input("How many vacations days have you been on this month?: "))
    sales=int(input("In dollar amount how much have you sold this month?: "))
    payroll(name,timeW,vacDays,sales)
def payroll(name,timeW,vacDays,sales):
    base=2000
    total=0
    bonus=0
    deduct=0
    commision=0
    if sales<10000:
        total=base
        if vacDays>3:
            total-=200
            deduct=200
            print("The base salary at SoftwarePirates Inc., is", base)
            print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",sales,"amount of sales, you earned no bonus, and had",deduct,"deducted from your pay due to",vacDays,"days of vacation.")
        else:
            print("The base salary at SoftwarePirates Inc., is", base)
            print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",sales,"amount of sales and earned no bonus.")
    if sales>10000 and sales<=100000:
        commision=sales*.02
        total=base+commision
        if vacDays>3:
            total-=200
            deduct=200
            if deduct==0:
                    print("The base salary at SoftwarePirates Inc., is", base)
                    print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and you earned $",bonus,"as a bonus and $",xbonus,"as an extra bonus thanks to your longeiviety with SoftwarePirates Inc.")
            else:
                if deduct==0:
                    print("The base salary at SoftwarePirates Inc., is", base)
                    print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and you earned $",bonus,"as a bonus")
                else:
                    print("The base salary at SoftwarePirates Inc., is", base)
                    print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and you earned $",bonus,"as a bonus and had $",deduct,"deducted from your pay")
                    
                    
        else:
            if deduct==0:
                print("The base salary at SoftwarePirates Inc., is", base)
                print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and earned no bonus.")
            else:
                print("The base salary at SoftwarePirates Inc., is", base)
                print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and you earned no bonus and had $",deduct,"deducted from your pay")
    if sales>100000 and sales<=500000:
        commision=sales*.15
        total=base+commision
        if vacDays>3:
            total-=200
            deduct=200
        if timeW>3:
            total+=1000
            bonus=1000
            if timeW>60:
                total+=1000
                xbonus=1000
                if deduct==0:
                    print("The base salary at SoftwarePirates Inc., is", base)
                    print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and you earned $",bonus,"as a bonus and $",xbonus,"as an extra bonus thanks to your longeiviety with SoftwarePirates Inc.")
                else:
                    print("The base salary at SoftwarePirates Inc., is", base)
                    print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commisionoff of $",sales,"sales and you earned $",bonus,"as a bonus and $",xbonus,"as an extra bonus thanks to your longeiviety with SoftwarePirates Inc. and had $",deduct,"deducted from your pay")
            else:
                if deduct==0:
                    print("The base salary at SoftwarePirates Inc., is", base)
                    print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and you earned $",bonus,"as a bonus")
                else:
                    print("The base salary at SoftwarePirates Inc., is", base)
                    print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and you earned $",bonus,"as a bonus and had $",deduct,"deducted from your pay")
                    
                    
        else:
            if deduct==0:
                print("The base salary at SoftwarePirates Inc., is", base)
                print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and earned no bonus.")
            else:
                print("The base salary at SoftwarePirates Inc., is", base)
                print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and you earned no bonus and had $",deduct,"deducted from your pay")
    if sales>500000 and sales<=1000000:
        commision=sales*.28
        total=base+commision
        if vacDays>3:
            total-=200
            deduct=200
        if timeW>3:
            total+=5000
            bonus=5000
            if timeW>60:
                total+=1000
                bonus+=1000
                if deduct==0:
                    print("The base salary at SoftwarePirates Inc., is", base)
                    print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and you earned $",bonus,"as a bonus and $",xbonus,"as an extra bonus thanks to your longeiviety with SoftwarePirates Inc.")
                else:
                    print("The base salary at SoftwarePirates Inc., is", base)
                    print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commisionoff of $",sales,"sales and you earned $",bonus,"as a bonus and $",xbonus,"as an extra bonus thanks to your longeiviety with SoftwarePirates Inc. and had $",deduct,"deducted from your pay")
            else:
                if deduct==0:
                    print("The base salary at SoftwarePirates Inc., is", base)
                    print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and you earned $",bonus,"as a bonus")
                else:
                    print("The base salary at SoftwarePirates Inc., is", base)
                    print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and you earned $",bonus,"as a bonus and had $",deduct,"deducted from your pay")
                    
                    
        else:
            if deduct==0:
                print("The base salary at SoftwarePirates Inc., is", base)
                print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and earned no bonus.")
            else:
                print("The base salary at SoftwarePirates Inc., is", base)
                print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and you earned no bonus and had $",deduct,"deducted from your pay")
    if sales>1000000:
        commision=sales*.35
        total=base+commision
        if vacDays>3:
            total-=200
            deduct=200
        if timeW>3:
            total+=100000
            bonus=100000
            if timeW>60:
                total+=1000
                bonus+=1000
                if deduct==0:
                    print("The base salary at SoftwarePirates Inc., is", base)
                    print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and you earned $",bonus,"as a bonus and $",xbonus,"as an extra bonus thanks to your longeiviety with SoftwarePirates Inc.")
                else:
                    print("The base salary at SoftwarePirates Inc., is", base)
                    print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commisionoff of $",sales,"sales and you earned $",bonus,"as a bonus and $",xbonus,"as an extra bonus thanks to your longeiviety with SoftwarePirates Inc. and had $",deduct,"deducted from your pay")
            else:
                if deduct==0:
                    print("The base salary at SoftwarePirates Inc., is", base)
                    print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and you earned $",bonus,"as a bonus")
                else:
                    print("The base salary at SoftwarePirates Inc., is", base)
                    print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and you earned $",bonus,"as a bonus and had $",deduct,"deducted from your pay")
                    
                    
        else:
            if deduct==0:
                print("The base salary at SoftwarePirates Inc., is", base)
                print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and earned no bonus.")
            else:
                print("The base salary at SoftwarePirates Inc., is", base)
                print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",commision,"in commision off of $",sales,"sales and you earned no bonus and had $",deduct,"deducted from your pay")
main()
        

    
    
