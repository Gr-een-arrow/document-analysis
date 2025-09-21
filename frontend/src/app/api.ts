import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api', // You can change this to your backend base URL if needed
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;
