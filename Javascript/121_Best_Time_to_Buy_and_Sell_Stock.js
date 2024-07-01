/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    // let buy = prices[0]
    // let profit = 0
    // for(let i =0; i<prices.length;i++){
    //     if(prices[i]<buy){
    //         buy = prices[i]
    //     }
    //     if(prices[i]-buy>profit){
    //         profit = prices[i]-buy
    //     }
    // }
    // return profit
    let b1 = -Infinity
    let s1 = 0
    for(let i =0; i<prices.length;i++){
        b1= Math.max(b1,-prices[i])
        s1 = Math.max(s1,b1+prices[i])
    }
    return s1
};
