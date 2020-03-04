#Lab 8
#boolean functions

def isValidVoter(age):
    #if statement -18+
    if age >= 18 and age <= 135:
        return True
    else:
        return False

def isLeapYear(year):
    if year % 4 == 0:
        return True
    else:
        return False
#define main()
def main():
    name = input('Please enter your name: ')
    age = int(input('Please enter your age: '))


    if isValidVoter(age):
        print('%s, at %d years old you are a valid voter' %(name,age))
    else:
        print('%s, at %d years old you are NOT a valid voter' %(name,age))


    year = int(input('Please enter the year: '))

    
    if isLeapYear(year):
        print('%d is a leap year' %(year))
    else:
        print('%d is not a leap year' %(year))




#call main()
main()

#nothing follows
