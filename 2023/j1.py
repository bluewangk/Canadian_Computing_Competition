def get_final_score(args):
    [delivered, collisions] = args
    delivered = int(delivered)
    collisions = int(collisions)

    score = delivered * 50 - collisions * 10
    if delivered > collisions:
        score += 500

    return str(score)


if __name__ == '__main__':
    inputs = []
    for _ in range(2):
        inputs.append(input())

    print(get_final_score(inputs))
