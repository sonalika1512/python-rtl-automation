# DAY 2 - VARIABLES AND DATA TYPES

# EXERCISE 1 - VARIABLE CREATION
depth = 8
print(depth)


# EXERCISE 2 - DATA TYPES
depth = 8
clock_period = 10.5
simulator = "SimVision"
simulation_passed = True

print("Depth:", type(depth))
print("Clock Period:", type(clock_period))
print("Simulator:", type(simulator))
print("Simulation Status:", type(simulation_passed))


# EXERCISE 3 - TYPE CONVERSION
depth = 8

# Integer to string
depth_text = str(depth)
print("Integer to String:", depth_text)
print("New Type:", type(depth_text))


# String to integer
depth_string = "16"
depth_number = int(depth_string)
print("String to Integer:", depth_number)
print("New Type:", type(depth_number))


# Integer to float
frequency = 100
frequency_float = float(frequency)
print("Integer to Float:", frequency_float)
print("New Type:", type(frequency_float))



# EXERCISE 4 - ARITHMETIC OPERATORS
depth = 8
width = 8

# Multiplication
capacity = depth * width
print("FIFO Capacity:", capacity, "bits")

# Division
capacity_bytes = capacity / 8
print("Capacity in Bytes:", capacity_bytes)

# Floor Division
whole_bytes = capacity // 8
print("Whole Bytes:", whole_bytes)

# Modulus
remainder = depth % 2
print("Remainder:", remainder)

# Address Width
depth = 16
addr_width = (depth - 1).bit_length()
print("Address Width:", addr_width)



# EXERCISE 5 - COMPARISON OPERATORS
depth = 8
width = 8

print("Depth equals 8:", depth == 8)
print("Depth not equal to 16:", depth != 16)
print("Depth greater than 4:", depth > 4)
print("Width less than 16:", width < 16)
print("Depth greater than or equal to 8:", depth >= 8)


# EXERCISE 6 - LOGICAL OPERATORS

depth = 8
width = 8

valid_depth = depth == 8
valid_width = width == 8
valid_configuration = valid_depth and valid_width

print("Valid Depth:", valid_depth)
print("Valid Width:", valid_width)
print("Valid Configuration:", valid_configuration)

# OR example
print("At least one condition is true:",
      depth == 8 or width == 16)


# NOT example
fifo_full = False
print("FIFO is not full:", not fifo_full)




# EXERCISE 8 - USER INPUT
#input() used to take a input from user and that input is always in form of string so we convert it into integer using int(
depth = int(input("Enter FIFO depth: ")) 
width = int(input("Enter FIFO data width: "))
capacity = depth * width

print("\nFIFO CONFIGURATION")
print("Depth:", depth)
print("Width:", width)
print("Capacity:", capacity, "bits")



# ==================================================
# DAY 2 - MINI PROJECT
# FIFO CONFIGURATION CALCULATOR
# ==================================================

#user input for FIFO depth and width
depth = int(input("Enter FIFO depth: "))
width = int(input("Enter FIFO data width: "))
#calculate capacity in bits and bytes
capacity = depth * width
capacity_bytes = capacity // 8
# CALCULATE ADDRESS WIDTH
addr_width = (depth - 1).bit_length()
#CHECK CONFIGURATION
expected_depth = 8
expected_width = 16
valid_configuration = (
    depth == expected_depth
    and width == expected_width
)

# DISPLAY PROJECT REPORT
print("\n========== FIFO PROJECT REPORT ==========")
print(f"FIFO Depth: {depth}")
print(f"Data Width: {width} bits")
print(f"Address Width: {addr_width}")
print(f"Total Capacity: {capacity} bits")
print(f"Capacity in Bytes: {capacity_bytes}")
print(f"Configuration Valid: {valid_configuration}")
print("==========================================")
