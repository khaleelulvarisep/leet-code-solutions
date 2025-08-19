/**
 * @param {number} n
 * @return {boolean}
 */
function isHappy(n) {
    const seen = new Set();

    function sumOfSquares(num) {
        let sum = 0;
        while (num > 0) {
            let digit = num % 10;
            sum += digit * digit;
            num = Math.floor(num / 10);
        }
        return sum;
    }

    while (n !== 1 && !seen.has(n)) {
        seen.add(n);
        n = sumOfSquares(n);
    }

    return n === 1;
}



