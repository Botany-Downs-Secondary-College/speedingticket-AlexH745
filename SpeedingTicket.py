name=""
vehicle_speed=0.00
limit_speed=0.00
difference=0.00
fine=0.00
warrant_list = ["Anson","Alex","Solomon"]


#function
def calculatefine(vehicle_speed, limit_speed):
    difference = vehicle_speed - limit_speed
    fine= difference*10
    if difference > 0:
        if difference > 50:
            if difference < 75:
                print(name, "You loose license")
            else:
                print(name, "You are going to jail")
        else:
            print(name, "The fine is {}".format(fine))
    else:
        print("You are driving under speed limit")
       
while name=="":
    name=input("Enter your name")
    if name in warrant_list:
      print(name,"IS WANTED FOR ARREST")

   
vehicle_speed=float(input("Enter your vehicle speed"))
limit_speed= float(input("Enter speed limit"))

# calling function
calculatefine(vehicle_speed, limit_speed)
