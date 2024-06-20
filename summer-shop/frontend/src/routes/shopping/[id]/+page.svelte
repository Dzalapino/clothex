<script>
    import { onMount } from 'svelte';
    import { page } from '$app/stores';

    let product = {};
    let productId;

    $: {
        productId = $page.params.id; // Get the product ID from the URL
    }

    // Print the product ID to the console
    console.log(productId);

    onMount(async () => {
        try {
            const response = await fetch(`https://api.example.com/products/${productId}`); // Replace with actual API URL
            product = await response.json();
        } catch (error) {
            console.error('Error fetching product data:', error);
        }
    });

    function addToCart() {
        // Implement add to cart functionality
    }
</script>

<div class="product-detail-container">
    <h1>{product.name}</h1>
    <div class="product-detail">
        <img src={product.imageUrl} alt={product.name} class="product-detail-image" />
        <div class="product-detail-info">
            <h2>{product.name}</h2>
            <p>{product.description}</p>
            <p><strong>Price:</strong> {product.price}</p>
            <button on:click={addToCart}>Add to Cart</button>
        </div>
    </div>
</div>

<style>
    .product-detail-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 2em;
        background-color: rgba(243, 180, 180, 0.8);
        border: 3px solid #c0392b;
        border-radius: 1em;
        max-width: 800px;
        margin: 2em auto;
    }

    .product-detail {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .product-detail-image {
        width: 100%;
        height: auto;
        max-width: 300px;
        border-radius: 0.5em;
        margin-bottom: 1em;
    }

    .product-detail-info {
        color: #333;
        text-align: center;
    }

    .product-detail-info h2 {
        font-family: "Caladea", cursive;
        color: #c0392b;
        margin-bottom: 0.5em;
    }

    .product-detail-info p {
        font-family: Arial, sans-serif;
        margin-bottom: 0.5em;
    }

    button {
        background-color: #c0392b;
        color: #fff;
        border: none;
        padding: 0.5em 1em;
        border-radius: 0.5em;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    button:hover {
        background-color: #ff6f61;
    }
</style>
