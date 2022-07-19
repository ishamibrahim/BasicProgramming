

def tower_of_hanoi(num_of_disks, tow_1, tow_2, tow_3):
    if num_of_disks > 0:
        tower_of_hanoi(num_of_disks-1, tow_1, tow_3, tow_2)
        print("Move disk from {} to {}".format(tow_1, tow_2))
        tower_of_hanoi(num_of_disks - 1, tow_3, tow_2, tow_1)


if __name__ == "__main__":
    num_of_disks = 6
    tower_of_hanoi(num_of_disks, "A", "C", "B")
