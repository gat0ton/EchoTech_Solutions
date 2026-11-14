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