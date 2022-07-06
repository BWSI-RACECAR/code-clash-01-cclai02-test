import sys

if len(sys.argv) != 2:
    print("Usage: python3 palindrome.py [string]")
    sys.exit(1)

def Solution(s):
    return s == s[::-1] and len(s) > 6

def main():
    print(Solution(sys.argv[1]))

if __name__ == "__main__":
    main()
