<script>
    export let data = [];
</script>

<div class="welcome-div">
    <h1>Welcome to Clothex Summer!</h1>
    <p>Here you can find that hawaii shirts you craved so long and many other things</p>
    <p>Enjoy your stay!</p>
    <p>
        And if you seek clothes for hiking or other outdoor adventures, don't forget to check our
        <a class="outdoor" href="shopping">outdoor</a> page! <!-- TODO: Integrate a link to outdoor -->
    </p>
    <div class="">
        <h1>Some inspirations for your stylish persona:</h1>
        {#each data.products as {id, amount_in_stock}}
            <div class="product">
                <p>id: {id}</p>
                <p>amount in stock: {amount_in_stock}</p>
            </div>
        {/each}
    </div>
</div>

<style>
    div.welcome-div {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: rgba(200,150,150,0.72);
        border: darkred 3px solid;
        border-radius: 2em;
    }
    h1 {
        font-family: "Caladea", cursive;
        color: #333;
        align-self: center;
    }
    p {
        font-family: "Caladea", cursive;
        color: #333;
    }
    a.outdoor {
        font-family: "Caladea", cursive;
        color: #33f;
        font-style: italic;
        font-weight: bold;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    a.outdoor:hover {
        color: #33a;
    }
</style>