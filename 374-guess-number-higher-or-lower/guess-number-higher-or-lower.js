/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

/**
 * @param {number} n
 * @return {number}
 */
var guessNumber = function(n) {
    let high=n
    let low=0
    while(low<=high){
      let mid=Math.floor((high+low)/2)
      if(guess(mid)===0){
        return mid
      }
      if(guess(high)===0){
        return high
      }
      if(guess(mid)===-1){
        high=mid
      }
      if(guess(mid)===1){
        low=mid
      }
    }
};