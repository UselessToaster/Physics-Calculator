### calculates physics for you ###

#speed function
def speed():
    distance = float(input("How far did you travel? "))
    timeS = float(input("How long did it take? "))
    speed = distance/timeS
    print("{:,.3f}".format(speed))

#velocity function
def velocity():
    xi = float(input("What is your initial position? "))
    xf = float(input("What is your final position? "))
    time = float(input("How long did it take? "))
    displacement = xf - xi
    velocity = displacement/time
    print("{:,.3f}".format(velocity))

#compare slopes 
def compare_slopes():
    n = 0
    i = 0
    distance = []
    time = []
    user = int(input("How many inputs? "))
    for _ in range(user):
        n += 1
        get_distance = float(input(f"Enter meter input {n}: "))
        distance.append(get_distance)
    for _ in range(user):
        i += 1
        get_time = float(input(f"Enter time input {i}: "))
        time.append(get_time)
    slopes = [float(m) / float(s) for m,s in zip(distance, time)]
    rounded_slopes = [round(elem, 2) for elem in slopes]
    print("Distance inputs:", distance)
    print("Time inputs:", time)
    print("Slopes in order of entry: ", rounded_slopes)

def acceleration():
    user = input("Do you have your initial and final velocity? (Y/N) " ).upper().strip()
    print()
    if user == "Y":
        vi = float(input("Initial velocity: "))
        vf = float(input("Final velocity: "))
    else: 
        print("*initial velocity*")
        vi = velocity()
        print("------")
        print("final velocity*")
        vf = velocity()
    time = float(input("Time: "))
    acceleration = (vf - vi)/time
    print("Your acceleration is: {:.2f}m/s^2".format(acceleration))

def comparing_accel():
    n = 0
    i = 0
    x = 0
    vi = []
    vf = []
    time = []
    user = int(input("How many inputs? "))
    for _ in range(user):
        n += 1
        get_vi = float(input(f"Enter initial velocity {n}: "))
        vi.append(get_vi)
        print("------")
    for _ in range(user):
        x += 1
        get_vf = float(input(f"Enter final velocity {x}: "))
        vf.append(get_vf)
        print("------")
    for _ in range(user):
        i += 1
        get_time = float(input(f"Enter time input {i}: "))
        time.append(get_time)
        print("------")
    avgV = [float(f) - float(i) for f,i in zip(vf, vi)]
    accel = [float(a) / float(s) for a,s in zip(avgV, time)]
    rounded_accel = [round(a, 2) for a in accel]
    print("Initial Velocity: {}m/s".format(vi))
    print("Final Velocity:   {}m/s".format(vf))
    print("Time:             {}s".format(time))
    print("Acceleration:     {}m/s^2".format(rounded_accel))
    
    
    


#lists possible actions and gets user input
print("""FUNCTIONS:
- speed
- velocity
- compare slopes
- acceleration
- compare accel
""")
user = input("What function do you need? ")

if user == "speed":
    print()
    speed()
elif user == "velocity":
    print()
    velocity()
elif user == "compare slopes":
    print()
    compare_slopes()
elif user == "acceleration":
    print()
    acceleration()
elif user == "compare accel":
    print()
    comparing_accel()

