
export async function load({ fetch }) {
    const categoriesResponse = await fetch('http://localhost:9000/hq_products/categories');
    const categoriesData = await categoriesResponse.json();
    const productsResponse = await fetch('http://localhost:9000/products_joined');
    const productsData = await productsResponse.json();

    return {
        categories: categoriesData !== null ? categoriesData : [],
        products: productsData !== null ? productsData : []
    };
}