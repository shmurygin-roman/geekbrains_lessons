'use strict';
// Задание 1
function simple(x) {
    if (x < 2) return false;
    for (let i = 2; i <= x; i++) {
        if (x !== i && x % i === 0) return false;
    }
    return true;
}

let i = 0;
while (i <= 100) {
    if (simple(i)) console.log(i);
    i++;
}


// Задание 2 - 3
const basket = [
    ['item_1', 5, 200],
    ['item_2', 2, 500],
    ['item_3', 4, 2000]
]

function countBasketPrice() {
    let result = 0
    for (let i = 0; i < basket.length; i++) {
        result += basket[i][1] * basket[i][2]
    }
    return result
}

console.log(countBasketPrice(basket));
