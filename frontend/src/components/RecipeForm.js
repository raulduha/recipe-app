import React, { useState } from 'react';
import './Form.css';

const RecipeForm = ({ addRecipe }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [ingredients, setIngredients] = useState('');
  const [category, setCategory] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const ingredientList = ingredients.split(',').map((item) => item.trim());
    addRecipe({ title, description, ingredients: ingredientList, category });
    setTitle('');
    setDescription('');
    setIngredients('');
    setCategory('');
  };

  return (
    <form onSubmit={handleSubmit} className="recipe-form">
      <input type="text" placeholder="Recipe Title" value={title} onChange={(e) => setTitle(e.target.value)} />
      <textarea placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} />
      <input type="text" placeholder="Ingredients (comma-separated)" value={ingredients} onChange={(e) => setIngredients(e.target.value)} />
      <select value={category} onChange={(e) => setCategory(e.target.value)}>
        <option value="">Select Category</option>
        <option value="Main Course">Main Course</option>
        <option value="Salad">Salad</option>
        <option value="Dessert">Dessert</option>
      </select>
      <button type="submit">Add Recipe</button>
    </form>
  );
};

export default RecipeForm;
