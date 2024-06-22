<script>
    import { onMount } from 'svelte';
    import { page } from '$app/stores';
    import { get, subscribe } from 'svelte/store';
    import { session } from '$lib/session';

    let product = {};
    let productId;
    let isAdmin = false;
    let newStockAmount = 0;

    // Using reactive statement to watch for changes in the $page store
    $: {
        const pageData = get(page);
        productId = pageData.params.id;
    }

    // Watch session for changes to determine if user is admin
    $: {
        subscribe(session, value => {
            console.log('Session data in component:', value); // Log session data in component
            isAdmin = value.role === 'admin';
        });
    }

    // Fetch product data when component mounts
    onMount(fetchProduct);

    // Function to fetch product data
    async function fetchProduct() {
        if (!productId) return;

        try {
            console.log(`Fetching product with ID: ${productId}`);
            const response = await fetch(`http://localhost:9000/products_joined/${productId}`);
            if (!response.ok) {
                throw new Error('Failed to fetch product data');
            }
            product = await response.json();
            console.log('Fetched product:', product);
        } catch (error) {
            console.error('Error fetching product data:', error);
        }
    }

    // Function to handle adding to cart
    function addToCart() {
        console.log(`Adding product ${product.name} to cart`);
    }

    // Function to handle adding more stock
    async function addMoreStock() {
        if (!newStockAmount || newStockAmount <= 0) return;

        try {
            const response = await fetch(`http://localhost:9000/products_joined/${productId}/stock`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({amount: newStockAmount}),
            });

            if (response.ok) {
                const updatedProduct = await response.json();
                product = updatedProduct; // Update local product data
                newStockAmount = 0; // Reset input field
                console.log('Stock updated successfully:', updatedProduct);
            } else {
                console.error('Failed to update stock');
            }
        } catch (error) {
            console.error('Error updating stock:', error);
        }
    }
</script>
