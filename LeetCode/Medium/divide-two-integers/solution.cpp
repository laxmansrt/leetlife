class Solution {
public:
    int divide(int dividend, int divisor) {
        long long INT_MAX_VAL = 2147483647;
        long long INT_MIN_VAL = -2147483648;

        // Overflow case
        if (dividend == INT_MIN_VAL && divisor == -1)
            return INT_MAX_VAL;

        // Determine sign
        int sign = ((dividend < 0) ^ (divisor < 0)) ? -1 : 1;

        // Convert to positive (use long long to avoid overflow)
        long long dvd = llabs(dividend);
        long long dvs = llabs(divisor);

        long long result = 0;

        while (dvd >= dvs) {
            long long temp = dvs;
            long long multiple = 1;

            // Double the divisor
            while (dvd >= (temp << 1)) {
                temp <<= 1;
                multiple <<= 1;
            }

            dvd -= temp;
            result += multiple;
        }

        return sign * result;
    }
};