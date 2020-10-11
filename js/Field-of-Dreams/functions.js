
"use strict";


const LIVE = '\u2764';

export let msgs = {
    'enter': 'Назовите букву или слово целиком: ',
    'right': 'Есть такая буква!',
    'wrong': 'Неправильно. Вы теряете жизнь',
    'wrong-input': 'Это не буква и не слово. Вы теряете жизнь',
    'lose': 'Вы проиграли. Это слово:',
    'win': 'Вы выиграли! Приз в студию!',
    'nolives':  'У вас закончились жизни.',
    'thanks': 'Спасибо за игру'
};


export function show_message(msg, added='') {
    // печатает сообщение
    alert(msg + added);
}


export function promt(msg) {
    // получает ответ от пользователя в верхнем регистре
    return promt(msg.toUpperCase());
}


export function get_word() {
    return 'носок'.toUpperCase();
}


export function is_alive(lives) {
    let total = get_lives();
    return !Boolean((total - lives === total));
}


export function get_lives() {
    // возвращает кол-во жизней в начале игры
    return 3;
}


export function update_lives(lives) {
    // изменяет кол-во жизней игрока
    return lives - 1;
}


export function create_table(current_word) {
    // возвращает строку из квадратиков
    return '#' * current_word.length();
}

export function show_table(table, lives) {
    // отрисовывает таблицу
    lives = LIVE + 'x' + toString(lives);
    alert(table + ' | ' + lives);
}


export function is_word(answer, current_word) {
    return answer.length() === current_word.length();
}


export function is_word_correct(answer, current_word) {
    return answer === current_word;
}


export function is_letter(answer, current_word) {
    return answer.length() === 1;
}


export function is_letter_correct(answer, current_word) {
    return answer in current_word;
}


export function is_last_letter_in_word(table) {
    return table.count('#') === 0;
}


export function update_table(table, current_word, answer) {
    table = table.split('#');
    for(const [i, char] of current_word.entries()) {
        if (char === answer) {
            table[i] = char;
        }
    }
    return '#'.join(table);
}