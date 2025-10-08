/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    const sn=s.split('').sort().join('')
    const tn=t.split('').sort().join('')
    if(sn===tn){
        return true
    }else{
        return false
    }
};