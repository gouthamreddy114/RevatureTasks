import string
def print_pattern(n):
    alphabet = string.ascii_lowercase
    lines = []
    for i in range(n):
        line = '-'.join(alphabet[n-1:n-i-1:-1] + alphabet[n-i-1:n])
        lines.append(line.center(4*n - 3, '-'))
    print('\n'.join(lines + lines[-2::-1]))
if __name__ == "__main__":
    N = int(input())
    print_pattern(N)