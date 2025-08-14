/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let str=String(x)
    let rvrs=str.split('').reverse().join('')
    if(str===rvrs){
        return true
    }else{
        return false
    }
};