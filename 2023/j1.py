def get_final_score(inputs):
    [delived, collisions] = inputs.split()
    delived = int(delived)
    collisions = int(collisions)

    score = delived * 50 - collisions * 10
    if delived > collisions:
        score += 500
    
    return str(score)

if __name__ == '__main__':
    inputs = ""
    for _ in range(2):
        data = input()
        inputs += data + "\n"
    
    print(get_final_score(inputs))
