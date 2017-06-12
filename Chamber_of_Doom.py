import random
import sys


#Dan Donohues Chamber of Doom.  You. Will. Probably. Die.


def rules():
	print ("\nWelcome to my game, the rules are simple.  Follow the halls until you get to the gold! \n")
	print "Make sure you type your decisions very similar to what is given to you...\n"
	print "For example, if it said 'jump off or fly away' you would type 'jump off' or 'fly away'."
	print "And now your ready to go. \nGood luck, you're probably gunna die. \n\n"

def start():
	rules()
	print "You are in a dark room."
	print "No idea how you got there."
	print "There are doors to your left and right."

	choice = raw_input("Which one do you go through?")

	if "left" in choice:
		bear_room()
	elif "right" in choice:
		cthulu_room()
	else: dead("You stumble around the room and starve to death.")


def dead(why):
	print why, '\nCongrats on death.'
	sys.exit(0)


def gold_room():
	print "This room is full of gold. How many pieces are you going to take?"

	gold_amount = input('enter a whole number > ')

	if gold_amount > 50:
		dead("You greedy bastard! \nYou turn into a gold statue and are stuck in the room for eternity.")
	elif gold_amount > 25 :
		print"Take your %r gold and get out of here, before I change my mind." % gold_amount
		win()
	elif gold_amount > 0:
		print "Really? That was stupid. I'm going to kill you for taking so little gold."
		dead('')
	else:
		print "Dummy you need to type a whole positive number."






def bear_room():
	print "There is a bear in here."
	print "The bear loves to eat honey."
	print "You are covered in honey."
	print "Do you run or stay?"

	next = raw_input('> ')

	if "run" in next:
		print "Good job you ran and stumbled upon a gold room!"
		gold_room()
	else:
		print "Why wouldn't you run away from a bear?"
		dead("You were mauled by the bear.")

def cthulu_room():
	print "Oh shit... "
	print "Here comes Cthulu!"
	print "Throw a grenade or close your eyes?"

	next = raw_input('> ')
	if "throw" in next:
		print "Hell yeah, you blew that mofo up, gold for you!"
		gold_room()
	else: print 'Well.. that was dumb.  \n But Cthulu spared your life and teleported you back home. \nYou wake up in bed, must have been a nightmare.\n Go get some breakfast?'
	breakfast = raw_input('yes or no?')
	if "yes" in breakfast:
		print "Your mom is already downstairs making cereal.  She turns around to say good morning, and her face is that of the evil Cthulu! You die."
		dead('You suck!')
	else:
		print "Good choice, it was too early for breakfast anyways."
		school = raw_input('Do you get on the bus and go to school?  yes or no > ')

		if "yes" or "Yes" in school:
			print "You get to school and a bully starts picking on you... choose a or b to defend yourself."

			bully = raw_input('> ')

			if bully == 'a' or "A":
				dead("You decided to nuke the bully.  Good choice, not only did you blow up the bully, but also everyone within a 2 mile radius.")
			elif bully == 'b' or "B": print "The bully takes your money... but today you stuffed your pockets with monopoly money and AIDS.\nYou don't have any money, but the bully has AIDS."
			else: dead('You didnt type a or b did you.  Well your inability to type has doomed you. \nOnce you get off this computer, a samurai will attack. Good luck...' )
		else:
			print "You didnt go to school and now are a hillbilly. You drink too much moonshine and wake up in a mysterious room."
			gold_room()


def win():
	print "Holy shit... you won!!!  You will have good karma for the rest of the day."
	sys.exit(0)


start()
