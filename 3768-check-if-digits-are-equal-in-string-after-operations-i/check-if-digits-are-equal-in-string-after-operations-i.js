/**
 * @param {string} s
 * @return {boolean}
 */
var hasSameDigits = function(s) {
   
       while(s.length>2){
        let newS=''
         for(let i=0;i<s.length-1;i++){
            newS+=(Number(s[i])+Number(s[i+1]))%10
         }
         s=newS
       }
       return s[0]===s[1]
};