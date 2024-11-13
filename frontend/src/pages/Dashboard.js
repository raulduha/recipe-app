import React, { useState, useEffect, useCallback } from 'react';
import { getRecipes, createRecipe } from '../services/api';
import { useAuth } from '../hooks/useAuth';
import './Dashboard.css';

const Dashboard = () => {
  const { token } = useAuth();
  const [recipes, setRecipes] = useState([]);
  const [newRecipe, setNewRecipe] = useState({ title: '', description: '', ingredients: '' });

  // Función para cargar todas las recetas al inicio
  const fetchRecipes = useCallback(async () => {
    if (token) {
      try {
        const response = await getRecipes(token);
        setRecipes(response.data);
      } catch (error) {
        console.error('Error fetching recipes:', error);
      }
    }
  }, [token]);

  // Crear una receta y actualizar la lista en tiempo real
  const handleCreateRecipe = async (e) => {
    e.preventDefault();

    if (!newRecipe.title || !newRecipe.description || !newRecipe.ingredients) {
      alert('Please fill in all fields');
      return;
    }

    try {
      // Crear la receta y obtener la respuesta
      const response = await createRecipe(newRecipe, token);
      
      // Actualizar el estado con la nueva receta y mantener las existentes
      setRecipes((prevRecipes) => [...prevRecipes, response.data]);

      // Limpiar el formulario
      setNewRecipe({ title: '', description: '', ingredients: '' });
    } catch (error) {
      console.error('Error creating recipe:', error);
    }
  };

  // Cargar las recetas al inicio
  useEffect(() => {
    fetchRecipes();
  }, [fetchRecipes]);

  return (
    <div className="dashboard">
      <h2>Recipes Dashboard</h2>
      <form className="recipe-form" onSubmit={handleCreateRecipe}>
        <input 
          type="text" 
          placeholder="Title" 
          value={newRecipe.title}
          onChange={(e) => setNewRecipe({ ...newRecipe, title: e.target.value })} 
        />
        <input 
          type="text" 
          placeholder="Description" 
          value={newRecipe.description}
          onChange={(e) => setNewRecipe({ ...newRecipe, description: e.target.value })} 
        />
        <input 
          type="text" 
          placeholder="Ingredients" 
          value={newRecipe.ingredients}
          onChange={(e) => setNewRecipe({ ...newRecipe, ingredients: e.target.value })} 
        />
        <button type="submit">Add Recipe</button>
      </form>

      <div className="recipes-list">
        {recipes.length > 0 ? (
          recipes.map((recipe) => (
            <div key={recipe.id} className="recipe-card">
              <h3>{recipe.title}</h3>
              <p>{recipe.description}</p>
              <p><strong>Ingredients:</strong> {recipe.ingredients}</p>
            </div>
          ))
        ) : (
          <p>No recipes available</p>
        )}
      </div>
    </div>
  );
};

export default Dashboard;
