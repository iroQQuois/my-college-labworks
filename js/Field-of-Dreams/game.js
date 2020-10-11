"use strict";


let current_word = get_word();
let table = create_table(current_word);
let lives = get_lives();


while (is_alive(lives)) {
    show_table(table, lives);
    let answer = promt(msgs['enter']);
    if (is_word(answer, current_word)) {
        if (is_word_correct(answer, current_word)) {
            show_message(msgs['win']);
        } else {
            show_message(msgs['lose'], current_word);
            break;
        }
    }
    if (is_letter(answer, current_word)) {
        if (is_letter_correct(answer, current_word)) {
            show_message(msgs['right']);
            table = update_table(table, current_word, answer);
            if (is_last_letter_in_word(table)) {
                show_message(msgs['win']);
                break;
            continue;
            }
        }
    } else {
        show_message(msgs['wrong-input']);
        lives = update_lives(lives);
        continue;
    }
    show_message(msgs['wrong']);
    lives = update_lives(lives);
}
if (!is_alive(lives)){
    show_message(msgs['nolives']);
}

show_message(msgs['thanks']);

