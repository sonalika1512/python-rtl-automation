# EXERCISE 1 - FOR LOOP
for i in range(5):
    print("Hello Python")

# EXERCISE 2 - FIFO TEST CASE GENERATION
for i in range(1, 11):
    print(f"FIFO Test Case {i}")

# EXERCISE 3 - while loop
i = 0
while i < 5:
    print("Hello Python")
    i += 1


#FOR LOOP WITH BREAK (exiting the loop)
for i in range(1, 11):
    if i == 5:
        break
    print(i)


#FOR LOOP WITH CONTINUE (skipping the iteration)
for test in range(1, 11):
    if test == 5:
        continue
    print(f"Running FIFO Test {test}")


