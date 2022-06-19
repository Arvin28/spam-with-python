import pyautogui 
import webbrowser
import time
 
message = input("Enter the message you want to send (dont use this blank if you want to paste your clipboard)  ")

repeats = int(input("How many times do you want to send the message?"))

delay = int(input("How many milliseconds do you want to wait in between each message?  "))

isLoaded = input("Press Enter when your message app is loaded")



print("You have 5 seconds to select the page you want to paste on it")

time.sleep(5)


for i in range(0,repeats):         
	if message != "":
		pyautogui.typewrite(message)     
		pyautogui.press("enter")
	else:
		pyautogui.hotkey('ctrl', 'v')      
		pyautogui.press("enter")

	time.sleep(delay/1000)


print("Easy\n")
