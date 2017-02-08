def main():
    commisionPCT=0
    bonus=0
    xBonus=0
    print("Welcome to SoftwarePirates Inc., payroll manager!")
    name=input("First lets start off with your name: ")
    timeW=int(input("How many months have you worked with this company?: "))
    vacDays=int(input("How many vacations days have you been on this month?: "))
    sales=int(input("In dollar amount how much have you sold this month?: "))
    if sales<10000:
        payroll(commisionPCT,name,timeW,vacDays,sales,bonus,xBonus)
    if sales>10000 and sales<=100000:
        commisionPCT=.02
        payroll(commisionPCT,name,timeW,vacDays,sales,bonus,xBonus)
    if sales>100000 and sales<=500000:
        commisionPCT=.15
        if timeW>3:
            bonus=1000
        if timeW>60:
            xBonus=1000
        payroll(commisionPCT,name,timeW,vacDays,sales,bonus,xBonus)
    if sales>500000 and sales<=1000000:
        commisionPCT=.28
        if timeW>3:
            bonus=5000
        if timeW>60:
            xBonus=1000
        payroll(commisionPCT,name,timeW,vacDays,sales,bonus,xBonus)
    if sales>1000000:
        commpisionPCT=.35
        if timeW>3:
            bonus=100000
        if timeW>60:
            xBonus=1000
        payroll(commisionPCT,name,timeW,vacDays,sales,bonus,xBonus)
def payroll(commisionPCT,name,timeW,vacDays,sales,bonus,xBonus):
    commision=sales*commisionPCT
    base=2000
    deduct=0
    total=base+commision+bonus+xBonus
    if vacDays>3:
        total-=200
        deduct=200
    if commision>0:
        if xBonus==0:
            if deduct==0:
                print("The base salary at SoftwarePirates Inc., is", base)
                print(name,"thanks for your",timeW,"months of working with us, you earned $",
                        total,"this month with $",commision,"in commision off of $",
                        sales,"sales and you earned $",bonus,"as a bonus")
            else:
                print("The base salary at SoftwarePirates Inc., is", base)
                print(name,"thanks for your",timeW,"months of working with us, you earned $",total,
                      "this month with $",commision,"in commision off of $",sales,"sales and you earned $",bonus,
                      "as a bonus and had $",deduct,"deducted from your pay")
        if xBonus>0:
            if deduct==0:
                print("The base salary at SoftwarePirates Inc., is", base)
                print(name,"thanks for your",timeW,"months of working with us, you earned $",total,
                      "this month with $",commision,"in commision off of $",sales,"sales and you earned $",bonus,
                      "as a bonus and $",xBonus,"as an extra bonus thanks to your longeiviety with SoftwarePirates Inc.")
            else:
                print("The base salary at SoftwarePirates Inc., is", base)
                print(name,"thanks for your",timeW,"months of working with us, you earned $",total,
                      "this month with $",commision,"in commisionoff of $",sales,"sales and you earned $",bonus,
                      "as a bonus and $",xBonus,"as an extra bonus thanks to your longeiviety with SoftwarePirates Inc. and had $",deduct,"deducted from your pay")
    else:
        if deduct!=0:
            print("The base salary at SoftwarePirates Inc., is", base)
            print(name,"thanks for your",timeW,"months of working with us, you earned $",total,
                  "this month with $",sales,"amount of sales, you earned no bonus, and had",deduct,"deducted from your pay due to",
                  vacDays,"days of vacation.")
        else:
            print("The base salary at SoftwarePirates Inc., is", base)
            print(name,"thanks for your",timeW,"months of working with us, you earned $",total,"this month with $",sales,"amount of sales and earned no bonus.")

main()           
            
    
        
        
    
        
