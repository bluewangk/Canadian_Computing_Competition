def hunt_word(word, letters_grid):
    letters_grid = [line.replace(" ", "") for line in letters_grid]
    # TODO
    
    


if __name__ == '__main__':
    word = input()
    rows= int(input())
    columns = int(input())
    letters_grid = []
    for row in range(rows):
        letters_grid.append(input())

    print(hunt_word(word, letters_grid))

    # word = "NATURE"
    # grid = [
    #     "N A T S F E G Q N",
    #     "S A I B M R H F A",
    #     "C F T J C U C L T",
    #     "K B H U P T A N U",
    #     "D P R R R J D I R",
    #     "I E E K M E G B E",
    # ]
    # print(hunt_word(word, grid))