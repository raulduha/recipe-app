-- Table to store users
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,  -- Store hashed passwords for security
    role VARCHAR(50) DEFAULT 'user',      -- Optional: for role-based access control
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store recipes
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,  -- Foreign key to users table (only allows user to manage their recipes)
    title VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store ingredients
CREATE TABLE ingredients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

-- Table to store units of measurement (e.g., cups, teaspoons)
CREATE TABLE units_of_measurement (
    id SERIAL PRIMARY KEY,
    unit VARCHAR(50) UNIQUE NOT NULL
);

-- Table to store predefined quantities for ingredients (e.g., 1, 2, etc.)
CREATE TABLE quantities (
    id SERIAL PRIMARY KEY,
    quantity DECIMAL NOT NULL  -- Store the quantity as a decimal
);

-- Table to store tags for recipes (e.g., main course, dessert)
CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

-- Many-to-many relationship table between recipes and tags
CREATE TABLE recipe_tags (
    recipe_id INT REFERENCES recipes(id) ON DELETE CASCADE,
    tag_id INT REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (recipe_id, tag_id)
);

-- Many-to-many relationship table between recipes and ingredients
CREATE TABLE recipe_ingredients (
    recipe_id INT REFERENCES recipes(id) ON DELETE CASCADE,
    ingredient_id INT REFERENCES ingredients(id) ON DELETE CASCADE,
    unit_id INT REFERENCES units_of_measurement(id),
    quantity_id INT REFERENCES quantities(id),
    PRIMARY KEY (recipe_id, ingredient_id)
);

-- Table to store the users allowed to register for the application (restricted access)
CREATE TABLE allowed_users (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    registration_allowed BOOLEAN DEFAULT TRUE,  -- Indicates whether a user can register
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

