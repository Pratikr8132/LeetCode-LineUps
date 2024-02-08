class Solution:
    def numSquares(self, n: int) -> int:

        def is_perfect_square(n):
            square_root = int(math.sqrt(n))
            return square_root**2 == n
        
        cpy_n = n
        if is_perfect_square(n):
            return 1
       
        while n & 3 == 0:    
            n >>= 2           
        if n & 7 == 7:    
            return 4
        n = cpy_n
        for i in range(1, int(math.sqrt(n)) + 1):
            if is_perfect_square(n - i*i):
                return 2
        return 3