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
  return await axios.get(`${API_URL}`, {
    headers: { Authorization: `${API_URL}/recipes` }
  });
};

// Crear una nueva receta
export const createRecipe = async (data, token) => {
  console.log("Sending recipe data:", data);
  try {
    const response = await axios.post(`${API_URL}/recipes`, data, {
      headers: { Authorization: `Bearer ${token}` }
    });
    return response.data;
  } catch (error) {
    console.error('Error creating recipe:', error);
    throw error;
  }
};
