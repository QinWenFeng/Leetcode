class Solution
    def fib(self, n int) - int
        count = 1
        if(n == 0)
            return 0
        if(n == 1)
            return 1
        n1 = 0
        n2 = 1
        while(count  n)
            fib_n = n1 + n2
            n1 = n2
            n2 = fib_n
            count = count + 1
        return fib_n