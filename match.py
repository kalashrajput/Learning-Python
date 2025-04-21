#match statement is like switch statement of c language.
day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day") #default case

day = 6
match day:
    case 2|4|6|8 :
        print("Even Number !")
    case 1|3|5|7|9 :
        print("Odd Number !")