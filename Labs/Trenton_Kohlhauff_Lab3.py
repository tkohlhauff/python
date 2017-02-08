#function for receiving user inputs and calling conversion functions
def main():
    print("Welcome to the freedom unit converter.")
    miles=int(input("How many miles would you like to convert?: "))
    fah=int(input("How many degrees fahrenheit would you like to convert?: "))
    gal=int(input("How many gallons would you like to convert?: "))
    lbs=int(input("How many pounds would you like to convert?: "))
    inch=int(input("How many inches would you like to convert?: "))
    milesToKm(miles)
    FahToCel(fah)
    GalToLit(gal)
    PoundsToKg(lbs)
    InchesToCm(inch)
    
    #check if user wants to leave program
    goagain=input("Would you like to convert again?: ")
    if goagain in ["yes","y","Yes","Y"]:
        main()
    else:
        print("Thank you for using the freedom unit converter.")
#conversion functions
def milesToKm(mile):
    km=mile*1.6
    print(mile,"Miles is equal to",format(km,".2f"),"kilometers")
def FahToCel(fah):
    cel=(fah-32)*5/9
    print(fah,"Degrees fahrenheit is equal to", format(cel,".2f"),"degrees celsius")
def GalToLit(gal):
    lit=gal*3.79
    print(gal,"Gallons is equal to",format(lit,".2f"),"liters")
def PoundsToKg(lbs):
    kg=lbs*.45
    print(lbs,"Pounds is equal to",format(kg,".2f"),"kilograms")
def InchesToCm(inch):
    cm=inch*2.54
    print(inch,"Inches is equal to",format(cm,".2f"),"centimeters")
main()
