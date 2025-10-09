/**
 * @param {string} val
 * @return {Object}
 */
function expect(value) {
  return {
    toBe: function(compareValue) {
      if (value === compareValue) {
        return true;
      } else {
        throw new Error("Not Equal");
      }
    },
    notToBe: function(compareValue) {
      if (value !== compareValue) {
        return true;
      } else {
        throw new Error("Equal");
      }
    }
  };
}


/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */