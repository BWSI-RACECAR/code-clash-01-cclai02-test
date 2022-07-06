import sys

class Solution:
    # Write code below to complete prompt
    def isPalindrome(self, s):
        return s == s[::-1] and len(s) > 6

def main():
    tc1 = Solution()
    inpyt = input()
    # Write code below to complete prompt
    print(tc1.isPalindrome(inpyt))

if __name__ == "__main__":
    main()
