import sys

num = input('수를 입력하세요 : ')

# # --- 1
# if num.isalpha():
#     print('#1 정수가 아닙니다.')
# elif int(num) % 3 != 0:
#     print('#1 3의 배수가 아닙니다.')
# else:
#     print('#1 3의 배수 입니다.')

# --- 2
if num.isalpha():
    print('#2 정수가 아닙니다.') or sys.exit(1)
int(num) % 3 != 0 and print('#2 3의 배수가 아닙니다.')
int(num) % 3 == 0 and print('#2 3의 배수 입니다.')