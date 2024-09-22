def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
    # if the index number is an even number, write it with an uppercase letter
       if string_index % 2 == 0:
        new_string += string[string_index].upper()
    # if the index number is single, write with a lowercase letter
       else:
        new_string += string[string_index].lower()
    print(new_string)           
        
alternating("my name is kayra ")   