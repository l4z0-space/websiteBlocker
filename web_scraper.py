import webbrowser
import time                                          # @ Lazaron Shyta
from datetime import datetime as dt                  # @ Python MegaCourse in Udemy 

host_path=r"C:\Windows\System32\drivers\etc\hosts" # the file where we can change the permission for having access in certain websites
redirect="127.0.0.1"
website_lists=["www.facebook.com","facebook.com"] # blocked websites


while True:
    before =  (dt.now().year,dt.now().month,dt.now().day,8) # time when working hours start
    now = (dt.now().year,dt.now().month,dt.now().day,dt.now().hour) # current time
    then =  (dt.now().year,dt.now().month,dt.now().day,9) # time when working hours end
    if before < now < then: # compare the time
        print("Working Hours")
        with open(host_path,'r+') as file:  # open file / with the 'r+' we can add more lines
            content = file.read()
            for website in website_lists: # iterate the websites
                if website in content:
                    pass
                else:
                    file.write(redirect +" "+ website + "\n") # append the line
    else:
        with open(host_path,'r+') as file: # open file
            content = file.readlines()
            file.seek(0)  # used to append the lines in the beggining of the page
            for line in content:
                if not any(website in line for website in website_lists): # check if any of the websites is in the line
                    file.write(line)
            file.truncate() # removes the other text
        print("Fun Hours")
    time.sleep(10) # update every 10 seconds
