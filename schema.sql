-- Create the Location table
CREATE TABLE location (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(255) NOT NULL,
);

-- create the category_age table
CREATE TABLE category_age (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(255) NOT NULL,
);

-- Create the physical_size table
CREATE TABLE physical_size (
    id INT AUTO_INCREMENT PRIMARY KEY,
    size VARCHAR(255) NOT NULL,
);

-- Create the owner table
CREATE TABLE owner (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
);

-- Create the pet table
CREATE TABLE pet (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    sex ENUM('M', 'F') NOT NULL,
    was_adopted BOOLEAN NOT NULL,
    specie ENUM('Cachorro', 'Gato') NOT NULL,
    location_id INT NOT NULL,
    category_age_id INT NOT NULL,
    physical_size_id INT NOT NULL,
    owner_id INT NOT NULL,
    FOREIGN KEY (location_id) REFERENCES location(id),
    FOREIGN KEY (category_age_id) REFERENCES category_age(id),
    FOREIGN KEY (physical_size_id) REFERENCES physical_size(id),
    FOREIGN KEY (owner_id) REFERENCES owner(id),
);
