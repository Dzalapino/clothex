import { writable } from 'svelte/store';

export const session = writable({});

export async function fetchSession() {
  const token = localStorage.getItem('token');
  if (token) {
    const response = await fetch('http://localhost:8000/auth/me', {
      headers: { 'Authorization': `Bearer ${token}` }
    });

    if (response.ok) {
      const data = await response.json();
      session.set(data);
    } else {
      session.set({});
    }
  } else {
    session.set({});
  }
}
