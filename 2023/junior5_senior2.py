def hunt_word(word, letters_grid):
    pass
    


if __name__ == '__main__':
    word = input()
    rows= int(input())
    columns = int(input())
    letters_grid = []
    for row in range(rows):
        letters_grid.append(input())

    print(hunt_word(word, letters_grid))