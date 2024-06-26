<script>
  import { session } from '$lib/session';
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  let user = {}; // Local user state
  let email = '';
  let name = '';
  let errorMessage = '';
  let successMessage = '';

  // Subscribe to session to get the current user info
  session.subscribe(value => {
    user = value.user || {};
    email = user.email || '';
    name = user.name || '';
  });

  async function updateProfile() {
    // Assuming your backend requires authentication token for profile update
    const token = localStorage.getItem('token');

    if (!token) {
      errorMessage = 'You are not logged in!';
      return;
    }

    try {
      const response = await fetch('http://localhost:9000/auth/update', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          email,
          name
        })
      });

      if (!response.ok) {
        const data = await response.json();
        errorMessage = data.detail || 'Failed to update profile';
        return;
      }

      const data = await response.json();
      successMessage = 'Profile updated successfully!';
      session.set({ ...session, user: data.user }); // Update session store
    } catch (error) {
      errorMessage = error.message;
    }
  }

  // Redirect to login if not authenticated
  onMount(() => {
    if (!user.email) {
      goto('/login');
    }
  });
</script>

<div class="profile-container">
  <h1>Your Profile</h1>
  <form on:submit|preventDefault={updateProfile}>
    <div class="form-group">
      <label>Email:</label>
      <input type="email" bind:value={email} required readonly/>
    </div>
    <div class="form-group">
      <label>Name:</label>
      <input type="text" bind:value={name} required />
    </div>
    <button type="submit">Update Profile</button>
    {#if errorMessage}
      <p class="error">{errorMessage}</p>
    {/if}
    {#if successMessage}
      <p class="success">{successMessage}</p>
    {/if}
  </form>
</div>

<style>
  .profile-container {
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
</style>
