"""
A streaming service wants to join family ids together for audit purposes. from a list of string usernames, An user is said to be
related if there is another username whose letters are +1 or -1 to them
example : if user - abc, then bcd and zab are related

Find number of relations.
"""


class Sol:
    def get_new_words(self, old_word):
        new_word_pos = new_word_neg = ""
        for ctr in old_word:
            new_num_pos = ord(ctr) + 1
            new_word_pos += chr(self.get_normalized_position(new_num_pos))
            new_num_neg = ord(ctr) - 1
            new_word_neg += chr(self.get_normalized_position(new_num_neg))
        return new_word_pos, new_word_neg

    def get_normalized_position(self, old_num_position):
        if old_num_position > 122:
            new_num_position = 97
        elif old_num_position < 97:
            new_num_position = 122
        else:
            new_num_position = old_num_position
        return new_num_position

    def count_family_logins(self, logins):
        family_accounts = 0
        for name_index in range(len(logins)-1):
            remaining_names = logins[name_index + 1:]
            name = logins[name_index]
            pos_name, neg_name = self.get_new_words(name)

            if pos_name in remaining_names:
                family_accounts += remaining_names.count(pos_name)
            if neg_name in remaining_names:
                family_accounts += remaining_names.count(neg_name)
        return family_accounts


s = Sol()
print(s.count_family_logins(['ab', 'bc', 'zz', 'aa', 'bb', 'cc', 'cc', 'cc', 'aa']))


