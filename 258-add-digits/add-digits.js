/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    let sum=0
    while(num>0)
    {
    let r=num%10
    sum+=r
    num=Math.floor(num/10)
    }
    if(sum<10){
        return sum
    }else{
        return addDigits(sum)
    }
};