import React, { useState } from 'react';
import RecipeList from '../components/RecipeList';
import RecipeForm from '../components/RecipeForm';
import './Dashboard.css';

const Dashboard = () => {
  const [recipes, setRecipes] = useState([
    {
      id: 1,
      title: 'Spaghetti Bolognese',
      description: 'Delicious spaghetti with rich tomato sauce and minced meat.',
      ingredients: ['Spaghetti', 'Tomato', 'Minced meat', 'Garlic', 'Olive oil'],
      category: 'Main Course'
    },
    {
      id: 2,
      title: 'Caesar Salad',
      description: 'A classic Caesar salad with crispy croutons and Parmesan.',
      ingredients: ['Romaine lettuce', 'Croutons', 'Parmesan', 'Caesar dressing'],
      category: 'Salad'
    }
  ]);

  const addRecipe = (newRecipe) => {
    setRecipes([...recipes, { id: recipes.length + 1, ...newRecipe }]);
  };

  return (
    <div className="dashboard">
      <h2>Your Recipe Dashboard</h2>
      <RecipeForm addRecipe={addRecipe} />
      <RecipeList recipes={recipes} />
    </div>
  );
};

export default Dashboard;
