<script>
    export let data; // Product data is passed as a prop

        function addToCart() {
        console.log("Product added to cart:", data.product);
    }

    function notifyMe() {
        console.log("Notification request for product:", data.product);
    }
</script>


<div class="product-detail-container">
    <h1>{data.product.name}</h1>
    <div class="product-detail">
        <img src="../{data.product.image_url}" alt={data.product.name} class="product-detail-image"/>
        <div class="product-detail-info">
            <h2>{data.product.name}</h2>
            <p><strong>Price:</strong> {data.product.price_pln}</p>
            <p><strong>Description:</strong></p>
            <p>{data.product.description}</p>
            <p><strong>Amount in stock:</strong> {data.product.amount_in_stock}</p>
            {#if data.product.amount_in_stock > 0}
                <button on:click={addToCart}>Add to Cart</button>
            {:else}
                <button on:click={notifyMe}>Email me when available</button>
            {/if}
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