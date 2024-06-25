export async function load({ params }) {
    const { id } = params;
    const productsResponse = await fetch('http://localhost:9000/products_joined/' + id);
    const productData = await productsResponse.json();

    return {
        product: productData !== null ? productData : []
    };
}
