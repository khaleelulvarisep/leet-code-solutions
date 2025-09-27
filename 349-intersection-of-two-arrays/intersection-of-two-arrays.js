/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    let new1=new Set(nums1)
    let new2=new Set(nums2)
    let inter=new Set([...new1].filter(x=>new2.has(x)));
    return [...inter]
};