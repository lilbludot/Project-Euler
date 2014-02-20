def alg(mo, day, year):
    """This program uses Zeller's alogorithm to figure out tghe day of the week on
on which a given date will fall or fell."""

    #changing mo into lower case
    month=mo.lower()
    #dictionary is created to assign a number for each month according to Zeller.
    month_dict={"january":11, "february":12, "march":1, "april":2 \
                ,"may":3, "june":4, "july":5, "august":6, \
                "september":7, "october":8, "november":9, "december":10}
    if month in month_dict:
        A=month_dict[month]
    else:
        print "Error. Invalid entry for the month."
    # setting B equal to the day and making it type integer    
    B=int(day)
    if B<1 or B>31 :
        print "Error. Invalid entry for the day."
    #setting yy equal to year making its type integer.     
    yy=int(year)
    #adjusting the value of yy as per instructions for Zeller's algorithm
    if A==11 or A==12:
        yy-=1
    if yy<0:
        print "Error. Invalid entry for the year."
    #assigning the year of the century to C    
    C=yy%100
    #assigning the century to D
    D=yy/100
    #Now copying the formulas from Zeller's algorithm:
    W=(13*A-1)/5
    X=C/4
    Y=D/4
    Z=W+X+Y+B+C-2*D
    R=Z%7
    #the value of R is used to determine day the date falls on according
    #to the week_day_dict defined below:
    week_day_dict={0:"Sunday", 1: "Monday", 2:"Tuesday", 3:"Wednesday"\
                   , 4:"Thursday", 5:"Friday",  6: "Saturday"}
    week_day=week_day_dict[R]
    return week_day


#print zellers("March", 10, 1940)
