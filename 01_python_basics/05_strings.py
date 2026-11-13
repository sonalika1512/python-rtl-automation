module_name = "async_fifo"
language = 'Verilog'
message = """Welcome to Python RTL Automation"""

print(module_name)
print(language)
print(message)

#string indexing 
module_name = "FIFO"

print(module_name[0])
print(module_name[1])
print(module_name[2])
print(module_name[3])

#negative indexing
module_name = "FIFO"

print(module_name[-1]) #last character
print(module_name[-2]) #second last character


#string slicing
module_name = "async_fifo"

print(module_name[0:5])
print(module_name[6:10])
print(module_name[:5])
print(module_name[6:])
print(module_name[:])


#other slicing operations 
name = "VERILOG"

print(name[::2])  #VRLG
print(name[::-1])  #GOLIREV


#uppercase and lowercase conversion
signal = "wr_clk"

print(signal.upper())
print(signal.lower())
print(signal.capitalize())
print(signal.title())
print(signal.swapcase())


#remove spaces from stiing 
message = "   Simulation Passed   "

print(message.strip()) # remove from both sides 
print(message.lstrip()) # remove from left side
print(message.rstrip()) # remove from right side


#searching inside string 
log_message = "ERROR: FIFO overflow detected"
position = log_message.find("overflow")
print(position)


#more methods - join, replace, concatenate, split, f-strings




# RTL Simulation Log Analyzer
# Step 1: Store sample simulation log
log_data = """
INFO: Simulation started
INFO: FIFO reset completed
WARNING: FIFO almost full
ERROR: FIFO overflow detected
INFO: Test 1 passed
ERROR: Read operation failed
INFO: Simulation completed
"""

# Step 2: Convert the complete log into individual lines
log_lines = log_data.splitlines()

# Step 3: Create counters
error_count = 0
warning_count = 0
pass_count = 0

# Step 4: Read every line
for line in log_lines:
    # Remove unnecessary spaces
    line = line.strip()
    # Ignore empty lines
    if line == "":
        continue
    # Check for errors
    if "ERROR" in line:
        error_count += 1
        print("Error found:", line)
    # Check for warnings
    elif "WARNING" in line:
        warning_count += 1
        print("Warning found:", line)
    # Check for passed tests
    elif "passed" in line.lower():
        pass_count += 1
        print("Test passed:", line)

# Step 5: Generate summary
print("\n----- SIMULATION SUMMARY -----")
print(f"Errors   : {error_count}")
print(f"Warnings : {warning_count}")
print(f"Passed   : {pass_count}")

if error_count == 0:
    print("Overall Status: PASS")
else:
    print("Overall Status: FAIL")
