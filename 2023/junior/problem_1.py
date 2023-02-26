def get_final_score(delived, collisions):
    score = delived * 50 - collisions * 10
    if delived > collisions:
        score += 500
    
    return score

# test cases
print(get_final_score(5, 2))
print(get_final_score(0, 10))

if __name__ == '__main__':
    delived = input()
    collisions = input()
    print(get_final_score(int(delived), int(collisions)))