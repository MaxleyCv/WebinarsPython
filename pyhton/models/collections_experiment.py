def add_sequence(sequence):
    sequence.append("nuiwe streng")
    sequence *= 2*2
    print(sequence * 2)

def add_element_to_tup_list(sequence: tuple):
    sequence[0].append(10)

def play_with_slicing():
    my_list = [23, 15, 97, 14, 24, 25, 3, "23", (1, 2, "blue"), 9]
    print("first slice: " + str(my_list[2:5]))
    my_list[2:10:2] = [0, 0, 0, 0]
    print("second slice: " + str(my_list[2:]))

if __name__ == "__main__":
    play_with_slicing()
    print("**********************************")

    test_list = [1, 2, 3, 4]
    print("before: " + str(test_list))
    add_sequence(test_list)
    print("after: " + str(test_list))
    if 2 in test_list:
        print("Ama hepi")

    new_tuple = ([1, 2], [3, 4])
    print("before: " + str(new_tuple))
    add_element_to_tup_list(new_tuple)
    print("after: " + str(new_tuple))


