# EXERCISE 1 - PYTHON ENVIRONMENT
import sys #Python module that provides information about the Python interpreter and its execution environment.
import platform  #provides information about your operating system and hardware platform.

print("Python Environment Information")

print("Python Version:", sys.version)
print("Python Executable:", sys.executable)
print("Operating System:", platform.system())



# EXERCISE 2 - FIFO PROJECT INFORMATION
project_name = "Asynchronous FIFO"
language = "Verilog"
depth = 8
width = 8
simulator = "SimVision"

print("FIFO Project Information")
print("Project Name:", project_name)
print("Design Language:", language)
print("FIFO Depth:", depth)
print("Data Width:", width, "bits")
print("Simulator:", simulator)



#Exercise 5 — Formatting
print("FIFO", "Verilog", "SimVision") #normal print statement
print("FIFO", "Verilog", "SimVision", sep=" | ")  #print with seperator

#want same line output, use end parameter
print("Hello", end=" ")
print("World")


