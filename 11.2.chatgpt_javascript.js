// Prompt the user to enter a number
let number = prompt("Enter a number:");

// Convert the input to a number (since prompt returns a string)
number = Number(number);

// Check if the number is positive, negative, or zero
if (number > 0) {
    console.log("The number is positive.");
} else if (number < 0) {
    console.log("The number is negative.");
} else if (number === 0) {
    console.log("The number is zero.");
} else {
    console.log("That's not a valid number.");
}
