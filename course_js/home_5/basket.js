'use strict';
// Задание 2

const basketProduct = {
    render(product) {
        return `<div class="product">
                    <div><b>Название</b>: ${product.product_name}</div>
                    <div><b>Цена за 1 шт.</b>: ${product.price} руб.</div>
                    <div><b>Количество</b>: ${product.quantity}</div>
                    <div><b>Стоимость</b>: ${product.price * product.quantity} руб.</div>
                </div>`;
    }
}

const basket = {
    basketList: null,
    basketButton: null,
    basketProduct,
    products: [
        {
            id_product: 1,
            product_name: 'LOL',
            price: 2200,
            quantity: 2,
        },
        {
            id_product: 2,
            product_name: 'Lego',
            price: 1700,
            quantity: 1,
        },
        {
            id_product: 3,
            product_name: 'Poopsi',
            price: 2500,
            quantity: 1,
        },
        {
            id_product: 4,
            product_name: 'Stickbot',
            price: 150,
            quantity: 5,
        }
    ],

    init() {
        this.basketList = document.querySelector('.basket-list');
        this.basketButton = document.querySelector('.basket-button');
        this.basketButton.addEventListener('click', this.clearBasket.bind(this));
        this.render();
    },

    render() {
        if (this.products.length) {
            this.products.forEach(el => {
                this.basketList.insertAdjacentHTML('beforeend', this.basketProduct.render(el));
            });
            this.basketList.insertAdjacentHTML('beforeend', `В корзине ${this.products.length} ${this.textPosition()} стоимостью ${this.getBasketPrice()} руб.`);
        }
        else {
            this.basketList.textContent = 'Корзина пуста';
        }
    },

    clearBasket() {
        this.products = [];
        this.render();
    },

    textPosition() {
        if (this.products.length === 1) return 'позиция';
        else if (this.products.length > 1 && this.products.length < 5) return 'позиции';
        else return 'позиций';
    },

    getBasketPrice() {
        return this.products.reduce((totalPrice, el) => totalPrice += el.price * el.quantity, 0);
    }
};

basket.init();