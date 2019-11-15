from datetime import datetime

# Current date time in local system
date = datetime.now().date()
date = str(date)
print("Todays Date:",date)
enterDate = input("Enter date in format shown above ({0}):".format(date))
if(enterDate == ""):
    enterDate = date

fileName = str("presentPeople"+enterDate+".txt")



# try:
#     fd=open(fileName, "r")
# except FileNotFoundError:
#     print("No One Present On This Date")
    
with open(fileName) as f:
    content = f.readlines()

content = [x.strip() for x in content] 

presenties = content[0].split()
presenties = [x.lower() for x in presenties]



print('\n'"Presenties on ",enterDate,":"'\n\n',presenties,'\n')

val = 'y'
while(val == 'y' or val == 'Y'):
    name = input("Enter name to check: ").lower()

    if name in presenties:
        print("Present"'\n')
    else:
        print("Absent"'\n')
    val = input("Want to check for someone else? (Y/n)")



#METHOD 2
# count =0
# for i in presenties:
#     if i == name:
#         count = count+1
#         print('present')



# if count == 0:
#     print("absent")