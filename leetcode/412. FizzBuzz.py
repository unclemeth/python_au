class Solution:
    def fizzBuzz(self, n):
        fizz_buzz_list = []
        for i in range(1, n + 1):
            if i % 5 == 0 and i % 3 == 0:
                fizz_buzz_list.append('FizzBuzz')
            elif i % 3 == 0:
                fizz_buzz_list.append('Fizz')
            elif i % 5 == 0:
                fizz_buzz_list.append('Buzz')
            else:
                print(i)
                fizz_buzz_list.append(str(i))
        return fizz_buzz_list