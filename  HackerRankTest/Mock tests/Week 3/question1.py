
def truckTour(petrolpumps):
    total_petrol = 0
    start_index = 0
    petrol_deficit = 0

    for i in range(len(petrolpumps)):
        petrol, distance = petrolpumps[i]
        total_petrol += petrol - distance
        if total_petrol < 0:
            start_index = i + 1
            petrol_deficit += total_petrol
            total_petrol = 0

    if total_petrol + petrol_deficit >= 0:
        return start_index
    else:
        return -1  # If no solution exists


# Test the function with sample input
petrolpumps = [
    (1, 5),
    (10, 3),
    (3, 4)
]
print(truckTour(petrolpumps))  # Output should be 1

