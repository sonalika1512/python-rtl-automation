# EXERCISE 1 - IF ELSE
depth = 8

if depth == 16:
    print("Maximum FIFO depth configured")

else:
    print("FIFO has not reached maximum depth")


# EXERCISE 2 - IF ELSE
fifo_full = True

if fifo_full:
    print("FIFO is FULL")

else:
    print("FIFO is NOT FULL")


# EXERCISE 3 - IF ELIF ELSE
depth = 16

if depth == 8:
    print("Small FIFO")

elif depth == 16:
    print("Medium FIFO")

elif depth == 32:
    print("Large FIFO")

else:
    print("Unsupported FIFO configuration")


# EXERCISE 4 - NESTED IF
depth = 8
width = 16

if depth == 8:

    print("FIFO depth is valid")

    if width == 8:
        print("FIFO width is valid")
        print("Configuration is correct")

    else:
        print("FIFO width is incorrect")

else:
    print("FIFO depth is incorrect")