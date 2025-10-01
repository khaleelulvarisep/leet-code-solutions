/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
function hammingDistance(x, y) {
    let xor = x ^ y;
    let count = 0;
    while (xor > 0) {
        xor &= (xor - 1);
        count++;
    }
    return count;
}

