/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    for(i=1;i<=n;i=i*2){
      if(i==n){
        return true
      }
    }
    return false
};