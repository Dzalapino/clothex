<script>
  import { session } from '$lib/session';
  import { goto } from '$app/navigation';
  import { page } from '$app/stores';
  import { onMount } from 'svelte';

  let userSession;

  // Reactive declaration to subscribe to the session store
  session.subscribe(value => {
    userSession = value;
  });

  async function logout() {
    if (typeof window !== 'undefined') { // Ensure we're in the browser
      localStorage.removeItem('token'); // Clear stored token
      session.set({}); // Clear session
      await goto('/'); // Redirect to homepage or login page
    }
  }

  // Ensure session is fetched on mount
  onMount(() => {
    session.subscribe(value => {
      console.log("Session updated:", value);
    });
  });
</script>

<div class="navbar">
  <div class="logo">
    <a class="logo-link" href="/">
      <span class="logo-cloth">cloth</span>
      <span class="logo-ex">ex</span>
      <span class="logo-summer">summer</span>
    </a>
  </div>
  <nav>
    <a href="/shopping">shopping</a>
    <a href="/about">about</a>
    <a href="/contact">contact</a>
    {#if userSession?.user?.email}
      <!-- Additional options for admin users -->
      {#if userSession.user.role === 'admin'}
        <a href="/admin">admin</a>
      {/if}
      <a href="/profile">profile</a>
      <a href="/" on:click|preventDefault={logout}>Logout</a>
    {:else}
      <!-- Show login link only if the current page is not the login page -->
      {#if $page.url.pathname !== '/login'}
        <a href="/login">Login</a>
      {/if}
    {/if}
  </nav>
</div>

<style>
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1em 2em;
    background-color: #b33;
    border-bottom: 4px solid #c0392b;
    border-radius: 0 0 1em 1em;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    position: relative;
    z-index: 10;
  }

  .logo {
    display: flex;
    align-items: center;
  }

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
    color: #ff6f61;
    font-size: 1.8em;
    margin-left: -0.1em;
  }

  .logo-summer {
    color: #ffdd57;
    font-size: 1.5em;
    letter-spacing: 2px;
  }

  .logo-link:hover .logo-cloth {
    color: #ff6f61;
  }

  .logo-link:hover .logo-summer {
    color: #c0392b;
  }

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
    color: #ffdd57;
  }

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

<slot/>
