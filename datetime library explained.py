import datetime
#1...........................................................................

datetime.date.today() # will print today's date 

#2...........................................................................

datetime.date.today().strftime("%Y") # will print only current year

#3...........................................................................

datetime.date.today().strftime("%B") # will print only current month

#4...........................................................................

datetime.date.today().strftime("%D") # will print only current date

#5..........................................................................

print ("Week number of the year", datetime.date.today().strftime("%W"))

#6............................................................................

print ("Week number of the month", datetime.date.today().strftime("%w"))


#7................................................................................

print ("Day of year is", datetime.date.today().strftime("%j"))

#8............................................................................

print ("Day of week is", datetime.date.today().strftime("%A"))

#9...........................................................................

datetime.datetime.now() # will show current year,month,date,hour,minutes,second