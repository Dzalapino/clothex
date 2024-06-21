<script>
  import { goto } from '$app/navigation';
  import { session } from '$lib/session';
  import { onMount } from 'svelte';

  let username = '';  // Change to 'username' to match backend
  let password = '';
  let errorMessage = '';

async function handleLogin() {
  try {
    const response = await fetch('http://localhost:8000/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: new URLSearchParams({
        username: username,  // Keep this as 'username' to match the backend
        password: password
      })
    });

    if (!response.ok) {
      const data = await response.json();
      errorMessage = data.detail || 'Failed to login';
      return;
    }

    const data = await response.json();
    session.set({ user: { username }, token: data.access_token });
    localStorage.setItem('token', data.access_token);  // Store token in localStorage
    goto('/shopping'); // Redirect after login
  } catch (error) {
    errorMessage = error.message;
  }
}

  onMount(() => {
    if (session.user) {
      goto('/shopping');
    }
  });
</script>


<div class="auth-container">
  <h1>Login</h1>
  <form on:submit|preventDefault={handleLogin}>
    <div class="form-group">
      <label>Email:</label>
      <input type="email" bind:value={username} required/>
    </div>
    <div class="form-group">
      <label>Password:</label>
      <input type="password" bind:value={password} required/>
    </div>
    <button type="submit">Login</button>
    {#if errorMessage}
      <p class="error">{errorMessage}</p>
    {/if}
  </form>
  <p class="register-link">Don't have an account? <a href="/register">Register here</a>.</p>
</div>

<style>
  .auth-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
    background-color: rgba(243, 180, 180, 0.8);
    border: 3px solid #c0392b;
    border-radius: 1em;
    max-width: 400px;
    margin: 2em auto;
  }

  h1 {
    font-family: "Caladea", cursive;
    color: #c0392b;
    margin-bottom: 1.5em;
  }

  form {
    display: flex;
    flex-direction: column;
    width: 100%;
  }

  .form-group {
    margin-bottom: 1em;
  }

  .form-group label {
    font-family: Arial, sans-serif;
    color: #333;
    margin-bottom: 0.5em;
    display: block;
  }

  .form-group input {
    width: 100%;
    padding: 0.5em;
    border: 1px solid #ccc;
    border-radius: 0.5em;
  }

  button {
    padding: 0.5em 1em;
    border: none;
    border-radius: 0.5em;
    background-color: #c0392b;
    color: #fff;
    font-family: Arial, sans-serif;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  button:hover {
    background-color: #a32e22;
  }

  .error {
    color: #e74c3c;
    margin-top: 1em;
  }

  .register-link {
    margin-top: 1.5em;
  }

  .register-link a {
    color: #c0392b;
    text-decoration: none;
  }

  .register-link a:hover {
    text-decoration: underline;
  }
</style>
