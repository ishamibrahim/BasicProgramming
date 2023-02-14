"""
Given two integer lists corresponding to the servers numbered on the index
One list shows  power required for server to boot
Another list power required during processing
With the formula given for net_power, group max number of servers to a cluster so that the net_power < max_power
"""


class Sol:
    @staticmethod
    def find_max_computer_group_size(processing_power, booting_power, max_power):
        max_group_size = 0
        len_servers = len(processing_power)
        group_size = 0
        while group_size < len_servers:
            group_size += 1
            is_size_changed = False
            for start in range(len_servers):
                net_power = max(booting_power[start: start + group_size]) + (sum(processing_power[start: start + group_size]) * group_size)
                if net_power <= max_power:
                    max_group_size = group_size
                    is_size_changed = True
                    break
                if start > len_servers - group_size:
                    break
            if not is_size_changed or not (len_servers - group_size):
                break

        return max_group_size


print(Sol.find_max_computer_group_size([2, 1, 3, 4, 5], [3, 6, 1, 3, 4], 25))

