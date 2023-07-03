names = "bjone"
user_input = input("Please enter username: ")
index = 0
illegal_string = False
if len(user_input) < len(names):
    illegal_string = True
else:
    for i in range(len(user_input)):
        if index < len(names):
            if user_input[i] == names[index]:
                ##print("Next letter")
                index += 1
            elif user_input[i] == names[index - 1]:
               ##print("Repeated letter")
               index = index
            else:
                ##print("Illegal letter")
                illegal_string = True
        else:
            if(user_input[i] == names[0]):
                ##print("Returned to first letter")
                index = 1   
            if(user_input[i] == names[index -1]):
                ##print("Repeated Letter")
                index = index
            else:
                ##print("Illegal letter")
                illegal_string = True
    if user_input[len(user_input) - 1] != names[len(names) -1]:
        illegal_string = True
if illegal_string:
    print("False. Goodbye")
else:
    print("True. Goodbye")





        