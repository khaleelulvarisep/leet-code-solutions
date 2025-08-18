/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let nw=s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase()
    let rev=nw.split('').reverse().join('')
     
     return rev===nw
};