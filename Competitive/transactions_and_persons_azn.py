"""
Given a list of strings, consisting of the pattern -->  sender receiver amount
Return users who have more than the threshold number of transactions

"""
class Sol:
    def increment_person_count(self, sender, receiver, person_dict):
        if sender != receiver:
            people_list = (sender, receiver)
        else:
            people_list = (sender,)
        for person in people_list:
            person_dict[person] = person_dict[person] + 1 if person_dict.get(person, None) else 1


    def process_logs(self, logs, threshold):
        person_dict = dict()
        for log_line in logs:
            sender, receiver, _ = log_line.split(" ")
            self.increment_person_count(sender, receiver, person_dict)

        print(person_dict)
        over_transaction_users = [person for person, count in person_dict.items() if count >= threshold]

        return sorted(over_transaction_users)
s = Sol()
print(s.process_logs(["3 5 13", "5 2 567", "3 5 278" ], 2))