def design_palindromic_poster(N, M, R, C):
    if R >= N or C >= M:
        return "IMPOSSIBLE"
    
    words = ["a" * M for _ in range(N)]
    return "\n".join(words)


if __name__ == '__main__':
    [N, M, R, C] = [int(n) for n in input().split()]
    print(design_palindromic_poster(N, M, R, C))