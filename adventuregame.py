username = input("User Name?")
World = input("Which world would you like to enter? Neverland or Wonderland?")
Health = 200
forward = 0
backward = 0
left = 0
right = 0

while Health > 0:
	if World == "Neverland":											#World 1
		Move1 = input(" What is your move, " + username + "? w=forward, d= right, a= left, s=backward") #Round 1
		if Move1 == ("w"):
			forward += 5
			print ("Going forward")
		elif Move1 == ("s"):
			backward += 5
			print ("Going backward")
		elif Move1 == ("d"):
			right += 5
			print ("Going right")
		elif Move1 == ("a"):
			left += 5
			print ("Going left")
		
		Move2 = input(" What's your next move?") #Round 2
		if Move2 =="w" and Move1 == "w":
			Health += 10
			print ("There were resources ahead. Plus 10 Health")
		elif Move2 == "a" and Move1 == "a":
			Health -= 10
			print ("To the left there were zombies. Minus 10 Health.")
		elif Move2 == "d" and Move1 == "d":
			Health += 5
			print ("To the right there was potable water. Plus 10 Health.")
		elif Move2 == "s" and Move1 == "s":
			Health -= 5
			print ("Going backward wasted time and resources. Minus 5 Health.")
		elif Move2 == "w" and Move1 == "s":
			Health -= 5
			print ("You just went forward and backward. That was dumb. Minus 5 Health.")
		elif Move2 == "w" and Move1 == "a":
			Health += 5
			print ("You found some helpful citizens. Plus 10 Health.")
		else:
			if Move2 == ("w"):
				forward += 5
				print ("Going forward")
			elif Move2 == ("s"):
				backward += 5
				print ("Going backward")
			elif Move2 == ("d"):
				right += 5
				print ("Going right")
			elif Move2 == ("a"):
				left += 5
				print ("Going left")
			Health +=5
print ("Health = " + Health + " You Died")

#elif World == "Wonderland" 										#World 2
