def freetime(calA,boundsA):
    freeslots=[]
    temp = None
    for ind,i in enumerate(calA):
       # print("lastchck",ind , len(calA)-1)
        if ind== 0:
            print(i[0],boundsA[0])
           
            if (i[0] - boundsA[0]) >= 1 :
                freeslots.append((boundsA[0],i[0]))
                
        
        else:    
         #   print("med",i[0],temp[1])
            if  (i[0] - temp[1])   >= 1   :
                freeslots.append((temp[1],i[0]))
        if ind == len(calA)-1:
          #  print("last",i[1],boundsA[1])
            if (boundsA[1]-i[1] ) >= 1 :
                freeslots.append((i[1],boundsA[1]))
            
        temp = i     
    return freeslots

def Find_slots(calA,boundsA,calB,boundsB,dur):
    freeA= freetime(calA,boundsA)
    print(freeA)
    freeB= freetime(calB,boundsB)
    print(freeB)

if __name__ == "__main__":
    DailyBounds= [9,12]
    calenderA= [(9,10)]
    calenderB= [(10,11),]

    Find_slots(calenderA,DailyBounds,calenderB,DailyBounds,1)

