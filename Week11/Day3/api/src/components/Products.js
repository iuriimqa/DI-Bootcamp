import { useState, useEffect } from 'react';

const Products = (props) => {

    useEffect(() => {
        const all = async () => {
            try {
                const res = await fetch('http://localhost:3030/api/products');
                const data = await res.json();
                setProducts(data)
            } catch (e) {
                console.log(e);
            }
        }
        all()
    }, [])

    const all = async () => {
        try {
            const res = await fetch('http://localhost:3030/api/products');
            const data = await res.json();
            setProducts(data)
        } catch (e) {
            console.log(e);
        }
        // fetch('http://localhost:3030/api/products')
        // .then(res => res.json())
        // .then(data => {
        //   setProducts(data)
        // })
        // .catch(err => {
        //   console.log(err);
        // })
    }

    const [products, setProducts] = useState([])
    return (
        <div>
            <h1>Shop</h1>
            {
                products.map(item => {
                    return (
                        <div key={item.id} style={{
                            display: 'inline-block',
                            padding: '20px',
                            margin: '20px',
                            border: '1px solid #fff',
                        }}>
                            <h4>{item.name}</h4>
                            <h5>{item.price}</h5>
                        </div>
                    )
                })
            }
        </div>
    )
}
export default Products