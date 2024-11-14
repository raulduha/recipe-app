import React, { useState, useEffect, useCallback } from 'react';
import { getRecipes, createRecipe } from '../services/api';
import { useAuth } from '../hooks/useAuth';
import './Dashboard.css';

const Dashboard = () => {
  const { token } = useAuth();
  const [recipes, setRecipes] = useState([]);
  const [newRecipe, setNewRecipe] = useState({
    title: '',
    description: '',
    ingredients: []
  });
  const [newIngredient, setNewIngredient] = useState('');

  // Fetch all recipes on initial load
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

  // Handle creating a new recipe
  const handleCreateRecipe = async (e) => {
    e.preventDefault();

    if (!newRecipe.title || !newRecipe.description || newRecipe.ingredients.length === 0) {
      alert('Please fill in all fields and add at least one ingredient');
      return;
    }

    try {
      const recipeData = {
        ...newRecipe,
        ingredients: newRecipe.ingredients.map(ingredient => ingredient.trim()) // Ensure ingredients are clean
      };

      const response = await createRecipe(recipeData, token);
      setRecipes((prevRecipes) => [...prevRecipes, response.data]);

      // Reset form
      setNewRecipe({ title: '', description: '', ingredients: [] });
      setNewIngredient('');
    } catch (error) {
      console.error('Error creating recipe:', error);
    }
  };

  // Handle adding a new ingredient
  const handleAddIngredient = () => {
    if (newIngredient.trim() !== '') {
      setNewRecipe((prevState) => ({
        ...prevState,
        ingredients: [...prevState.ingredients, newIngredient]
      }));
      setNewIngredient(''); // Clear the input field after adding
    }
  };

  // Fetch recipes initially
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
        
        <div className="ingredients-input">
          <input
            type="text"
            placeholder="Add ingredient"
            value={newIngredient}
            onChange={(e) => setNewIngredient(e.target.value)}
          />
          <button type="button" onClick={handleAddIngredient}>Add Ingredient</button>
        </div>

        <ul className="ingredients-list">
          {newRecipe.ingredients.map((ingredient, index) => (
            <li key={index}>{ingredient}</li>
          ))}
        </ul>

        <button type="submit">Add Recipe</button>
      </form>

      <div className="recipes-list">
        {recipes.length > 0 ? (
          recipes.map((recipe) => (
            <div key={recipe.id} className="recipe-card">
              <h3>{recipe.title}</h3>
              <p>{recipe.description}</p>
              <p><strong>Ingredients:</strong> {recipe.ingredients.join(', ')}</p>
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
