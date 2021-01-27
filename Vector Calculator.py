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
    distance = []
    time = []
    user = int(input("How many inputs? "))
    print("Enter the distance followed by time like so: \nx \ny")
    #collects data
    for _ in range(user):
        n += 1
        print(f"Input {n}:")
        get_distance = float(input())
        distance.append(get_distance)
        get_time = float(input())
        time.append(get_time)
    #runs calculations
    slopes = [float(m) / float(s) for m,s in zip(distance, time)]
    rounded_slopes = [round(elem, 2) for elem in slopes]
    #prints results
    print("Distance inputs:{}m".format(distance))
    print("Time inputs:    {}s".format(time))
    print("Slopes:         {}m/s".format(rounded_slopes))

#acceleration function
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

#compare accelerations
def comparing_accel():
    n = 0
    vi = []
    vf = []
    time = []
    user = int(input("How many inputs? "))
    print("Enter your date like so: \nvi \nvf \nt")
    #collects data
    for _ in range(user):
        n += 1
        print(f"Input{n}")
        get_vi = float(input())
        vi.append(get_vi)
        get_vf = float(input())
        vf.append(get_vf)
        get_time = float(input())
        time.append(get_time)
        print()
    #calculates data
    avgV = [float(f) - float(i) for f,i in zip(vf, vi)]
    accel = [float(v) / float(s) for v,s in zip(avgV, time)]
    rounded_accel = [round(a, 2) for a in accel]
    #prints results
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
