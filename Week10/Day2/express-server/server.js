const express = require('express');
const {products} = require('./config/data.js')

const app = express();

app.listen(5001, ()=>{
    console.log('server running on the port 5001');
})


app.get('api/products',(req,res)=> {
    res.json(products)
})

app.get('api/products/:product_id',(req,res)=> {
    const id = req.params.product_id
    const product = products.find(item => item.id == id);
    if(!product) {
        return res.status(404).json({message:'Product not found'})
    }
    res.status(200).json(product)
})

