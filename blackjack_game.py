import random
import sys


"""Blackjack game for single player. It promps user whether to hit a new card or stand then calculates total card points.

"""

#loads new card deck
def loadDeck():
	global flag_house
	global flag_player
	global house_card_val
	global player_card_val
	global house_card_list
	global player_card_list
	global player_card
	global house_card
	global cardo
	
	flag_house=[" "]
	flag_player=[" "]
	house_card_val=0
	player_card_val=0
	house_card_list=["House: "]
	player_card_list=["Player: "]
	player_card=""
	house_card=""
	cardo= {"AC":11,"2C":2,"3C":3,"4C":4,"5C":5,"6C":6,"7C":7,"8C":8,"9C":9,"10C":10,"QC":10,"JC":10,"KC":10,"AS":11,"2S":2,"3S":3,"4S":4,"5S":5,"6S":6,"7S":7,"8S":8,"9S":9,"10S":10,"QS":10,"JS":10,"KS":10,"AD":11,"2D":2,"3D":3,"4D":4,"5D":5,"6D":6,"7D":7,"8D":8,"9D":9,"10D":10,"QD":10,"JD":10,"KD":10,"AH":11,"2H":2,"3H":3,"4H":4,"5H":5,"6H":6,"7H":7,"8H":8,"9H":9,"10H":10,"QH":10,"JH":10,"KH":10}
#House plays in this function.It changes the global variable named house_card_val which is for storing value of house's card.
def housePlay(house_card_val_local,house_card_list):
	
	global house_card_val
	house_card=random.choice(cardo.keys())
	house_card_val_local = house_card_val_local + cardo.pop(house_card)
	house_card_list.append(house_card)
	for house in house_card_list:
	#Here function looks to value of the card if it is higher than 21 and house's hand contains and A it translates A value to 1.
		if house.find("A") !=-1:
			if house_card_val_local>21:
				for item3 in flag_house:
				#In this function if house's hand contains any A it recompense the extra -10 calculation.It holds the A variables in another list named flag_house
						if item3.find(item) !=-1:
							house_card_val_local+=10
				house_card_val_local-=10
				flag_house.append(item)
				
	house_card_val =house_card_val_local		
	#Players turn is played in this function.It changes the global variable named player_card_val which is for storing value of player's card.
def customerPlay(player_card_val_local,player_card_list):
	global player_card_val
	player_card= random.choice(cardo.keys())
	player_card_val_local= player_card_val_local + cardo.pop(player_card)	
	player_card_list.append(player_card)
	for item in player_card_list :
	#Here function looks to value of the card if it is higher than 21 and player's hand contains and A it translates A value to 1.
		if item.find("A") !=-1:
			if player_card_val_local >21:
				for item2 in flag_player:
				#In this function if player's hand contains any A it recompense the extra -10 calculation.It holds the A variables in another list named flag_player
						if item2.find(item) !=-1:
							player_card_val_local+=10
				player_card_val_local-=10
				flag_player.append(item)
	player_card_val=player_card_val_local
	#Here program asks player whether they want to continue to get another card or not by asking Hit for h,Stand for s.
def prompPlay():
	global player_card_val
	global house_card_val
	global flag_player
	player_hit= raw_input("To get another card enter h else enter s")
	if player_hit=="h":
		
		customerPlay(player_card_val,player_card_list)
		controlWinHit()
		
		
		
	elif player_hit=="s" :
		housePlay(house_card_val,house_card_list)
		
		
		controlWinStay()
	else :
		print "You entered wrong character please try again"
		prompPlay()
		#Here function makes controls if player want's another card.
def controlWinHit():
	global player_card_val
	global house_card_val
	global player_money
	global player_bet
	for item in player_card_list:
			print item
	print "House Total:",house_card_val,"You:",player_card_val
	if player_card_val>21:
		
		
		print "You Lose"
		print "You have",player_money,"chips"
		loadDeck()
		prompExit()
	elif player_card_val == 21 :
		housePlay(house_card_val,house_card_list)
		player_money+=3*player_bet/2
		
		print "You Win"
		print "You have",player_money,"chips"
		loadDeck()
		prompExit()
	else:
		prompPlay()
		#Here this function controls if player chooses to stay.
def controlWinStay():
	global player_money
	global player_bet
	for h in house_card_list:
			print h
	print "House Total:",house_card_val,"You:",player_card_val
	if (house_card_val<=21 and house_card_val>player_card_val) or (house_card_val==21 and player_card_val==21):
		
		print "You lose"
		print "You have",player_money,"chips"
		loadDeck()
		prompExit()
	elif house_card_val>21 :
		player_money+=2*player_bet
		print "You Win"
		print "You have",player_money,"chips"
		loadDeck()
		prompExit()
	elif player_card_val > house_card_val and house_card_val<17:
		housePlay(house_card_val,house_card_list)
		controlWinStay()
	elif house_card_val==player_card_val and house_card_val<17:
		housePlay(house_card_val,house_card_list)
		controlWinStay()
	elif house_card_val == player_card_val  :
		print "You lose"
		print "You have",player_money,"chips"
		loadDeck()
		prompExit()
	elif player_card_val>house_card_val:
		player_money+=2*player_bet
		print "You Win"
		print "You have",player_money,"chips"
		loadDeck()
		prompExit()
	
	else:
		print " "
def prompExit():
	global game_status
	global player_money
	if player_money>0:
		while True: #infinite loop
			prompEx=int(input("If you want to play please enter 1 else 0"))
			try:
				prompEx= int(prompEx)
				if prompEx ==1 or prompEx ==0:		
					break
		  #conditions true can get out
					
			except ValueError:  #error
				print ("Please make sure that you enter a valid number")
		game_status=prompEx

	
#initial definitions
game_deck=0
ace="A"
game_status=1
player_money=100
player_bet=0
#end defs


while game_status== 1:
	
	if game_status ==1:
		
		
		if player_money>0:
			while True: #infinite loop
				player_bet = int(input("Please enter your bet"))
				try:
					if player_bet<=player_money and player_bet>=1:
						player_bet= int(player_bet)
						break  #conditions true can get out
					
				except ValueError:  #error
					print ("Please make sure that you enter a number and dont exceed the chips you have")
			
			
			player_money= player_money - player_bet
			
			
			#Initial definitions
			loadDeck()
			flag_house=[" "]
			flag_player=[" "]
			house_card_val=0
			player_card_val=0
			house_card_list=["House: "]
			player_card_list=["Player: "]
			player_card=""
			house_card=""
			#Card object to create card-deck for game
	
			
			
			
			
			
			housePlay(house_card_val,house_card_list)
			customerPlay(player_card_val,player_card_list)
			customerPlay(player_card_val,player_card_list)
			for item in house_card_list:
				print item
			print "Total" ,house_card_val 	
			for item in player_card_list:
				print item
			print "Total",player_card_val
			if player_card_val==21:
				housePlay(house_card_val,house_card_list)
				player_money+=3*player_bet/2
				print "You Win "
				print "You have",player_money,"chips"
				loadDeck()
				prompExit()
			else:
				
				prompPlay()
				
				
		else:
			game_status=0
			print "Thank you for playing"
	else:
		
		print "Thank you for playing you have ",player_money,"chips"
