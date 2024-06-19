<div class="navbar">
    <div class="logo">
        <a class="logo-link" href="/">
            <span class="logo-cloth">cloth</span>
            <span class="logo-ex">ex</span>
            <span class="logo-summer">summer</span>
        </a>
    </div>
    <nav>
        <a href="shopping">shopping</a>
        <a href="about">about</a>
        <a href="contact">contact</a>
    </nav>
</div>

<style>
    .logo {
        display: flex;
        align-items: start;
    }
    .logo-cloth {
        font-family: Verdana;
        font-style: italic;
        color: #eee; /* Change this to the color you want for "cloth" */
        font-size: 1.5em;
        text-decoration: none;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: color 0.3s ease;
    }
    .logo-ex {
        font-family: Verdana;
        font-style: italic;
        font-weight: bold;
        color: #b33;
        font-size: 2em;
        margin-left: -0.2em;
        transition: color 0.3s ease;
    }
    .logo-summer {
        font-family: Verdana;
        font-style: italic;
        color: #ee0;
        font-size: 2em;
        text-decoration: none;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: color 0.3s ease;
    }
    .logo-link:hover .logo-cloth,
    .logo-link:hover .logo-summer {
        color: #b33;
    }
    a {
        font-family: Verdana;
        color: #eee;
        text-decoration: none;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin: 0 3em;
        transition: color 0.3s ease;
    }
    a:hover {
        color: #555;
    }
    div.navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1em;
        background-color: rgba(156,50,50,0.72);
        border: darkred 3px solid;
        border-radius: 2em;
    }
</style>

<slot>

</slot>