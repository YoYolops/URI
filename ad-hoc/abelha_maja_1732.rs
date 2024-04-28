/* https://judge.beecrowd.com/pt/problems/view/1732 */

use std::io;

fn read_input() -> String {
    let mut input = String::new();

    match io::stdin().read_line(&mut input) {
        Ok(_) => {
            input.trim_end().to_string()
        }
        Err(error) => {
            println!("Error reading input: {}", error);
            String::new()
        }
    }
}

fn parse_string_to_int(input: &str) -> Result<isize, String> {
    match input.trim().parse::<isize>() {
        Ok(parsed_int) => Ok(parsed_int),
        Err(parse_error) => println!("Failed to parse string {} to int", str),
    }
}


