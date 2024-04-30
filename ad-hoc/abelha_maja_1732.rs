/* https://judge.beecrowd.com/pt/problems/view/1732 */

use std::io;
use std::collections::HashMap;

fn read_integer() -> isize {
    let mut input = String::new();
    io::stdin().read_line(&mut input)
        .expect("Failed to read line");

    let parsed_input: isize = input.trim().parse()
        .expect("Failed to parse integer");

    parsed_input
}

fn get_max_level_value(level: &isize) -> isize {
    (3*level.pow(2)) - (3*level) + 1
}

fn solver() -> (isize, isize) {
    let target = read_integer();
    let mut level = 1;
    let mut max_level_value: isize;
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

    let mut map: HashMap<String, isize> = HashMap::new();
    map.insert(String::from("up"), level-1); /* maximo de pulos que podem ser feitos nessa direção */
    map.insert(String::from("left"), (level-1)*2);
    map.insert(String::from("down"), level-1);
    map.insert(String::from("right"), (level-1)*2);

    let movements: [String; 4] = [
        String::from("up"),
        String::from("left"),
        String::from("down"),
        String::from("right")
    ];
    let mut current_binary_coordinates_address = (level-1, 0);
    let jumps_needed = max_level_value - target;
    let mut current_movement_type_index = 0;
    for _ in 0..jumps_needed { /* Executa os saltos até chegar ao target */
        if let Some(value) = map.get_mut(&movements[current_movement_type_index]) {
            match movements[current_movement_type_index].as_str() {
                "up" => {
                    current_binary_coordinates_address = (current_binary_coordinates_address.0, current_binary_coordinates_address.1 - 1);
                }
                "left" => {
                    current_binary_coordinates_address = (
                        current_binary_coordinates_address.0 - 1,
                        if *value <= (level-1) { current_binary_coordinates_address.1 + 1 } else { current_binary_coordinates_address.1 }
                    )
                }
                "right" => {
                    current_binary_coordinates_address = (
                        current_binary_coordinates_address.0 + 1,
                        if *value <= (level-1) {current_binary_coordinates_address.1 - 1} else { current_binary_coordinates_address.1 }
                    );
                }
                "down" => {
                    current_binary_coordinates_address = (current_binary_coordinates_address.0, current_binary_coordinates_address.1 + 1);
                }
                _ => {
                    println!("No patterns matched");
                }
            }
            *value -= 1;
            if *value == 0 {
                current_movement_type_index += 1;
            }
        }
    }
    current_binary_coordinates_address
}

fn main() {
    loop {
        let res = solver();
        println!("{} {}", res.0, res.1);
    }
}