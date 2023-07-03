names = "bjone"
user_input = input("Please enter your string: ")
illegal_string = False
index = 0

if(len(user_input) % len(names) != 0) or len(user_input) < len(names):
    illegal_string = True
for i in range(len(user_input)):
    if user_input[i] == names[index]:
        index += 1
        if(index > len(names)-1):
            index = 0
    else:
        illegal_string = True
if(illegal_string):
    print("False. Goodbye.")
else:
    print("True. Goodbye.")
