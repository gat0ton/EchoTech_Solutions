CREATE DATABASE IF NOT EXISTS ecotech_solutions
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_general_ci;

USE ecotech_solutions;

CREATE TABLE IF NOT EXISTS usuario (
    numUsuario   INT AUTO_INCREMENT PRIMARY KEY,
    username     VARCHAR(50) NOT NULL UNIQUE,
    -- "sha256$<salt>$<hash>" (104 caracteres): hash SHA-256 con salt; nunca la contraseña en texto.
    passwordHash VARCHAR(255) NOT NULL,
    rol          VARCHAR(20) NOT NULL,
    -- Solo se aceptan los roles que reconoce la clase Usuario.
    CONSTRAINT chk_usuario_rol CHECK (rol IN ('Administrador', 'Empleado'))
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS empleado (
    id         INT PRIMARY KEY,
    nombre     VARCHAR(100) NOT NULL,
    apellido   VARCHAR(100) NOT NULL,
    edad       INT NOT NULL,
    genero     VARCHAR(30) NOT NULL,
    telefono   VARCHAR(30) NOT NULL,
    direccion  VARCHAR(255) NOT NULL,
    correo     VARCHAR(150) NOT NULL,
    horas      INT NOT NULL DEFAULT 0,
    salario    DECIMAL(12, 2) NOT NULL,
    puesto     VARCHAR(100) NOT NULL,
    username   VARCHAR(50) UNIQUE,
    departamento VARCHAR(100)
) ENGINE = InnoDB;

-- Compatibilidad con instalaciones anteriores que no tenían estas columnas.
ALTER TABLE empleado
    ADD COLUMN IF NOT EXISTS username VARCHAR(50) UNIQUE,
    ADD COLUMN IF NOT EXISTS departamento VARCHAR(100);

CREATE TABLE IF NOT EXISTS departamento (
    nombre          VARCHAR(100) PRIMARY KEY,
    descripcion     VARCHAR(255) NOT NULL,
    responsable_id  INT NOT NULL
) ENGINE = InnoDB;