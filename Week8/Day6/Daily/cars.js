// // Part1
// const inventory = [
//     { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
//     { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
//     { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
//     { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
//     { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
//   ];

//   function getCarHonda(inventory){
//     const hondas = inventory.find(car => car.car_make = "Honda");
//     console.log(`This is a ${hondas.car_make} ${hondas.car_model} from ${hondas.car_year}`);
//   }

// getCarHonda(inventory)

// Part2
const inventory = [
    { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
    { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
    { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
    { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
    { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
  ];

  function sortCarInventoryByYear(inventory) {
    const sortedCars = inventory.sort((a, b) => {
      if (a.car_year < b.car_year) {
        return -1;
      }
      if (a.car_year > b.car_year) {
        return 1;
      }
      return 0;
    });
    console.log(sortedCars);
  }

sortCarInventoryByYear(inventory);