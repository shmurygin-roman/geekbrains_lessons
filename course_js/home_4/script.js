'use strict';
// Задание 1

function getObjByNum(num) {
    if (!Number.isInteger(num) || num < 0 || num > 999) {
        console.log('Число должно быть от 0 до 999.');
        return {};
    }

    const obj = {};
    obj.единицы = num % 10;
    obj.десятки = Math.floor(num / 10) % 10;
    obj.сотни = Math.floor(num / 100);
    return obj;
}

console.log(getObjByNum(368));

// Задание 2

const Basket = {
    products: [
        {
            id_product: 1,
            product_name: "item_1_name",
            price: 200,
            quantity: 5
        },
        {
            id_product: 2,
            product_name: "item_2_name",
            price: 500,
            quantity: 2
        }
    ],
    countBasketPrice() {
        return this.products.reduce((totalPrice, cartItem) => totalPrice += cartItem.price * cartItem.quantity, 0);
    }
};

console.log(Basket.countBasketPrice());