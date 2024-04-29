/* https://judge.beecrowd.com/pt/problems/view/1732 */

use std::io;
use std::collections::HashMap;

fn read_integer() -> i32 {
    let mut input = String::new();
    io::stdin().read_line(&mut input)
        .expect("Failed to read line");

    let parsed_input: i32 = input.trim().parse()
        .expect("Failed to parse integer");

    parsed_input
}

fn get_max_level_value(level: &i32) -> i32 {
    (3*level.pow(2)) - (3*level) + 1
}

fn solver() -> (i32, i32) {
    let target = read_integer();
    let mut level = 1;
    let mut max_level_value: i32;
    loop {
        max_level_value = get_max_level_value(&level);

        if max_level_value == target {
            return (level-1, 0); /* encontra A coordenada x quando o valor target é exatamente o maximo valor possivel em dado nivel */
        }

        else if max_level_value > target {
            break;
        }
        level += 1;
    }

    let mut map: HashMap<String, i32> = HashMap::new();
    map.insert(String::from("up"), level); /* maximo de pulos que podem ser feitos nessa direção */
    map.insert(String::from("left"), level*2);
    map.insert(String::from("down"), level);
    map.insert(String::from("right"), level*2);

    let mut current_binary_coordinates_address = (level-1, 0);
    let jumps_needed = max_level_value - target;
    let mut current_square_value = max_level_value;

    for _ in 0..jumps_needed { /* Executa os saltos até chegar ao target */
        const movements = ["up", "left", "down", "right"];
    }

    /* to go left => x-1 */
    /*  to go right => x+1 */
    /*  to go up y-1 */
    /* to go down y+1 */
    return (10, 10)
}

fn main() {
    loop {
        let res = solver();
        println!("{}", res.0);
    }
}