<script>
  export let data = {categories: [], products: []};

  let category = '';
  let minPrice = 0;
  let maxPrice = 0;

  let filteredProducts = [];

  // Filter products based on the criteria
  const filterProducts = () => {
    if (!data || !data.products) return [];

    filteredProducts = data.products.filter(product => {
      return ((product.category === category || category === '') &&
        (product.price_pln >= minPrice || minPrice === 0 || minPrice === null) &&
        (product.price_pln <= maxPrice || maxPrice === 0 || maxPrice === null));
    });

    console.log(filteredProducts);
  }

  // Initialize filteredProducts on mount
  $: filteredProducts = data.products;
</script>

<div class="shopping-container">
  <h1>Our Collection</h1>

  <div class="filter-form">
    <label>
      Category:
      <select bind:value={category} on:change={filterProducts}>
        <option value="">All</option>
        {#each data.categories as category}
          <option value={category}>{category}</option>
        {/each}
      </select>
    </label>

    <label>
      Min Price:
      <input type="number" bind:value={minPrice} min="0" on:input={filterProducts}/>
    </label>

    <label>
      Max Price:
      <input type="number" bind:value={maxPrice} min="0" on:input={filterProducts}/>
    </label>
  </div>

  <div class="product-grid">
    {#if filteredProducts.length > 0}
      {#each filteredProducts as { id, name, image_url, price_pln, amount_in_stock }}
        <a href={`/shopping/${id}`} class="product-card">
          <img src={image_url} alt={name} class="product-image" />
          <div class="product-info">
            <h3>{name}</h3>
            <h3>{price_pln} PLN</h3>
            <p>{amount_in_stock} in stock</p>
          </div>
        </a>
      {/each}
    {:else}
      <p>No products found matching the criteria.</p>
    {/if}
  </div>
</div>

<style>
  .shopping-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
    background-color: rgba(243, 180, 180, 0.8);
    border: 3px solid #c0392b;
    border-radius: 1em;
    max-width: 1200px;
    margin: 2em auto;
  }

  h1 {
    font-family: "Caladea", cursive;
    color: #c0392b;
    margin-bottom: 1.5em;
  }

  .filter-form {
    display: flex;
    gap: 1em;
    margin-bottom: 2em;
  }

  .filter-form label {
    font-family: Arial, sans-serif;
    font-size: 0.9em;
    color: #333;
  }

  .filter-form input,
  .filter-form select {
    margin-left: 0.5em;
    padding: 0.5em;
    border: 1px solid #ccc;
    border-radius: 0.5em;
  }

  .admin-controls {
    display: flex;
    gap: 1em;
    margin-bottom: 2em;
  }

  .admin-controls button {
    padding: 0.5em 1em;
    border: none;
    border-radius: 0.5em;
    background-color: #c0392b;
    color: #fff;
    font-family: Arial, sans-serif;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  .admin-controls button:hover {
    background-color: #a32e22;
  }

  .product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1.5em;
    width: 100%;
  }

  .product-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    background-color: #fff;
    border: 2px solid #c0392b;
    border-radius: 0.5em;
    padding: 1em;
    transition: transform 0.3s, box-shadow 0.3s;
    text-decoration: none;
    color: inherit;
  }

  .product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }

  .product-image {
    width: 100%;
    height: auto;
    max-width: 150px;
    border-radius: 0.5em;
    margin-bottom: 0.5em;
  }

  .product-info {
    color: #333;
  }

  .product-info h3 {
    font-family: "Caladea", cursive;
    font-size: 1.1em;
    margin: 0.5em 0;
  }

  .product-info p {
    font-family: Arial, sans-serif;
    font-size: 0.9em;
    color: #777;
    margin: 0;
  }

  @media (max-width: 768px) {
    .shopping-container {
      padding: 1em;
    }

    .product-grid {
      grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
      gap: 1em;
    }

    .product-image {
      max-width: 100px;
    }
  }
</style>
