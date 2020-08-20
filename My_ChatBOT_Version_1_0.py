import pyttsx3
import os
from datetime import datetime

os.system("cls")
print("#######################################################################################################################")
print("#######################################################################################################################")
print("---------------------------------------------------[ My ChatBOT 1.0 ]--------------------------------------------------")
print("#######################################################################################################################")
print("#######################################################################################################################")

pyttsx3.speak("My ChatBOT 1.0")

#Input your username
pyttsx3.speak("Please enter your name to continue")
print("Please enter your name to continue : " , end='')


#Storing the Name input in a variable
User_Name = input().upper()

#Clearing the screen
os.system("cls")

#Storing Chatbot Name
cb_name = "ALEXA"

#Getting the current Date
print("----------------------------------------------------------------------------------------------------------------------")
today = datetime.now()
print("Username     :", User_Name)
print("Login date   :", today.strftime("%Y-%m-%d %H:%M:%S"))

#Welcome_screen of my chatbot
print("-----------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------[ My ChatBOT 1.0 ]--------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------------")
print(">>",cb_name,"    : Hi ",User_Name,"!!! My name is ", cb_name)
pyttsx3.speak(" Hi Sir!!! My name is ALEXA")
print(">>",cb_name,"    : I am having shortcuts to open administrative tools, system or user installed applications for you")
pyttsx3.speak(" I am having shortcuts to open administrative tools, system or user installed applications for you")
print(">>",cb_name,"    : How may I help you Sir?")
pyttsx3.speak(" How may I help you Sir? ")

while True:
#for getting the reply from end-user
	print(">>",User_Name,"     : " , end='')
	p = input()


	if (("Taskmanager" in p) or ("taskmanager" in p) or ("TASKMANAGER" in p) or ("TaskManager" in p))  and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : Jeez!!! Kill the not responding taks it will consume more memory sir")
		pyttsx3.speak("	Jeez!!! Kill the not responding tasks it will consume more memory sir")
		os.system("taskmgr")
    
	elif (("Systemconfiguration" in p) or ("configuration" in p) or ("System Configuration" in p) or ("system configuration" in p))  and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):		
		print(">>",cb_name,"    : Gonna change system startup configurations.. Go Ahead sir!! ")
		pyttsx3.speak("	Gonna change system startup configurations.. Go Ahead sir!! ")
		os.system("msconfig")
    
	elif (("Notepad" in p) or ("notepad" in p) or ("NOTEPAD" in p) or ("NotePad" in p))  and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : Prioritize your everyday tasks with notepad sir it will be helpful ...")
		pyttsx3.speak(" Prioritize your everyday tasks with notepad sir it will be helpful ...")		
		os.system("notepad")

	elif (("Perfomancemonitor" in p) or ("monitor" in p) or ("performance" in p) or ("performance monitor" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : Oh no!! Lagging in performance is more irritaning thing.. I will open it for you sir")
		pyttsx3.speak("	Oh no!! Lagging in performance is more irritaning thing.. I will open it for you sir")
		os.system("perfmon")

	elif (("Registryeditor" in p) or ("Registry" in p) or ("registry" in p) or ("Registry editor" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : Yeah Sir!!! I will open registry settings for you")
		pyttsx3.speak("	Yeah Sir!!! I will open registry settings for you")
		os.system("regedit")

	elif (("systeminformation" in p) or ("systeminfo" in p) or ("System Information" in p) or ("Systeminformation" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : Amazing!!! Your system is having powerful specifications.. If you don't believe me i will show you sir")
		pyttsx3.speak("	Amazing!!! Your system is having powerful specifications.. If you don't believe me i will show you sir")
		os.system("msinfo32")

	elif (("Windows Firewall" in p) or ("firewall" in p) or ("Windowsfirewall" in p) or ("Firewall" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : Need protection from harmful viruses.. I am not saying corona")
		pyttsx3.speak("	Need protection from harmful viruses.. I am not saying corona")
		os.system("WF")		

	elif (("Remote desktop" in p) or ("RDP" in p) or ("rdp" in p) or ("remote desktop" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : Please connect with your friends system.. He needs your help")
		pyttsx3.speak("	Please connect with your friends system.. He needs your help")
		os.system("mstsc")	

	elif (("Snipping Tool" in p) or ("snipping" in p) or ("snipping tool" in p) or ("snippingtool" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : No worries!! Please capture every activity with snipping tool")
		pyttsx3.speak("	No worries!! Please capture every activity with snipping tool")
		os.system("SnippingTool")

	elif (("Control Panel" in p) or ("Control" in p) or ("control panel" in p) or ("control" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : Yes Captain!! Please take full control of your system")
		pyttsx3.speak("	Yes Captain!! Please take full control of your system")
		os.system("control")
		
	elif (("MSpaint" in p) or ("paint" in p) or ("Paint" in p) or ("mspaint" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : I hope you will beat picasso with your drawings :O")
		pyttsx3.speak("	I hope you will beat picasso with your drawings ")
		os.system("mspaint")

	elif (("Calculator" in p) or ("Calc" in p) or ("calculator" in p) or ("calc" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : I know maths is tough for you sir :P")
		pyttsx3.speak("	I know maths is tough for you sir")
		os.system("calc")

	elif (("Google Chrome" in p) or ("Chrome" in p) or ("chrome" in p) or ("google chrome" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : Fine Sir!! Browse whatever you want but please bookmark for important links..")
		pyttsx3.speak("	Fine Sir!! Browse whatever you want but please bookmark for important links..")
		os.system("chrome google.com")

	elif (("Internet Explorer" in p) or ("IE" in p) or ("explorer" in p) or ("internet explorer" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):	
		print(">>",cb_name,"    : Sir!! I think you must be 90s Kid :D")
		pyttsx3.speak("	Sir!! I think you must be ninetees Kid ")
		os.system("iexplore google.com")

	elif (("NPad" in p) or ("plus" in p) or ("npadplusplus" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):	
		print(">>",cb_name,"    : Sir!! Opening notepad positve positive :D")
		pyttsx3.speak("	Sir!! Opening notepad positve positive ")
		os.system("notepad++")

	elif (("Windows Media Player" in p) or ("media" in p) or ("player" in p) or ("media player" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):	
		print(">>",cb_name,"    : Today's weather is chill.. So hear some melody songs Sir")
		pyttsx3.speak("	Today's weather is chill.. So hear some melody songs Sir ")
		os.system("wmplayer")

	elif (("Adobe Reader" in p) or ("Reader" in p) or ("reader" in p) or ("adobe" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):	
		print(">>",cb_name,"    : Great!! I have lots of pdf story book collection for you Sir.. ")
		pyttsx3.speak("	Great!! I have lots of pdf story book collection for you Sir.. ")
		os.system("AcroRd32")

	elif  (("Thankyou" in p)  or ("exit" in p) or ("logout" in p) or ("close" in p)):
		print(">>",cb_name,"    : Are you satisfied with my service sir? ")
		pyttsx3.speak("	Are you satisfied with my service sir?")
		print(">>",User_Name,"     : " , end='')
		feedback = input()
		if (("yes" in feedback) or ("ok" in feedback) or ("great" in feedback) or ("nice" in feedback) or ("satisfied" in feedback)):
			print(">>",cb_name,"    : Thank you for your valuable comments and time sir")
			pyttsx3.speak("	Thank you for your valuable comments and time sir :D")			
			break
		elif (("no" in feedback) or ("not ok" in feedback) or ("bad" in feedback) or ("not satisfied" in feedback) or ("awful" in feedback)):
			print(">>",cb_name,"    : I think i need a upgrade sir.. Will see you soon in my version 2.0")
			pyttsx3.speak("	I think i need a upgrade sir.. Will see you soon in my version 2.0")
			break

	else:
		print(">>",cb_name,"    : OOPS!!! Please provide me a valid query request for better results")
		pyttsx3.speak("OOPS!!! Please provide me a valid search query for better results")
print("-----------------------------------------------------[ VIMAL DAGA ]----------------------------------------------------")
pyttsx3.speak("Guided by VIMAL DAGA")
print("---------------------------------------------------[ JOHN JAYAKUMAR ]--------------------------------------------------")
pyttsx3.speak("Created by JOHN JAYAKUMAR")
print("------------------------------[ Please do follow me on linkedin, instagram and facebook ]------------------------------")
pyttsx3.speak("Please do follow me on linkedin, instagram and facebook")
