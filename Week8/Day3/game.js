let count = 0;

function playTheGame() {
  let userInput;
  let computerNumber;

  if (confirm("Start The Game") == true) {
    while (count < 3) {
      userInput = prompt("Please write a number");

      if (!isNaN(userInput) && userInput >= 0 && userInput <= 10) {
        computerNumber = Math.floor(Math.random() * 11);
        compareNumbers(userInput, computerNumber);
      } else {
        if (userInput < 0 || userInput > 10) {
          alert("Sorry, it is not a good number. Goodbye");
        }
        if (isNaN(userInput)) {
          alert("Sorry, it's not a number");
        }
      }
    }
  } else {
    alert("No problem, Goodbye");
  }

  return { userInput: userInput, computerNumber: computerNumber };
}

function compareNumbers(userInput, computerNumber) {
  if (userInput === computerNumber) {
    alert("WINNER");
  } else if (userInput > computerNumber) {
    count += 1;
    alert("Your number is bigger than the computer's, guess again");
  } else {
    count += 1;
    alert("Your number is smaller than the computer's, guess again");
  }

  if (count === 3 && userInput != computerNumber) {
    alert("Game over");
  }
}



  



