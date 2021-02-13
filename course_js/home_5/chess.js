'use strict';
// Задание 1

const chess = {
    game: document.getElementById('game'),

    isBlack(row, col) {
        if (row === 0 || col === 0 || row === 9 || col === 9) {
            return false;
        }
        if ((row % 2 === 1 && col % 2 === 0) || (row % 2 === 0 && col % 2 === 1)) {
            return true;
        }
    },

    render() {
        const rows = [0, 8, 7, 6, 5, 4, 3, 2, 1, 0];
        const cols = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 0];

        for (let row = 0; row < rows.length; row++) {
            const tr = document.createElement('tr');
            this.game.appendChild(tr);

            for (let col = 0; col < cols.length; col++) {
                const td = document.createElement('td');
                tr.appendChild(td);

                if (rows[row] === 0 && cols[col] !== 0) {
                    td.innerHTML = cols[col];
                }
                else if (cols[col] === 0 && rows[row] !== 0) {
                    td.innerHTML = rows[row].toString();
                }

                if (this.isBlack(row, col)) {
                    td.style.backgroundColor = 'black';
                }
            }
        }
    },

};

chess.render();


