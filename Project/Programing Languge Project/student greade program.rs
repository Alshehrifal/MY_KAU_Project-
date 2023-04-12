	use std::io; // Rust Standard Library 
	use io::BufRead; // necessary to have `.read_line()` on
	                 // locked stdin available 
	 
	fn main() { //main function
	 
	    let stdin = io::stdin(); // handle to the standered input 
	print!("\n========================================"); 
	print!("\n=====reading student greade program=====");
	print!("\n========================================\nEnter number of student :"); 
	print!("\n");
	    let mut locked_stdin = stdin.lock();//handel for scoping,reading data
	    let mut buffer = String::new(); //red line 
	    locked_stdin .read_line(&mut buffer).expect("Need number of student");
	     //lock buffer to make it like circular array    
	    let numberofgrades: usize = buffer.trim().parse().expect("Need a number");
	   //pointer size and remove the white space and convert string to intger
	    buffer.clear(); //set the buffer 
	    let  mut gred:Vec<f32> = Vec::with_capacity(numberofgrades);
	 	//create vec with initial size  
	     //reade the greate
    for x in 0..numberofgrades { //for loop for number of student
	        buffer.clear(); //make sure the buffer is clean
	        print!("\nGrade {}: ",x+1);
	        locked_stdin.read_line(&mut buffer).expect("Need Grade"); //read the greade
       gred.push(buffer.trim().parse().expect("Need a number")); //insert the value in the  vec and remove the white space and convert string to intger
	        
	      println!();
	    }
	 
	   //find  the avg 
	    let numberofgrades = gred.len() as f32; //the size of the vec as float number
	    let mut sum = 0.0;
    // This will consume the numbers.
  for n in  &gred{ //this case we refer to the element of the vec since we dont want to take the ownership 
	        sum += n;
    }
	    let avg:f32=sum/numberofgrades; // find the avg be devied the sum and numberofgrades
    
	  
	   gred.sort_by(|a, b| a.partial_cmp(b).unwrap()); //sort to get easily the max and min
	 
	println!("\nThe  number of student is : {}", numberofgrades);
	print!("\nthe Avrage of student grade is {:.2}",avg);
	print!(" \nMaximum Grade :{}",gred[gred.len()-1]);
	print!(" \nMinimum Grade :{}",gred[0]);
	}
 
