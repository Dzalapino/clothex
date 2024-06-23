<script>
  import { goto } from '$app/navigation';
  import { session } from '$lib/session';

  let email = '';
  let password = '';
  let confirmPassword = '';
  let errorMessage = '';
  let successMessage = '';

  async function handleRegister() {
    if (password !== confirmPassword) {
      errorMessage = "Passwords do not match.";
      return;
    }

    try {
      const response = await fetch('http://localhost:9000/auth/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
      });

      if (!response.ok) {
        const data = await response.json();
        errorMessage = data.detail || 'Failed to register';
        return;
      }

      const data = await response.json();
      session.set({ user: { email }, token: data.access_token });
      successMessage = "Registration successful! Redirecting to shopping page...";
      setTimeout(() => goto('/shopping'), 2000);
    } catch (error) {
      errorMessage = error.message;
    }
  }
</script>

<div class="auth-container">
  <h1>Register</h1>
  <form on:submit|preventDefault={handleRegister}>
    <div class="form-group">
      <label>Email:</label>
      <input type="email" bind:value={email} required />
    </div>
    <div class="form-group">
      <label>Password:</label>
      <input type="password" bind:value={password} required />
    </div>
    <div class="form-group">
      <label>Confirm Password:</label>
      <input type="password" bind:value={confirmPassword} required />
    </div>
    <button type="submit">Register</button>
    {#if errorMessage}
      <p class="error">{errorMessage}</p>
    {/if}
    {#if successMessage}
      <p class="success">{successMessage}</p>
    {/if}
  </form>
  <p class="login-link">Already have an account? <a href="/login">Login here</a>.</p>
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

  .success {
    color: #27ae60;
    margin-top: 1em;
  }

  .login-link {
    margin-top: 1.5em;
  }

  .login-link a {
    color: #c0392b;
    text-decoration: none;
  }

  .login-link a:hover {
    text-decoration: underline;
  }
</style>
