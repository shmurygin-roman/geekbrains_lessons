'use strict';
// Задание 1


// Задание 2

class Product {
    id_product = null;
    product_name = null;
    price = null;
    quantity = null;

    init(_id_product, _product_name, _price, _quantity) {
        this.id_product = _id_product;
        this.product_name = _product_name;
        this.price = _price;
        this.quantity = _quantity;
    }
};

class Basket {
    products = [];

    addBasket(product) {
        this.products.push(product);
    };

    countBasketPrice() {
        return this.products.reduce((totalPrice, cartItem) => totalPrice += cartItem.price * cartItem.quantity, 0);
    };
};

let item_1 = new Product();
item_1.init(1, 'item_1_name', 200, 5);
let item_2 = new Product();
item_2.init(2, 'item_2_name', 500, 2);

let basket = new Basket();
basket.addBasket(item_1);
basket.addBasket(item_2);

console.log(basket.countBasketPrice());


