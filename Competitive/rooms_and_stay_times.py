"""
Given a set of rooms N. And an array of tenants who come at increasing intervals of time with
random stay times. If the rooms are provided in a first come first serve basis.
Which is the most occupied room

"""

NUM_OF_ROOMS = 10
customer_list = [(1, 20), (3, 3), (5, 2), (6, 3), (19, 1)]

room_list = []
occupied_list = []
class Room:
    def __init__(self):
        self.end_time


for customer in customer_list:
    start_time, duration = customer
    room_found = False

    for room_no in range(len(room_list)):
        if room_list[room_no] < start_time:
            room_list[room_no] = start_time + duration
            occupied_list[room_no] += 1
            room_found = True
            break

    if not room_found:
        room_list.append(start_time + duration)
        occupied_list.append(1)
ocupied_max_count = max(occupied_list)
occupied_max_room = occupied_list.index(ocupied_max_count)

print(ocupied_max_count, occupied_max_room)



