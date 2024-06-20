<script>
    // Add any necessary script logic here
</script>

<!-- Navbar Layout -->
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
    /* Navbar styling */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1em 2em;
        background-color: #b33; /* Matches red color scheme */
        border-bottom: 4px solid #c0392b; /* Darker red for the border */
        border-radius: 0 0 1em 1em; /* Rounded bottom corners */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        position: relative;
        z-index: 10;
    }

    /* Logo container */
    .logo {
        display: flex;
        align-items: center;
    }

    /* Logo parts */
    .logo-cloth, .logo-ex, .logo-summer {
        font-family: Verdana, sans-serif;
        font-style: italic;
        text-transform: uppercase;
        text-decoration: none;
        letter-spacing: 1px;
        transition: color 0.3s ease;
        display: inline-block;
    }

    .logo-cloth {
        color: #fff;
        font-size: 1.5em;
    }

    .logo-ex {
        font-weight: bold;
        color: #ff6f61; /* Slightly lighter red for emphasis */
        font-size: 1.8em;
        margin-left: -0.1em;
    }

    .logo-summer {
        color: #ffdd57; /* Matches yellow scheme */
        font-size: 1.5em;
        letter-spacing: 2px;
    }

    /* Hover effects for logo */
    .logo-link:hover .logo-cloth {
        color: #ff6f61;
    }

    .logo-link:hover .logo-summer {
        color: #c0392b;
    }

    /* Navbar links */
    nav {
        display: flex;
        gap: 2em;
    }

    nav a {
        font-family: Verdana, sans-serif;
        color: #fff;
        text-decoration: none;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: color 0.3s ease;
        padding: 0.5em 0;
        position: relative;
    }

    nav a:hover {
        color: #ffdd57; /* Yellow hover effect */
    }

    /* Underline effect on hover */
    nav a::after {
        content: '';
        position: absolute;
        width: 0;
        height: 2px;
        bottom: -2px;
        left: 50%;
        background-color: #ffdd57;
        transition: width 0.3s ease, left 0.3s ease;
    }

    nav a:hover::after {
        width: 100%;
        left: 0;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .navbar {
            flex-direction: column;
            align-items: flex-start;
        }

        nav {
            flex-direction: column;
            width: 100%;
        }

        nav a {
            margin-bottom: 1em;
        }
    }
</style>

<!-- Slot for page-specific content -->
<slot></slot>
