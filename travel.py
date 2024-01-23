# TripPlanner V1.0

# Welcome function
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

# Rounding the estimated time function
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

# Destination setup function
def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

# Calling the welcome function
trip_planner_welcome("James")

# Calling the estimated_time_rounded function and store it in a variable
estimate = estimated_time_rounded(3.5)

# Calling the Destination setup function - passing estimate from the estimated time function as an argument
destination_setup("Budapest", "Seoul", estimate, "Plane")
