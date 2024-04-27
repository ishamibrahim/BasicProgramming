from datetime import datetime


class Sol:
    # For additional verification
    total_val = ""
    """
        Time: 15 mins
        Find the count of carried numbers during the addition of two input numbers
        Ex. 142 + 87 :
                2 + 7 = 9 --> No carry numbers
                4 + 8 = 12 -> 2 in place, 1 carried to the next digit
                1 + 0 + 1(Carried from previous  digit) = 2 --> No carry numbers
                In this example the answer is 1.

    """
    def number_of_carry_operations2(self, num1: int, num2: int):
        carriage_count = 0

        str_num1 = str(num1)
        str_num2 = str(num2)

        len1 = len(str_num1)
        len2 = len(str_num2)

        max_len = max(len1, len2)
        position_counter = 1
        carriage = 0

        while True:
            last_sum = 0
            if position_counter > max_len:
                break
            if position_counter <= len1 and position_counter <= len2:
                last_sum = int(str_num1[-position_counter]) + int(str_num2[-position_counter]) + carriage
            elif position_counter <= len1:
                last_sum = int(str_num1[-position_counter]) + carriage
            elif position_counter <= len2:
                last_sum = int(str_num2[-position_counter]) + carriage
            self.total_val = str(last_sum)[-1] + self.total_val
            carriage = 1 if last_sum >= 10 else 0
            if carriage:
                carriage_count += 1
            position_counter += 1
        self.total_val = "  " + self.total_val
        return carriage_count

    def number_of_carry_operations(self, num1: int, num2: int):
        carry_count = 0
        carry = 0
        add1 = add2 = 0
        while True:
            if num1 and num2:
                add1 = num1 % 10
                add2 = num2 % 10
                num1 = num1 // 10
                num2 = num2 // 10

            elif num1 or num2:
                if num1:
                    add1 = num1 % 10
                    add2 = 0
                    num1 = num1 // 10
                elif num2:
                    add2 = num2 % 10
                    add1 = 0
                    num2 = num2 // 10
            else:
                break
            if add1 + add2 + carry > 9:
                carry = 1
                carry_count += 1
            else:
                carry = 0
        return carry_count



start = datetime.now()
s = Sol()
print(s.number_of_carry_operations(123, 456))  # 0
print(s.number_of_carry_operations(555, 555))  # 3
print(s.number_of_carry_operations(900, 11))  # 0
print(s.number_of_carry_operations(145, 55))  # 2
print(s.number_of_carry_operations(0, 0))  # 0
print(s.number_of_carry_operations(1, 99999))  # 5
print(s.number_of_carry_operations(999045, 1055))  # 5
print(s.number_of_carry_operations(101, 809))  # 1
print(s.number_of_carry_operations(189, 209))  # 1
print("total value ", s.total_val)

print (f"time taken - {datetime.now() - start}")

