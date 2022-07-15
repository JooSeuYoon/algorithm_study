import sys

def main():
    read = sys.stdin.readline

    S = read().rstrip()
    T = read().rstrip()
    
    while len(S) != len(T):
        if T[len(T)-1] == 'A':
            T = T[:len(T) - 1]
        elif T[len(T) - 1] == 'B':
            T = T[:len(T) - 1]
            T = T[::-1]
    
    if S==T:
        print(1)
    else:
        print(0)

    return 0

if __name__ == '__main__':
   main()