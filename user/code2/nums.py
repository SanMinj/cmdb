#encoding: utf-8
num_list = [1,2,3,2,12]

right = None
left = None
for num in num_list:
    if right is None:
        right = num
    elif right < num:
        left = right
        right = num
    elif left is None:
        left = num
    elif left < num:
        left = num

print right, left