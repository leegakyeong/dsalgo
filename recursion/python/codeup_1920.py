result = ''
def decimal_to_binary(n):
    global result # 뭔가 이상한데....
    if n == 0 or n == 1:
        result = str(n) + result
        return result
    else:
        result = str(n%2) + result
        return decimal_to_binary(n//2)

print(decimal_to_binary(10))
