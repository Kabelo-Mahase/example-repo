
print("Triathlon Awards!\n")
units = "Minutes"
print("Please enter your respective completion times for each event (in minutes)\n")
Swimming = int(input("Swimming :" ))
print(Swimming, units)
Cycling = int(input("Cycling  :"))
print(Cycling, units)
Running = int(input("Running  :"))
print(Running , units)
print()
Times = [Swimming, Cycling, Running]
print("you have entered the following times :",Times , units)
print()
print("Total time taken for the triathlone : ",sum(Times) , units)
completion_time = sum(Times)
if(completion_time) >=0 and completion_time <=100 :
    print("Award : Provincial colours")
elif(completion_time) >= 100 and completion_time  <=105 :
       print("Award : Provincial half colours")
elif(completion_time) >= 106 and  completion_time <=110 :
    print("Award : Provincial scroll ")
else : 
    print("No Award")

