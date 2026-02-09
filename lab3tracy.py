def check_weekday_or_weekend(day_number):
    if 1<=day<=5:
       return "Weekday"
    elif 6<=day<=7:
       return "Weekend"
    else:
      return "Not a proper day!"
   
    
def get_day_name(day_number):
    if day==1:
       return "Monday"
    elif day==2:
       return "Tuesday"
    elif day==3:
       return "Wednesday"
    elif day==4:
       return "Thurday"
    elif day==5:
       return "Friday"
    elif day==6:
       return "Saturday"
    elif day==7:
       return "Sunday"
    else:
       return "Not a proper day number!"
    
if __name__=='__main__':
  day=int((input("Enter a number from 1 to 7:")))
  print(f"The the number entered is {(check_weekday_or_weekend(day))}.")
  print(f"The day name is {get_day_name(day)}.")
