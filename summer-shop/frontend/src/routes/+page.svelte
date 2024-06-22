<script>
    export let data = [];
</script>

<div class="welcome-div">
    <h1>Welcome to Clothex Summer!</h1>
    <p>Here you can find that Hawaii shirts you craved so long and many other things</p>
    <p>Enjoy your stay!</p>
    <p>
        And if you seek clothes for hiking or other outdoor adventures, don't forget to check our
        <a class="outdoor" href="http://localhost:4200/">outdoor</a> page!
    </p>
    <div class="products">
        <h2>Some inspirations for your stylish persona:</h2>
        <div class="product-grid">
            {#each data.products as {id, amount_in_stock, name, image_url, price_pln}}
                <a class="product" href={`/shopping/${id}`} title={`View ${name}`}>
                    <img src={image_url} alt={name} class="product-image" />
                    <div class="product-details">
                        <h3>{name}</h3>
                        <h3>{price_pln} PLN</h3>
                        <p>{amount_in_stock} in stock</p>
                    </div>
                </a>
            {/each}
        </div>
    </div>
</div>

<style>
    /* Welcome div styling */
    .welcome-div {
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: rgba(243, 180, 180, 0.8); /* Light red for background */
        border: 3px solid #c0392b; /* Dark red border */
        border-radius: 1em;
        padding: 2em;
        max-width: 800px;
        margin: 2em auto;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    }

    /* Heading styling */
    h1 {
        font-family: "Caladea", cursive;
        color: #c0392b; /* Dark red color */
        margin-bottom: 1em;
    }

    /* Subheading for products */
    h2 {
        font-family: "Caladea", cursive;
        color: #b33;
        margin-bottom: 1em;
    }

    /* Paragraph styling */
    p {
        font-family: "Caladea", cursive;
        color: #333;
        text-align: center;
        margin: 0.5em 0;
    }

    /* Outdoor link */
    a.outdoor {
        font-family: "Caladea", cursive;
        color: #c0392b; /* Matches color scheme */
        font-style: italic;
        font-weight: bold;
        text-decoration: none;
        transition: color 0.3s ease;
    }

    a.outdoor:hover {
        color: #ffdd57; /* Hover effect matches yellow in logo */
    }

    /* Product grid */
    .products {
        width: 100%;
        margin-top: 2em;
    }

    .product-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 1.5em;
    }

    /* Individual product styling */
    .product {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        text-decoration: none;
        border: 2px solid #c0392b;
        border-radius: 0.5em;
        padding: 1em;
        background-color: #fff;
        transition: transform 0.3s, box-shadow 0.3s;
    }

    .product:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .product-image {
        width: 100%;
        height: auto;
        max-width: 150px;
        border-radius: 0.5em;
        margin-bottom: 1em;
    }

    .product-details {
        color: #333;
    }

    .product h3 {
        font-family: "Caladea", cursive;
        font-size: 1.1em;
        margin: 0.5em 0;
    }

    .product p {
        font-family: Arial, sans-serif;
        font-size: 0.9em;
        color: #777;
        margin: 0;
    }
</style>
