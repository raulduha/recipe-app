import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

// Registro de usuario
export const registerUser = async (data) => {
  return await axios.post(`${API_URL}/auth/register`, data);
};

// Inicio de sesión
export const loginUser = async (data) => {
  const response = await axios.post(`${API_URL}/auth/login`, data);
  return response.data;
};

// Obtener todas las recetas
export const getRecipes = async (token) => {
  return await axios.get(`${API_URL}/recipes/recipes`, {
    headers: { Authorization: `Bearer ${token}` }
  });
};

// Crear una nueva receta
export const createRecipe = async (data, token) => {
  return await axios.post(`${API_URL}/recipes/recipes`, data, {
    headers: { Authorization: `Bearer ${token}` }
  });
};
