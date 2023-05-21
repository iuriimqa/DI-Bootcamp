function bottlesOfBeer() {
    var bottles = prompt("How many bottles of beer on the wall? ");
    while (bottles > 0) {
      console.log(bottles + " bottles of beer on the wall, " + bottles + " bottles of beer.");
      console.log("Take one down and pass it around, " + (bottles - 1) + " bottles of beer on the wall.");
      bottles--;
    }
    console.log("No more bottles of beer on the wall, no more bottles of beer.");
    console.log("Go to the store and buy some more, 99 bottles of beer on the wall.");
  }
  
  bottlesOfBeer();
  