#Andrey Ilkiv Assignment 3 Problem 3 10/05/2020 section 01

#-----------------------------------------------
#Print header and empty lines for format
#asks user to input start date and birthday in MMDDYYYY format
#intBirthDate and intStartDate store input in int format for arithmetic
#StartDate and BirthDate store the input as a string for later use
print('' , 'Enter the start date and birthdate for an employee to determine their age at the start of employment.')
StartDate = input('Enter start date MMDDYYYY: ')
BirthDate = input('Enter birth date MMDDYYYY: ')
#-----------------------------------------------
                    
#-----------------------------------------------
#splitting months, days, and year by using division operators and modulus
#formatting for 0 decimal points
#alloweddate and allowed month check for age of 21 by month and year
Day = format((((int(BirthDate)//10000)/100)%(int(BirthDate)//1000000))*100 , '.0f')
Day = int(Day)
Month = int(BirthDate)//1000000
StartMonth = int(StartDate)//1000000
Year = format(((int(BirthDate)/10000)%(int(BirthDate)//10000)*10000) , '.0f')
Year = int(Year)
StartYear = format(((int(StartDate)/10000)%(int(StartDate)//10000)*10000) , '.0f')
StartYear = int(StartYear)
suffix = ''
allowedmonth = int(Month) <= StartMonth
alloweddate = (StartYear - Year) >= 21

#creates correct suffix for each numerical day
if (4 <= Day <=20 or 24 <= Day <= 30):
    suffix = 'th'
if (Day == 3 or Day == 23):
    suffix = 'rd'
if (Day == 1 or Day == 21 or Day == 31):
    suffix = 'st'
if (Day == 2 or Day == 22):
    suffix = 'nd'

#changes month from a number to a string and spells out the month
if (Month >= 10):
    if (str(Month) == '10'):
        Month = 'October'
    if (str(Month) == '11'):
        Month = 'November'
    if (str(Month) == '12'):
        Month = 'December'

#changes month from single digit to include leading 0 and spells out month    
if (Month <= 9):
    Month = ('0' + str(Month))
    if (Month == '01'):
        Month = 'January'
    if (Month == '02'):
        Month = 'February'
    if (Month == '03'):
        Month = 'March'
    if (Month == '04'):
        Month = 'April'
    if (Month == '05'):
        Month = 'May'
    if (Month == '06'):
        Month = 'June'
    if (Month == '07'):
        Month = 'July'
    if (Month == '08'):
        Month = 'August'
    if (Month == '09'):
        Month = 'September'
print('The contestant was born on ' , Month , ' ' , Day , suffix , ',' , ' ' , Year , sep='')
# ' symbol for neatness
symbol = "'"
#-----------------------------------------------

#-----------------------------------------------
#Checks if the allowed date is greater than or equal to the birthdate
#if it is then program says that the constestan is eligible for taping on starting date
#if not then program says contestant is not eligible for taping on starting date
if (alloweddate == True and allowedmonth == True):
    print('ELIGIBLE: The contestant will be 21 by the time taping begins')
else:
    print('NOT ELIGIBLE: The contestant won' + symbol + 't be 21 by the time taping begins')
#-----------------------------------------------
