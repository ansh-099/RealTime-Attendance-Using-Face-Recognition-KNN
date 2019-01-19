from datetime import datetime

# Current date time in local system
date = datetime.now().date()
date = str(date)
fileName = str("presentPeople"+date+".txt")
print("Check Attendence of "+date)
f=open(fileName, "r")
presenties = {}


for line in f:
        for name in line.split():
           presenties[name] = 'p'  


print(presenties)


name = input("Enter name to check: ")
try:
    value = presenties[name]
    print("Present")
except KeyError:
    # Key is not present
    print("Absent")




#METHOD 2
# count =0
# for i in presenties:
#     if i == name:
#         count = count+1
#         print('present')



# if count == 0:
#     print("absent")