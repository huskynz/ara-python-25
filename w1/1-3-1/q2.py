# 1-1-1
# Peter
# peter@husky.nz
# wow

user_num1ipt = input("Please enter the first integer: ")
user_num2ipt = input("Please enter the second integer: ")

user_num1 = int(user_num1ipt)
user_num2 = int(user_num2ipt)
add_result = user_num1
add_result += user_num2

sub_result = user_num1
sub_result -= user_num2

diff_result = user_num1
diff_result /= user_num2

multi_result = user_num1
multi_result *= user_num2

print(f'{user_num1} + {user_num2} is {add_result}')
print(f'{user_num1} - {user_num2} is {sub_result}')
print(f'{user_num1} * {user_num2} is {multi_result}') 
print(f'{user_num1} / {user_num2} is {diff_result}' ) 