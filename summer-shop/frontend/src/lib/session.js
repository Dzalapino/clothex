// lib/session.js

import { writable } from 'svelte/store';

// Define the session store
export const session = writable({});

// Fetch session from the server using the stored token
export async function fetchSession() {
  if (typeof window !== 'undefined') { // Check if window is available
    const token = localStorage.getItem('token');
    console.log('Token:', token); // Log token for debugging
    if (token) {
      try {
        const response = await fetch('http://localhost:9000/auth/me', {
          headers: { 'Authorization': `Bearer ${token}` }
        });

        console.log('Response status:', response.status); // Log response status

        if (response.ok) {
          const data = await response.json();
          console.log('Session data fetched:', data); // Log session data
          if (data.role) {
            session.set(data); // Set session with user data
          } else {
            console.error('Role not found in session data:', data);
            session.set({}); // Clear session if role is missing
          }
        } else {
          console.error('Failed to fetch session:', response.status);
          session.set({}); // Clear session if token is invalid
        }
      } catch (error) {
        console.error('Error fetching session:', error);
        session.set({}); // Clear session on error
      }
    } else {
      console.warn('No token found');
      session.set({}); // Clear session if no token
    }
  }
}

// Initialize the session store on page load
if (typeof window !== 'undefined') {
  fetchSession();
}
