# range
## integer_max
- 9223372036854775807
- sys.maxsize
- 2**63 - 1
# Cast
## int 

아래의 예시처럼 white space를 알아서 제거해주지만 숫자로 바꿀 수 없는 문자가 있으면 Error를 발생함

print(int("1\n"))

print(int("1a")) # Error

print(int("1 "))

print(int("      1   "))