pepper_SHU_dict = {
    "Poblano":  1500,
    "Mirasol":  6000,
    "Serrano":  15500,
    "Cayenne":  40000,
    "Thai":     75000,
    "Habanero": 125000,
}

def calculate_total_speciness(peppers):
    total_speciness = 0
    for pepper in peppers:
        if pepper in pepper_SHU_dict:
            total_speciness += pepper_SHU_dict[pepper]
    
    return total_speciness

if __name__ == '__main__':
    number = input()
    peppers = []
    for _ in range(int(number)):
        peppers.append(input())

    print(calculate_total_speciness(peppers))