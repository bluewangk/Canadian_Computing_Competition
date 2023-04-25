def calculate_tape_length(columns, first_row, second_row):
    first_row = first_row.replace(" ", "")
    second_row = second_row.replace(" ", "")

    total_length = 0
    for i in range(columns):
        if first_row[i] == "1":
            total_length += 3
        if second_row[i] == "1":
            total_length += 3
        
        if i % 2 == 0 and first_row[i] == "1" and second_row[i] == "1":
            total_length -= 2
        if i > 0 and first_row[i] == "1" and first_row[i-1] == "1":
            total_length -= 2
        if i > 0 and second_row[i] == "1" and second_row[i-1] == "1":
            total_length -= 2
    
    return(total_length)


if __name__ == '__main__':
    columns = int(input())
    first_row= input()
    second_row = input()
    print(calculate_tape_length(columns, first_row, second_row))