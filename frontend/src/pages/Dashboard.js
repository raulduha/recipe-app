import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useAuth } from '../hooks/useAuth';
import './Dashboard.css';

const Dashboard = () => {
  const { token } = useAuth();

  // Estados para la creación de recetas
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [ingredients, setIngredients] = useState([]);
  const [newIngredient, setNewIngredient] = useState({ ingredient_id: null, unit_id: null, quantity_id: null });

  // Estados para obtener datos de la API
  const [allIngredients, setAllIngredients] = useState([]);
  const [allUnits, setAllUnits] = useState([]);
  const [allQuantities, setAllQuantities] = useState([]);
  const [recipes, setRecipes] = useState([]);

  // Cargar todos los datos necesarios al iniciar
  useEffect(() => {
    fetchIngredients();
    fetchUnits();
    fetchQuantities();
    fetchRecipes();
  }, [token]);

  // Funciones para obtener datos desde la API
  const fetchIngredients = async () => {
    try {
      const response = await axios.get('http://localhost:8000/recipes/ingredients', { headers: { Authorization: `Bearer ${token}` } });
      setAllIngredients(response.data);
    } catch (error) {
      console.error('Error fetching ingredients:', error);
    }
  };

  const fetchUnits = async () => {
    try {
      const response = await axios.get('http://localhost:8000/recipes/units', { headers: { Authorization: `Bearer ${token}` } });
      setAllUnits(response.data);
    } catch (error) {
      console.error('Error fetching units:', error);
    }
  };

  const fetchQuantities = async () => {
    try {
      const response = await axios.get('http://localhost:8000/recipes/quantities', { headers: { Authorization: `Bearer ${token}` } });
      setAllQuantities(response.data);
    } catch (error) {
      console.error('Error fetching quantities:', error);
    }
  };

  const fetchRecipes = async () => {
    try {
      const response = await axios.get('http://localhost:8000/recipes', { headers: { Authorization: `Bearer ${token}` } });
      setRecipes(response.data.sort((a, b) => a.title.localeCompare(b.title)));
    } catch (error) {
      console.error('Error fetching recipes:', error);
    }
  };

  // Manejar el envío del formulario para crear una receta
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!title || !description || ingredients.length === 0) {
      alert('Please fill in all fields');
      return;
    }

    const recipeData = {
      title,
      description,
      owner_id: 1, // Cambiar según el usuario actual
      ingredients
    };

    try {
      await axios.post('http://localhost:8000/recipes', recipeData, { headers: { Authorization: `Bearer ${token}` } });
      setTitle('');
      setDescription('');
      setIngredients([]);
      fetchRecipes(); // Actualizar lista de recetas
    } catch (error) {
      console.error('Error creating recipe:', error);
    }
  };

  // Agregar un nuevo ingrediente
  const handleAddIngredient = () => {
    if (newIngredient.ingredient_id && newIngredient.unit_id && newIngredient.quantity_id) {
      setIngredients([...ingredients, newIngredient]);
      setNewIngredient({ ingredient_id: null, unit_id: null, quantity_id: null });
    }
  };

  return (
    <div className="dashboard">
      <h2>Recipe Dashboard</h2>

      {/* Formulario para crear una receta */}
      <form onSubmit={handleSubmit} className="recipe-form">
        <input
          type="text"
          placeholder="Recipe Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />

        <h4>Add Ingredients</h4>
        <div className="button-group">
          <h5>Select Ingredient:</h5>
          {allIngredients.map(ing => (
            <button
              key={ing.id}
              type="button"
              className={newIngredient.ingredient_id === ing.id ? 'selected' : ''}
              onClick={() => setNewIngredient({ ...newIngredient, ingredient_id: ing.id })}
            >
              {ing.name}
            </button>
          ))}
        </div>

        <div className="button-group">
          <h5>Select Unit:</h5>
          {allUnits.map(unit => (
            <button
              key={unit.id}
              type="button"
              className={newIngredient.unit_id === unit.id ? 'selected' : ''}
              onClick={() => setNewIngredient({ ...newIngredient, unit_id: unit.id })}
            >
              {unit.unit}
            </button>
          ))}
        </div>

        <div className="button-group">
          <h5>Select Quantity:</h5>
          {allQuantities.map(qty => (
            <button
              key={qty.id}
              type="button"
              className={newIngredient.quantity_id === qty.id ? 'selected' : ''}
              onClick={() => setNewIngredient({ ...newIngredient, quantity_id: qty.id })}
            >
              {qty.quantity}
            </button>
          ))}
        </div>

        <button type="button" onClick={handleAddIngredient}>Add Ingredient</button>

        <ul>
          {ingredients.map((ing, index) => (
            <li key={index}>
              {allIngredients.find(i => i.id === ing.ingredient_id)?.name} - 
              {allUnits.find(u => u.id === ing.unit_id)?.unit} - 
              {allQuantities.find(q => q.id === ing.quantity_id)?.quantity}
            </li>
          ))}
        </ul>

        <button type="submit">Add Recipe</button>
      </form>

      {/* Mostrar recetas guardadas */}
      <div className="recipes-list">
        <h2>Saved Recipes</h2>
        {recipes.map((recipe) => (
          <div key={recipe.id} className="recipe-card">
            <h3>{recipe.title}</h3>
            <p>{recipe.description}</p>
            <ul>
              {recipe.ingredients.map((ing, index) => (
                <li key={index}>
                  {allIngredients.find(i => i.id === ing.ingredient_id)?.name} - 
                  {allUnits.find(u => u.id === ing.unit_id)?.unit} - 
                  {allQuantities.find(q => q.id === ing.quantity_id)?.quantity}
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
