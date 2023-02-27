def get_maximum_participants(number, availabilities):
    maximum_participants = 0
    maximum_day = ""

    for day in range(5):
        participants_in_day = 0
        for availability in availabilities:
            if availability[day] == "Y":
                participants_in_day += 1
        
        if participants_in_day > maximum_participants:
            maximum_participants = participants_in_day
            maximum_day = str(day+1)
        elif participants_in_day == maximum_participants:
            if maximum_day == "":
                maximum_day = str(day+1)
            else:
                maximum_day += "," + str(day+1)

    return maximum_day

if __name__ == '__main__':
    number = int(input())
    availabilities = []
    for _ in range(number):
        availabilities.append(input())

    print(get_maximum_participants(number, availabilities))