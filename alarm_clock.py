import time, winsound

prompt = "How long do you want to set the alarm \n(put in seconds): "

def alarm(question): 
	time.sleep(question) #take user_input as the time to wait
	winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS) #play the sound after the time has run out

while True:
	user_input = input(prompt) #ask for user input 
	alarm(int(user_input))

	if input("Do you want to use the alarm again?(y/n) ") == 'n': #check if the user wants to use the alarm again
		break

