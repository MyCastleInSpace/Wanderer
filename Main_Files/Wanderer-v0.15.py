
		# Game System Modules

import click 			# For the clear screen function
import keyboard 		# For arrow key movement function (WIP)
from playsound import playsound # For ambient sounds to play
import multiprocessing 		# Additional support for Playsound
import vlc 			# Secondary system for sounds (Not Used Currently)
import sys			# For creating a secondary path for modules (adding /game_data as the usable directory for modules)

		# Game Data Modules

sys.path.insert(0, '/home/castle/Wanderer/Alpha/game_data') # Setting /game_data as usable directory

import roomdesc 		# For Room Description Plaintexts

		# HUD and Basic Variables		

player = None
version_number = 'v0.14'
i = 1
startup = True
health = "?"
maxhealth = "?"
money = 0
playername = "Unknown"
privPlayer_loc = "locDesertedInn"
pubPlayer_loc = "A Deserted Inn"
gotoLoc = "locations[privPlayer_loc]"
invalid_comm = 0

			#items

flashlight = True
haveFlashlight = False
takeCheck = 'take'
moveCheck = 'move'
funcAppend = '()'
playerInventory = ['']
elseSKIP = 0
firstInvalid = True
at_menu = True
#sound_file = ''
p = multiprocessing.Process(target=playsound, args=("music/startmenu.mp3",))

		# Map Variables
map_roomT = ["[X]", "[^]", "[X]", "[X]", "[ ]", "[X]", "[ ]", "[*]", "[?]"]
#map

		# Location Items
itemAppend = str('Items')
localItems = ''
locDesertedInnDiningItems = ['flashlight', 'axe']
tempLoc = privPlayer_loc

# Defines the clear screen function
def clrscr():
	# Clear screen using clrscr()
	click.clear()

clrscr()
while i == 1:
	#Define the function for items check of the current room
	def localItemsCheck():
		global privPlayer_loc
		global tempLoc
		global localItems
		global itemAppend
		str(tempLoc)
		str(itemAppend)
		tempLoc += itemAppend
		if len(tempLoc) == 0:
			print("There is nothing here.")
		if len(tempLoc) > 0:
			print(f"""
		{tempLoc}
			""")
			tempLoc = privPlayer_loc
	# Defines the function to clear screen and redraw playscreen
	def hudRedraw():
		clrscr(); hudTOP();
	
	def commands_help():
	    global invalid_comm
	    invalid_comm = 1
	    print("""
	That 3x3 grid at the top right is a map.
	    
	Move: Used to navigate the environment
	    Usage: Type 'move' followed by 'forward',
	    'back', 'left', or 'right'.
	    Type this: move right, move forward, etc.
	    
	    
	Take: Used to take items from the environment
	    Usage: Type 'take' followed by the name of
	    the item you wish to take.
	    Type this: take flashlight
	    
	Inventory: Used to view your current inventory
	    Usage: inventory
	    Type this: inventory
	
	Debug: Used to display debugging information
	    Usage: Displays variable values for
	    debugging and quality control.
	    Type this: debug
	
	Map Legend:
	[*] = You
	[ ] = Enterable Room
	[X] = Innaccessible Room
	[^] = More Rooms Where the Arrow Points
	[?] = Point of Interest
	    """)
	  
	
	# Defines the top of the HUD function (Prints vars player, health, money, and pubPlayer_loc)
	def hudTOP():
#	while map_room_num < 10:
	    print(f"Identity: {playername}			Location: {pubPlayer_loc}")
	    print(f"						<<<Map>>>")
	    print(f"Health: {health}/{maxhealth}					{map_roomT[0]}{map_roomT[1]}{map_roomT[2]}")
	    print(f"Money: ${money}					{map_roomT[3]}{map_roomT[4]}{map_roomT[5]}")
	    print(f"						{map_roomT[6]}{map_roomT[7]}{map_roomT[8]}")
# for debug	    print(map_roomT[5])
	
	def locDesertedInn():
	    global tempVar; global privPlayer_loc; global funcAppend
	    tempVar = privPlayer_loc + funcAppend
	    print("""
	You stand at the front door of a deserted inn.
	The slow creaking of the floor boards, the
	wind seeping through the closed window.
	""")
	    tempLoc = "locDesertedInn"

	def locDesertedInnKitchen():
	    global tempVar; global privPlayer_loc; global funcAppend
	    tempVar = privPlayer_loc + funcAppend
	    print("""
	The floor tiles are more of an assortment of
	broken glass on the floor, finding new shapes
	to take with each step you take.
	""")
	    tempLoc = "locDesertedInnKitchen"
	
	def locDesertedInnHallway():
	    tempVar = privPlayer_loc + funcAppend
	    print("""
	Small streaks of light illunimate the otherwise
	dim corridor. Doors with missing knobs, some
	hanging onto their hinges for dear life.
	
	Ahead of you is a staircase leading up.
	""")
	    tempLoc = "locDesertedInnHallway"

	def locDesertedInnLounge():
	    tempVar = privPlayer_loc + funcAppend
	    print("""
	Not a single ember glowing in the ashes of the
	fireplace. The seats and the couch are showing
	their age. The slight tinge of a moldy carpet
	hangs in the air.
	""")
	    tempLoc = "locDesertedInnLounge"
	
	def locDesertedInnDining():
	    global flashlight
	    tempVar = privPlayer_loc + funcAppend
	    print(f"""
	The table cloth is clean despite it being worn.
	The chairs and plates are neatly set in their 
	places. You wonder if the residents knew it was 
	the last time they would eat here.
	""")
	    tempLoc = "locDesertedInnDining"
	    if flashlight == True:
	        print("""		There is a flashlight here
	    """)
	 
	def locDesertedInn2ndFLHallway():
	    tempVar = privPlayer_loc + funcAppend
	    print("""
	 You're at the top of the stairs on the second 
	 floor. At the end of the hallway you hear a
	 strange noise coming from one of the rooms.
	     """)
	    tempLoc = "locDesertedInn2ndFLHallway"
	
	def locDesertedInn2ndFLHallway2():
	    tempVar = privPlayer_loc + funcAppend
	    print("""
	 The noise became a memory as the noise now 
	 rendered mute.
	     """)
	    tempLoc = "locDesertedInn2ndFLHallway2"
	
	def locDesertedInn2ndFLHallway3():
	    tempVar = privPlayer_loc + funcAppend
	    print("""
	 You stand outside Room 416, staples littering
	 the door. 
	     """)
	    tempLoc = "locDesertedInn2ndFLHallway3"

	def locDesertedInn2ndFLMysteryRoom():
	    global i
	    global p
	    global gameWin
	    global haveFlashlight
	    p.terminate()
	    tempVar = privPlayer_loc + funcAppend
	    if haveFlashlight == True:
	        print("""
	 	You turn on your flashlight and open
	 	the door slowly. A figure jumps out
	 	at you, but gets scared away by the
	 	light. It scurries away out of a
	 	broken window. 
	 	
	 	You illuminate the walls of the room
	 	that reveal the true nature of the
	 	evil behind this Inn.
	     """)
	        tempLoc = "locDesertedInn2ndFLMysteryRoom"
	        gameWin = 1
	        i = 0
	        
	    if haveFlashlight == False:
	        print("""
	 	You slowly open the door, the room appearing 
	 	as a dark void. You take a step inside and a 
	 	wave of uncertainty comes over you as you begin 
	 	to lose consciousness. You struggle to keep your 
	 	footing solid as you fall to the ground. 
	     """)
	        tempLoc = "locDesertedInn2ndFLMysteryRoom"
	        gameWin = 0
	        i = 0

	# Move 'Forward' Function
	def command1():
	    global map_roomT
	    global invalid_comm
	    global elseSKIP
	    global privPlayer_loc
	    global pubPlayer_loc
	    invalid_comm = 1
	    	    
	    # 2nd FL Hallway 2 to 2nd FL Hallway 3
	    if privPlayer_loc == "locDesertedInn2ndFLHallway2":
	    	privPlayer_loc = "locDesertedInn2ndFLHallway3"; pubPlayer_loc = "A Deserted Inn - 2nd Floor Hallway cont."
	    	map_roomT = ["[X]", "[*]", "[?]", "[X]", "[ ]", "[X]", "[X]", "[ ]", "[X]"]
	    	elseSKIP = 1
	    	clrscr(); hudTOP(); locDesertedInn2ndFLHallway3()
	    # 2nd FL Hallway to 2nd FL Hallway 2
	    if privPlayer_loc == "locDesertedInn2ndFLHallway":
	    	privPlayer_loc = "locDesertedInn2ndFLHallway2"; pubPlayer_loc = "A Deserted Inn - 2nd Floor Hallway cont."
	    	map_roomT = ["[X]", "[ ]", "[?]", "[X]", "[*]", "[X]", "[X]", "[ ]", "[X]"]
	    	elseSKIP = 1
	    	clrscr(); hudTOP(); locDesertedInn2ndFLHallway2()
	    # Hallway to 2nd FL Hallway
	    if privPlayer_loc == "locDesertedInnHallway":
	    	privPlayer_loc = "locDesertedInn2ndFLHallway"; pubPlayer_loc = "A Deserted Inn - 2nd Floor Hallway"
	    	map_roomT = ["[X]", "[ ]", "[?]", "[X]", "[ ]" , "[X]", "[X]", "[*]", "[X]"]
	    	elseSKIP = 1
	    	clrscr(); hudTOP(); locDesertedInn2ndFLHallway()
	    # Kitchen to hallway
	    if privPlayer_loc == "locDesertedInnKitchen":
	    	privPlayer_loc = "locDesertedInnHallway"; pubPlayer_loc = "A Deserted Inn - Hallway"
	    	map_roomT = ["[X]", "[*]", "[X]", "[X]", "[ ]", "[X]", "[ ]", "[ ]", "[?]"]
	    	elseSKIP = 1
	    	clrscr(); hudTOP(); locDesertedInnHallway()	
	    # Spawn to kitchen
	    if privPlayer_loc == "locDesertedInn":
	    	privPlayer_loc = "locDesertedInnKitchen"; pubPlayer_loc = "A Deserted Inn - Kitchen"
	    	map_roomT = ["[X]", "[^]", "[X]", "[X]", "[*]", "[X]", "[ ]", "[ ]", "[?]"]
	    	elseSKIP = 1
	    	clrscr(); hudTOP(); locDesertedInnKitchen()	
	    if elseSKIP == 0:
	        print("You can't move there.")
	
	
	# Move 'Back' Function
	def command2():
	    global map_roomT
	    global invalid_comm
	    global elseSKIP
	    global privPlayer_loc
	    global pubPlayer_loc
	    invalid_comm = 1
	    
	    # Kitchen to spawn
	    if privPlayer_loc == "locDesertedInnKitchen":
	    	privPlayer_loc = "locDesertedInn"; pubPlayer_loc = "A Deserted Inn"
	    	map_roomT = ["[X]", "[^]", "[X]", "[X]", "[ ]", "[X]", "[ ]", "[*]", "[?]"]
	    	elseSKIP = 1
	    	clrscr(); hudTOP(); locDesertedInn()
	    	
	    # Hallway to kitchen
	    if privPlayer_loc == "locDesertedInnHallway":
	    	privPlayer_loc = "locDesertedInnKitchen"; pubPlayer_loc = "A Deserted Inn - Kitchen"
	    	map_roomT = ["[X]", "[^]", "[X]", "[X]", "[*]", "[X]", "[X]", "[ ]", "[?]"]
	    	elseSKIP = 1
	    	clrscr(); hudTOP(); locDesertedInnKitchen()
	    	
	    # 2nd FL Hallway to Hallway
	    if privPlayer_loc == "locDesertedInn2ndFLHallway":
	    	privPlayer_loc = "locDesertedInnHallway"; pubPlayer_loc = "A Deserted Inn - Hallway"
	    	map_roomT = ["[X]", "[*]", "[X]", "[X]", "[ ]", "[X]", "[ ]", "[ ]", "[?]"]
	    	elseSKIP = 1
	    	clrscr(); hudTOP(); locDesertedInnHallway()
	    # 2nd FL Hallway 2 to Hallway '1'
	    if privPlayer_loc == "locDesertedInn2ndFLHallway2":
	    	privPlayer_loc = "locDesertedInn2ndFLHallway"; pubPlayer_loc = "A Deserted Inn - 2nd FL Hallway"
	    	map_roomT = ["[X]", "[ ]", "[?]", "[X]", "[ ]", "[X]", "[X]", "[*]", "[X]"]
	    	elseSKIP = 1
	    	clrscr(); hudTOP(); locDesertedInn2ndFLHallway()
	    	
	    # 2nd FL Hallway 3 to 2nd FL Hallway 2
	    if privPlayer_loc == "locDesertedInn2ndFLHallway3":
	    	privPlayer_loc = "locDesertedInn2ndFLHallway2"; pubPlayer_loc = "A Deserted Inn - 2nd FL Hallway cont."
	    	map_roomT = ["[X]", "[ ]", "[?]", "[X]", "[*]", "[X]", "[X]", "[ ]", "[X]"]
	    	elseSKIP = 1
	    	clrscr(); hudTOP(); locDesertedInn2ndFLHallway2()
	    if elseSKIP == 0:
	        print("You can't move there.")
	
	# Move 'Left' Function
	def command3():
	    global map_roomT
	    global invalid_comm
	    global elseSKIP
	    global privPlayer_loc
	    global pubPlayer_loc
	    invalid_comm = 1
	    
	    # Spawn to lounge
	    if privPlayer_loc == "locDesertedInn":
	    	privPlayer_loc = "locDesertedInnLounge"; pubPlayer_loc = "A Deserted Inn - Lounge"
	    	map_roomT = ["[X]", "[^]", "[X]", "[X]", "[ ]", "[X]", "[*]", "[ ]", "[?]"]
	    	elseSKIP = 1
	    	clrscr(); hudTOP(); locDesertedInnLounge()
	    # Dining to spawn
	    if privPlayer_loc == "locDesertedInnDining":
	    	privPlayer_loc = "locDesertedInn"; pubPlayer_loc = "A Deserted Inn"
	    	map_roomT = ["[X]", "[^]", "[X]", "[X]", "[ ]", "[X]", "[ ]", "[*]", "[?]"]
	    	elseSKIP = 1
	    	clrscr(); hudTOP(); locDesertedInn()
	    if elseSKIP == 0:
	        print("You can't move there.")
	 
	# Move 'Right' Function
	def command4():
	    global map_roomT
	    global invalid_comm
	    global elseSKIP
	    global privPlayer_loc
	    global pubPlayer_loc
	    invalid_comm = 1
	    # 2nd FL Hallway 3 to 2nd FL Mystery Room
	    if privPlayer_loc == "locDesertedInn2ndFLHallway3":
	    	privPlayer_loc = "locDesertedInn2ndFLMysteryRoom"; pubPlayer_loc = "A Deserted Inn - 2nd Floor - Strange Noise"
	    	map_roomT = ["[X]", "[ ]", "[*]", "[X]", "[ ]", "[X]", "[X]", "[ ]", "[X]"]
	    	elseSKIP = 1
	    	clrscr(); hudTOP(); locDesertedInn2ndFLMysteryRoom()
	    # Spawn to dining
	    if privPlayer_loc == "locDesertedInn":
	    	privPlayer_loc = "locDesertedInnDining"; pubPlayer_loc = "A Deserted Inn - Dining Room"
	    	map_roomT = ["[X]", "[^]", "[X]", "[X]", "[ ]", "[X]", "[ ]", "[ ]", "[*]"]
	    	elseSKIP = 1
	    	clrscr(); hudTOP(); locDesertedInnDining()
	    # Lounge to spawn
	    if privPlayer_loc == "locDesertedInnLounge":
	    	privPlayer_loc = "locDesertedInn"; pubPlayer_loc = "A Deserted Inn"
	    	map_roomT = ["[X]", "[^]", "[X]", "[X]", "[ ]", "[X]", "[ ]", "[*]", "[?]"]
	    	elseSKIP = 1
	    	clrscr(); hudTOP(); locDesertedInn()
	    if elseSKIP == 0:
	        print("You can't move there.")
	
	    # Take Command
	def command5():
	    global invalid_comm
	    global takeCheck
	    global user_input
	    global haveFlashlight
	    global flashlight
	    global elseSKIP
	    invalid_comm = 1
	    elseSKIP = 0
	    takeList = ["take"]
	    for sub in takeList:
	    	user_input = user_input.replace(sub, '')
	    	user_input = (user_input[1:])
	    if user_input == 'flashlight':
	    	if flashlight == True:
	    	    flashlight = False
	    	    haveFlashlight = True
	    	    print(f"{user_input} taken.")
	    elif user_input == flashlight:
	    	if flashlight == False:
	    	    print(f"There is no {user_input} here.")
	    else:
	    	print("That object is not here.")
	    if user_input == '':
	        print("""	    Take: Used to take items from the environment
	    
	    Usage: Type 'take' followed by the name of
	    the item you wish to take.
	    
	    Type this: take flashlight
	        """)
	    
	    	    # Inventory Command
	def command6():
	    global invalid_comm
	    invalid_comm = 1
	    print("Items:")
	    if haveFlashlight == True:
	    	print("Flashlight")
	    print("")
	
	# Move Command Function
	def command7():
	    global invalid_comm
	    global moveCheck
	    global user_input
	    invalid_comm = 1
	    moveList = ["move"]
	    for sub in moveList:
	    	user_input = user_input.replace(sub, '')
	    	user_input = (user_input[1:])
	    if user_input == '' or user_input == ' ' or user_input == '   ':
	        print("You need a direction. See help command.\n") 
	    if user_input == 'forward':
	    	command1()
	    if user_input == 'back':
	    	command2()
	    if user_input == 'left':
	    	command3()
	    if user_input == 'right':
	    	command4()
	    if user_input == '':
	        print("""	    Move: Used to navigate the environment
	        
	    Usage: Type 'move' followed by 'forward',
	    	'back', 'left', or 'right'.
	    
	    Type this: move right, move forward, etc.
	        """)
	
	def debug_menu():
	    global invalid_comm
	    invalid_comm = 1
	    print(f"""
	    Debug Menu:
	    	Version Number: {version_number}
	    	
	    	More debugging information and options coming soon.
	    """)
	    debug_menu_prompt = input("Press ENTER to return to the game.\n")
	    
	def exit_program_confirm():
	    global invalid_comm
	    invalid_comm = 1
	    p.terminate()
	    print("""
	        
	            Are you sure you want to exit?
	       	                (y/n)
	       """)
	    leaveVAR = input("Exit? #>")
	    if leaveVAR =="y":
	        print("Leaving")
	        exit()
	    if leaveVAR == "n":
	        print("Not Leaving")
	        
	def look_command():
	    global invalid_comm
	    global privPlayer
	    room = privPlayer_loc
	    invalid_comm = 1
	    if room == "locDesertedInn":
	        print(roomdesc.desertedInn[7], "\n")
	    if room == "locDesertedInnKitchen":
	        print(roomdesc.desertedInn[4], "\n")

	commands = {
	    #'move forward' : command1,
	    #'move backward' : command2,
	    #'move left' : command3,
	    #'move right' : command4,
	    'take'	: command5,
	    'inventory'	: command6,
	    'move'	: command7,
	    'debug'	: debug_menu,
	    'exit'	: exit_program_confirm,
	    'look'	: look_command
	}
	
	def variableReset():
	    global health
	    global maxhealth
	    global money
	    global player
	    global privPlayer_loc
	    global pubPlayer_loc
	    global gotoLoc
	    global flashlight
	    global haveFlashlight
	    global takeCheck
	    global moveCheck
	    global funcAppend
	    global playerInventory
	    global itemAppend
	    global localItems
	    global locDesertedInnDiningItems
	    global tempLoc
	    global map_roomT
	    
	    health = "?"
	    maxhealth = "?"
	    money = 0
	    playername = "Unknown"
	    privPlayer_loc = "locDesertedInn"
	    pubPlayer_loc = "A Deserted Inn"
	    gotoLoc = "locations[privPlayer_loc]"
   #items
	    flashlight = True
	    haveFlashlight = False
	    takeCheck = 'take'
	    moveCheck = 'move'
	    funcAppend = '()'
	    playerInventory = ['']

 # Map Variables
	    map_roomT = ["[X]", "[^]", "[X]", "[X]", "[ ]", "[X]", "[ ]", "[*]", "[?]"]

 # Location Items
	    itemAppend = str('Items')
	    localItems = ''
	    locDesertedInnDiningItems = ['flashlight', 'axe']
	    tempLoc = privPlayer_loc
	    
	def play(sound_file):
	    global player
	    if player is not None:
	        play.stop
	
	
	while at_menu == True:
	    clrscr()
	    try:
	        p.start()
	        print(f"""\n\n\n\n\n\n\n\n			        Wanderer
	        	        ({version_number}) 
	        			
	          "How can one become free when being
	             a prisoner is a human right?"
	             
	                  <Press ENTER to start>
	                   <Type quit to exit>
	        """)
	        cont = input("				> ")
	        if cont == "":
	            p.terminate()
	            at_menu = False
	        if cont == "quit":
	            p.terminate
	            exit()
	        p.terminate()
	    except KeyboardInterrupt:
	        p.terminate()
	        print("""
	        
             Are you sure you want to quit?
             	          (y/n)
             
	        """)
	        cont = input("#> ")
	        if cont == "y":
	            print("Leaving")
	            exit()
	        if cont == "n":
	            print("Not leaving")
	    except ValueError:
	        print("value error")  	        
	    
	        	   	            
	        
	
	while startup == True:
	    clrscr()
	    try:
	        print("""
	    You wake up inside what seems to be an old Inn.
	    A cold breeze is crawling around the room. You
	    look around and see a lounge to your left, the 
	    kitchen ahead of you, and the dining room on
	    to your right. 
	    
	    "How did I get here?" you ask yourself. A
	    question that seems to be too common nowadays.
	    
	    "Better yet," you think, "What's my name?"
	    How come you can't remember? "My name...
	    My name..."
	    """)
	        playername = input('"It has to be ')
	        clrscr()
	        hudTOP()
	        locDesertedInn()
	        print("Type 'help' for a list of commands")
	        print("")
	        startup = False
	        p = multiprocessing.Process(target=playsound, args=("music/ambient_wind.mp3",))
	        p.start()
	    except KeyboardInterrupt:
	            p.terminate()
	            print("""
	        
	             Are you sure you want to exit?
	        	         (Y/N)
	            """)
	            leaveVAR = input("?>")
	            if leaveVAR == "y":
	                exit()
	            if leaveVAR == "n":
	                startup = True
	
	def inputscreen():
		global firstInvalid
		global invalid_comm
		global user_input
		try:
		    user_input = input(f"{playername}#> "); 
		    if user_input == 'help':
		        commands_help()
		    if user_input in commands:
		        func = commands[user_input]
		        func()
		    # You could also shorten this to:
		    # commands[user_input]()
		    if takeCheck in user_input:
		        command5()
		    if moveCheck in user_input:
		        command7()
		    if invalid_comm == 0: # if the user doesn't type in a valid command
		        if firstInvalid == False: # and if it's not the first wrong command
		            print("Invalid Command.\n") # print Invalid Command to screen
		    if invalid_comm == 0:
		        if firstInvalid == True:
		            print("Invalid Command. Type 'help' for the list of commands.\n")
		            firstInvalid = False
		except EOFError as e:
		    print("\nNon-game function not allowed.")
		except:
		    print("\nNon-game function not allowed.")
	
	while i == 1:
	    elseSKIP = 0
	    invalid_comm = 0
	    inputscreen()
	if gameWin == 0:
	    input("Game Over. Press ENTER to restart.")
	    i = 1
	    startup = True
	
	if gameWin == 1:
	    input("You lived to tell the tale. Press ENTER to restart.")
	    i = 1
	    startup = True
	variableReset()
