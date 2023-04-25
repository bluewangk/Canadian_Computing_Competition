pepper_SHU_dict = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000,
}


def calculate_total_spiciness(args):
    total_spiciness = 0
    for pepper in args[1:]:
        if pepper in pepper_SHU_dict:
            total_spiciness += pepper_SHU_dict[pepper]

    return total_spiciness


if __name__ == '__main__':
    number = input()
    pp = []
    for _ in range(int(number)):
        pp.append(input())

    print(calculate_total_spiciness(pp))
