
export async function load({ fetch }) {
    const response = await fetch('http://localhost:8000/products_joined');
    const data = await response.json();

    // Check if the data is empty
    if ( !data ) {
        return { products: [] };
    }

    // Fisher-Yates shuffle algorithm
    for (let i = data.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [data[i], data[j]] = [data[j], data[i]];
    }

    // Get the first 10 elements
    const products = data.slice(0, 9);

    return {
        products
    };
}