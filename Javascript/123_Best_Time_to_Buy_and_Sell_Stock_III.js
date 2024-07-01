/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let b1 = -Infinity
    let s1 = 0
    let b2 = -Infinity
    let s2 = 0
    for(let price of prices){
        b1 = Math.max(b1, -price)
        s1 = Math.max(s1, b1+price)
        b2 = Math.max(b2, s1-price)
        s2 = Math.max(s2, b2+price)
    }
    return s2
};
