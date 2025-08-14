/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let arr=s.trim()
   let arrr=arr.split(' ') 
   return arrr[arrr.length-1].length
};