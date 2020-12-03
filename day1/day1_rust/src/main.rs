use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::process;

//es llegeix apartir de la carpeta day1_rist
fn main() {
    let filename = "../input.txt";
    let mut v: Vec<i32> = Vec::new();
    // File hosts must exist in current path before this produces output
    if let Ok(lines) = read_lines(filename) {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(ip) = line {
             //   println!("{}", ip);
                v.push(ip.parse::<i32>().unwrap());
            }
        }
    }
}

fn part_one(v: Vec<i32>) {
    for x in 0..v.len() {
        for y in x .. v.len(){
            if v[x] + v[y] == 2020{
                println!("{} + {} = 2020", v[x], v[y]);
                println!("Sol: {}", v[x] * v[y]);
                process::exit(0);                
            }
        }

    }
}

fn part_two(v: Vec<i32>) {
    for x in 0..v.len() {
        for y in x .. v.len(){
            for z in y .. v.len(){
                if v[x] + v[y] + v[z] == 2020{
                    println!("{} + {} + {} = 2020", v[x], v[y], v[z]);
                    println!("Sol: {}", v[x] * v[y] * v[z]);

                    process::exit(0);                
                }
            }
        }
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
