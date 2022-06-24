#no of guesses 9
#print no. of guesses left
#no. of guesses he took to finish
#game over
print("Guess The Number And You Have Total Of 5 Chances")
Att = 4
At = 1
while(True):
	inp = int(input())
	if inp>18 and Att>0:
		print("Choose a Smaller Number Then",inp)
		print("You Have ",Att,"Chances Left")
		Att = Att-1
		At = At+1
		continue
	if inp<18 and Att>0:
		print("Choose a Bigger Number Then",inp)
		print("You Have ",Att,"Chances Left")
		Att = Att-1
		At = At+1
		continue
	if inp==18:
		print("Congratulatios, You Have Completed Game In Just",At,"Chance")
		break
	if Att==0:
		print("game over, No Chances Left")
		break
#	if Inp.isalpha:
#		print("please choose an integer ")
#		continue
