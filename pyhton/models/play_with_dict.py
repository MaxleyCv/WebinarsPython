



if __name__ == "__main__":
    my_dict = {4: "4", 8: "2", frozenset([23, 45, 53]): "4"}
    adndic = dict(first=1, second=2, third="seven", fourth=300)
    drit_dict  = dict([("first", 2), ((71,), "seventy")])
    veer_dict = dict({4: "4", 8: "2", frozenset([23, 45, 53]): "4"})
    cinci_dict = dict()
    sase_dict = {}


    print(my_dict)
    print(adndic)
    print(drit_dict)

    print("Elementi de cheie 1 e: " + my_dict[4])
    print("Elementi de cheie NEIN sau de valea default e: " + str(my_dict.get("NEIN", 43)))

    my_dict["NEIN"] = 1933
    my_dict.pop(4)


    print(my_dict.values())

    print( my_dict.keys())


    print(my_dict)


    upd_dict = {4: "444", 8: "2551", 94: "4452"}
    my_dict.update(upd_dict)
    print(my_dict)

    for x in iter(my_dict):
        print(x)

    valeble_dict  = {x: x**5 for x in range(30)}
    print(valeble_dict)

