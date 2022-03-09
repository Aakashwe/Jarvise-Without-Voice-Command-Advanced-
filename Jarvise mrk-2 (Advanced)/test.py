import random
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()


def gameStone():
	print("Press 's' for Stone\n")
	print("Press 'p' for Paper\n")
	print("Press 'sc' for Scissors\n")
	userChoice = input("Chose any above Options\n").lower()
	game = ["Stone", "Paper", "Scissors"]
	AI = random.choice(game)

	# Paper
	if AI == "Paper" and userChoice == "sc":
		speak("Congrats you won sir")
		print("Aakash has won")
		print(f"Jarvis chose {AI}")
	elif AI == "Paper" and userChoice == "s":
		speak("Huray, i won")
		print("Jarvis has won")
		print(f"Jarvis chose {AI}")
	elif AI == "Paper" and userChoice == "p":
		speak("Tie")
		print("Tie")
		print(f"Jarvis chose {AI}")

	# Stone
	elif AI == "Stone" and userChoice == "sc":
		speak("Huray, i won")
		print("Jarvis has won")
		print(f"Jarvis chose {AI}")
	elif AI == "Stone" and userChoice == "s":
		speak("Tie")
		print("Tie")
		print(f"Jarvis chose {AI}")
	elif AI == "Stone" and userChoice == "p":
		speak("Congrats you won sir")
		print("Aakash has won")
		print(f"Jarvis chose {AI}")
	# Scissors

	elif AI == "Scissors" and userChoice == "p":
		speak("Huray, i won")
		print("Jarvis has won")
		print(f"Jarvis chose {AI}")
	elif AI == "Scissors" and userChoice == "s":
		speak("Congrats you won sir")
		print(f"Jarvis chose {AI}")
		print("Aakash has won")
	elif AI == "Scissors" and userChoice == "sc":
		speak("Tie")
		print("Tie")
		print(f"Jarvis chose {AI}")
	else:
		print("Please input a valid input")
		gameStone()
gameStone()

