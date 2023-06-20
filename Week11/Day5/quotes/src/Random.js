import React, { useEffect, useState } from 'react';
import quotes from './quotesandColors';
import colors from './colors';

const RandomNumberAndColor = () => {
  // const [randomNumber, setRandomNumber] = useState(0);
  const [randomColor, setRandomColor] = useState("blue");
  const [quote, setQuote] = useState(quotes[0].quote);
  const [author, setAuthor] = useState(quotes[0].author);
  
  useEffect(() => {
    document.body.style.backgroundColor = randomColor
  }, [randomColor])
  

  const handleButtonClick = () => {
    const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
    const randomClr = colors[Math.floor(Math.random() * colors.length)];
    console.log(randomQuote,randomClr)

    // setRandomNumber(randomNum);
    setRandomColor(randomClr);
    setQuote(randomQuote.quote)
    setAuthor(randomQuote.author)
    // return [randomNum,randomClr]
  };

  return (
    <div id="big">
      <div style={{backgroundColor : "white", borderColor: randomColor,borderStyle:'unset',borderRadius:30}}>
        <p style={{color:randomColor,fontSize:30, fontFamily:'fantasy'}}>Quote:{quote}</p>
        <p style={{color:randomColor,fontSize:15}}>Author: {author}</p>
        <button style={{backgroundColor : randomColor,fontSize:14,fontFamily:'fantasy',borderStyle:'groove',borderColor:'blue',color:'white'}} onClick={handleButtonClick}>New Quote</button>
      </div>
    </div>
  );
};

export default RandomNumberAndColor;


