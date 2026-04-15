import time

proceed = True
go = True
choice = 0
t_start = 0
t_end = 0
t_total = 0
name = None 


def BOLDFACE_ABORT():
    global proceed
    print("ABORT")
    ans1 = input("1:")
    if ans1 != 'RELEASE - PULL TWICE':
        print("Incorrect!")
        proceed = False
        return proceed
    else:
        print("Correct!")
        proceed = True
        return proceed
        
def BOLDFACE_ROPEBREAK():
    global proceed
    print("ROPE BREAK")
    ans1 = input("1:")
    ans2 = input("2:")
    if ans1 != 'GLIDE - ESTABLISH' or ans2 != 'RELEASE - PULL TWICE':
        print("Incorrect!")
        proceed = False
        return proceed
    else:
        print("Correct!")
        proceed = True
        return proceed
    
def BOLDFACE_PI():
    global proceed
    print("PHYSIOLOGICAL INCIDENT")
    ans1 = input("1:")
    ans2 = input("2:")
    if ans1 != 'MODE SELECTOR SWITCH - F4' or ans2 != 'DESCEND - IMMEDIATELY':
        print("Incorrect!")
        proceed = False
        return proceed
    else:
        print("Correct!")
        proceed = True
        return proceed

def BOLDFACE_UPRIGHTSPINRECOVERY():
    global proceed
    print("UPRIGHT SPIN RECOVERY")
    ans1 = input("1:")
    ans2 = input("2:")
    ans3 = input("3:")
    ans4 = input("4:")
    if ans1 != 'AILERONS - NEUTRAL' or ans2 != 'RUDDER - FULL OPPOSITE DIRECTION OF SPIN AND HOLD' or ans3 != 'STICK - STEADILY FORWARD UNTIL SPINNING STOPS' or ans4 != 'CONTROLS - NEUTRAL AND RECOVER FROM DIVE':
        print("Incorrect!")
        proceed = False
        return proceed
    else:
        print("Correct!")
        proceed = True
        return proceed
    
def OPSLIMITS_PM():
    global proceed
    print("PROHIBITED MANEUVERS")
    ans1 = input("1:")
    ans2 = input("2:")
    if ans1 != 'IMC FLIGHT' or ans2 != 'NIGHT FLIGHT':
        print("Incorrect!")
        proceed = False
        return proceed
    else:
        print("Correct!")
        proceed = True
        return proceed
    
def OPSLIMITS_GLIMITS():
    global proceed
    print("G LIMITS")
    ans1 = input("At Va, Acro (<= 1389 lbs):")
    ans2 = input("At Vne, Acro (<= 1389 lbs):")
    ans3 = input("Airbrakes at Vne, Acro (<= 1389 lbs):")
    ans4 = input("At Va, Utility (> 1389 lbs):")
    ans5 = input("At Vne, Utility (> 1389 lbs):")
    ans6 = input("Airbrakes at Vne, Utility (> 1389 lbs):")
    if ans1 != '7.0/-5.0' or ans2 != '7.0/-5.0' or ans3 != '3.5/0' or ans4 != '5.3/-2.6' or ans5 != '4.0/-1.5' or ans6 != '3.5/0':
        print("Incorrect!")
        proceed = False
        return proceed
    else:
        print("Correct!")
        proceed = True
        return proceed
    
def OPSLIMITS_AIRSPEEDS():
    global proceed
    print("AIRSPEEDS (KIAS), Dual @1389 lbs:")
    ans1 = input("Speed at Max L/D:")
    ans2 = input("Minimum Sink Speed:")
    ans3 = input("Stall Speed - Wings Level - Vs:")
    if ans1 != '61' or ans2 != '50' or ans3 != '40':
        print("Incorrect!")
        proceed = False
        return proceed
    else:
        print("Correct!")
        proceed = True
        return proceed
    
def OPSLIMITS_WINDCON():
    global proceed
    print("WIND LIMITATIONS")
    ans1 = input("Max Wind for Takeoff:")
    ans2 = input("Max Crosswind Component:")
    ans3 = input("Max Gust Factor for Takeoff:")
    if ans1 != '25' or ans2 != '16' or ans3 != '10':
        print("Incorrect!")
        proceed = False
        return proceed
    else:
        print("Correct!")
        proceed = True
        return proceed
    
def OPSLIMITS_AIRSPEEDLIMIT():
    global proceed
    print("AIRSPEED LIMITATIONS")
    ans1 = input("Maximum Glide or Dive - Vne (< 10,000 MSL):")
    ans2 = input("Maximum Glide or Dive - Vne (<= 10,000 MSL):")
    ans3 = input("Maneuvering Airspeed - Va / Rough Airspeed - Vra:")
    ans4 = input("Max Aerotow - Vt:")
    if ans1 != '146' or ans2 != '138' or ans3 != '100' or ans4 != '100':
        print("Incorrect!")
        proceed = False
        return proceed
    else:
        print("Correct!")
        proceed = True
        return proceed
    
def OPSLIMITS_PATTERNAIRSPEED():
    global proceed
    print("PATTERN AIRSPEED:")
    ans1 = input("__ KIAS Min:")
    ans2 = input("+ __ Max Wind Velocity (excluding tailwinds):")
    if ans1 != '54' or ans2 != '1/2':
        print("Incorrect!")
        proceed = False
        return proceed
    else:
        print("Correct!")
        proceed = True
        return proceed


name = input("ENTER YOUR NAME (LAST, FIRST):")

t_start = time.perf_counter()

while go == True:
    if proceed == True:
        choice = choice + 1
        
    if choice == 1 and proceed == True:
        BOLDFACE_UPRIGHTSPINRECOVERY()
    elif choice == 2 and proceed == True:
        BOLDFACE_ROPEBREAK()
    elif choice == 3 and proceed == True:
        BOLDFACE_ABORT()
    elif choice == 4 and proceed == True:
        BOLDFACE_PI()
    elif choice == 5 and proceed == True:
        OPSLIMITS_PM()
    elif choice == 6 and proceed == True:
        OPSLIMITS_GLIMITS()
    elif choice == 7 and proceed == True:
        OPSLIMITS_AIRSPEEDS()
    elif choice == 8 and proceed == True:
        OPSLIMITS_WINDCON()
    elif choice == 9 and proceed == True:
        OPSLIMITS_AIRSPEEDLIMIT()
    elif choice == 10 and proceed == True:
        OPSLIMITS_PATTERNAIRSPEED()
    
        
        
    if proceed == False:
        if choice == 1:
            BOLDFACE_UPRIGHTSPINRECOVERY()
        elif choice == 2:
            BOLDFACE_ROPEBREAK()
        elif choice == 3:
            BOLDFACE_ABORT()
        elif choice == 4:
            BOLDFACE_PI()
        elif choice == 5:
            OPSLIMITS_PM()
        elif choice == 6:
            OPSLIMITS_GLIMITS()
        elif choice == 7:
            OPSLIMITS_AIRSPEEDS()
        elif choice == 8:
            OPSLIMITS_WINDCON()
        elif choice == 9:
            OPSLIMITS_AIRSPEEDLIMIT()
        elif choice == 10:
            OPSLIMITS_PATTERNAIRSPEED()
    
    if choice == 11:
        t_end = time.perf_counter()
        t_total = t_end - t_start
        mins, secs = divmod(t_total,60)
        print("BOLDFACE AND OPS LIMITS COMPLETE!!")
        print(f"TIME ELAPSED: {int(mins)} MINUTES AND {secs:.2f} SECONDS")
        quit()
    
    