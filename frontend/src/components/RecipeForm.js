import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Form.css';

const RecipeForm = ({ token }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [ingredients, setIngredients] = useState([]);
  const [newIngredient, setNewIngredient] = useState({ ingredient_id: null, unit_id: null, quantity_id: null });
  const [allIngredients, setAllIngredients] = useState([]);
  const [allUnits, setAllUnits] = useState([]);
  const [allQuantities, setAllQuantities] = useState([]);
  const [recipes, setRecipes] = useState([]); // Nuevo estado para las recetas

  // Cargar datos desde la API al iniciar
  useEffect(() => {
    axios.get('http://localhost:8000/recipes/ingredients', { headers: { Authorization: `Bearer ${token}` } })
      .then(response => setAllIngredients(response.data))
      .catch(err => console.error('Error fetching ingredients:', err));

    axios.get('http://localhost:8000/recipes/units', { headers: { Authorization: `Bearer ${token}` } })
      .then(response => setAllUnits(response.data))
      .catch(err => console.error('Error fetching units:', err));

    axios.get('http://localhost:8000/recipes/quantities', { headers: { Authorization: `Bearer ${token}` } })
      .then(response => setAllQuantities(response.data))
      .catch(err => console.error('Error fetching quantities:', err));

    fetchRecipes(); // Cargar todas las recetas al iniciar
  }, [token]);

  // Función para obtener todas las recetas
  const fetchRecipes = async () => {
    try {
      const response = await axios.get('http://localhost:8000/recipes', { headers: { Authorization: `Bearer ${token}` } });
      // Ordenar las recetas alfabéticamente por título
      const sortedRecipes = response.data.sort((a, b) => a.title.localeCompare(b.title));
      setRecipes(sortedRecipes);
    } catch (error) {
      console.error('Error fetching recipes:', error);
    }
  };

  // Agregar un nuevo ingrediente
  const handleAddIngredient = () => {
    if (newIngredient.ingredient_id && newIngredient.unit_id && newIngredient.quantity_id) {
      setIngredients([...ingredients, newIngredient]);
      setNewIngredient({ ingredient_id: null, unit_id: null, quantity_id: null });
    }
  };

  // Manejar el envío del formulario
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!title || !description || ingredients.length === 0) {
      alert('Please fill in all fields');
      return;
    }

    const recipeData = {
      title,
      description,
      owner_id: 1,
      ingredients
    };

    try {
      await axios.post('http://localhost:8000/recipes', recipeData, { headers: { Authorization: `Bearer ${token}` } });
      setTitle('');
      setDescription('');
      setIngredients([]);
      fetchRecipes(); // Actualizar la lista de recetas después de agregar una nueva
    } catch (error) {
      console.error('Error creating recipe:', error);
    }
  };

  return (
    <div>
      {/* Formulario para crear receta */}
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

      {/* Mostrar recetas existentes */}
      <div className="recipes-list">
        <h2>Saved Recipes</h2>
        {recipes.map((recipe) => (
          <div key={recipe.id} className="recipe-card">
            <h3>{recipe.title}</h3>
            <p>{recipe.description}</p>
            <ul>
              {recipe.ingredients.map((ing, index) => (
                <li key={index}>
                  Ingredient ID: {ing.ingredient_id}, Unit ID: {ing.unit_id}, Quantity ID: {ing.quantity_id}
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RecipeForm;
