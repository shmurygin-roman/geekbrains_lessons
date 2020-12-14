'use strict';
// Задание 1
var a = 1, b = 1, c, d;
c = ++a; alert(c);           // 2:  c = undefined, a = 1, после ++a, a = 2, c = a, c = 2
d = b++; alert(d);           // 1:  d = undefined, b = 1, d = b до b++, поэтому d = 1, b = 2
c = (2 + ++a); alert(c);     // 5:  a = 2, ++a до сложения, поэтому c = 2 + 3 = 5, a = 3
d = (2 + b++); alert(d);     // 4:  b = 2, b++ после сложения, поэтому d = 2 + 2 = 4, b = 3
alert(a);                    // 3
alert(b);                    // 3

// Задание 2
var a = 2;
var x = 1 + (a *= 2); // x = 1 + (2 * 2) = 5

// Задание 3
function calc(x, y) {
    if (x >= 0 && y >= 0 && x >= y) return x - y
    else if (x >= 0 && y >= 0 && x < y) return y - x
    else if (x < 0 && y < 0) return x * y
    else return x + y
}

let a = -10;
let b = 4;
let c = calc(a, b);
alert(c);

// Задание 4
let a = 11;

switch (a) {
    case 1: alert(a++);
    case 2: alert(a++);
    case 3: alert(a++);
    case 4: alert(a++);
    case 5: alert(a++);
    case 6: alert(a++);
    case 7: alert(a++);
    case 8: alert(a++);
    case 9: alert(a++);
    case 10: alert(a++);
    case 11: alert(a++);
    case 12: alert(a++);
    case 13: alert(a++);
    case 14: alert(a++);
    case 15: alert(a++);
}

// Задание 5
function add(x, y) {
    return x + y
}

function sub(x, y) {
    return x - y
}

function multi(x, y) {
    return x * y
}

function div(x, y) {
    return x / y
}

// Задание 6
function mathOperation(x, y, operation) {
    switch (operation) {
        case '+': return add(x, y);
        case '-': return sub(x, y);
        case '*': return multi(x, y);
        case '/': return div(x, y);
    }
}

let a = 7
let b = 8
alert(mathOperation(a, b, '/'));