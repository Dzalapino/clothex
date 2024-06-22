import { writable } from 'svelte/store';

// Define the session store
export const session = writable({});

// Fetch session from the server using the stored token
export async function fetchSession() {
  if (typeof window !== 'undefined') { // Check if window is available
    const token = localStorage.getItem('token');
    if (token) {
      try {
        const response = await fetch('http://localhost:8000/auth/me', {
          headers: { 'Authorization': `Bearer ${token}` }
        });

        if (response.ok) {
          const data = await response.json();
          session.set(data); // Set session with user data
        } else {
          session.set({}); // Clear session if token is invalid
        }
      } catch (error) {
        session.set({}); // Clear session on error
      }
    } else {
      session.set({}); // Clear session if no token
    }
  }
}

// Initialize the session store on page load
if (typeof window !== 'undefined') {
  fetchSession();
}
