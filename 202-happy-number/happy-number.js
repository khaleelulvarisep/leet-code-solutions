/**
 * @param {number} n
 * @return {boolean}
 */
function isHappy(n) {
    const seen = new Set();

    function sumOfSquares(num) {
        let sum = 0;
       let str=num.toString()
       for(let val of str){
        sum+=Number(val)*Number(val)
       }
       return sum
    }

    while (n !== 1 && !seen.has(n)) {
        seen.add(n);
        n = sumOfSquares(n);
    }

    return n === 1;
}



