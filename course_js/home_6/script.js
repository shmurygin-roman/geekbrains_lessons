'use strict';
// Задание 1

/*Каталог*/
const itemProduct = {
    render(product) {
        return `<div class="product">
                    <div><b>Название</b>: ${product.product_name}</div>
                    <div><b>Цена за 1 шт.</b>: ${product.price} руб.</div>
                    <div><b>В наличии</b>: ${product.quantity} шт.</div>
                    <button class="product__add_basket" id_product="${product.id_product}">В корзину</button>
                </div>`;
    }
};

const catalog = {
    catalogList: null,
    basket: {},
    itemProduct,
    productList: [
        {
            id_product: 1,
            product_name: 'LOL',
            price: 2200,
            quantity: 20,
        },
        {
            id_product: 2,
            product_name: 'Lego',
            price: 1700,
            quantity: 10,
        },
        {
            id_product: 3,
            product_name: 'Poopsi',
            price: 2500,
            quantity: 10,
        },
        {
            id_product: 4,
            product_name: 'Stickbot',
            price: 150,
            quantity: 50,
        }
    ],

    init(basket) {
        this.catalogList = document.querySelector('.catalog-list');
        this.basket = basket;
        this.catalogList.addEventListener('click', event => this.addBasket(event));
        this.render();

    },

    render() {
        this.productList.forEach(el => {
            this.catalogList.insertAdjacentHTML('beforeend', this.itemProduct.render(el));
        });
    },

    addBasket(event) {
        if (!event.target.classList.contains('product__add_basket')) return;
        const id = +event.target.dataset.id_product;
        this.basket.addBasket(id);
    }
};

/*Корзина*/
const basketProduct = {
    render(product) {
        return `<div class="product">
                    <div><b>Название</b>: ${product.product_name}</div>
                    <div><b>Цена за 1 шт.</b>: ${product.price} руб.</div>
                    <div><b>Количество</b>: ${product.quantity}</div>
                    <div><b>Стоимость</b>: ${product.price * product.quantity} руб.</div>
                </div>`;
    }
};

const basket = {
    basketList: null,
    basketButton: null,
    basketProduct,
    products: [],
    catalog: [],

    init(catalog) {
        this.basketList = document.querySelector('.basket-list');
        this.basketButton = document.querySelector('.basket-button');
        this.basketButton.addEventListener('click', this.clearBasket.bind(this));
        this.catalog = catalog;
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
    },

    addBasket(id) {
        const product = this.catalog.find(el => el.id_product === id);

        if (product) {
            this.products.push(product);
            this.render();
        } else {
            alert('Ошибка! Товар не добавлен.');
        }
    },
};

catalog.init(basket);

basket.init(catalog.productList);


