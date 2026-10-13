class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        
        n, m = len(num1), len(num2)
        result = [0] * (n + m)
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                sum_ = mul + result[i + j + 1]
                
                result[i + j + 1] = sum_ % 10
                result[i + j] += sum_ // 10
        
        return ''.join(map(str, result)).lstrip('0')