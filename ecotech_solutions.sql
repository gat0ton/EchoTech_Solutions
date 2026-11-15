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

CREATE TABLE IF NOT EXISTS registro (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    horas           INT NOT NULL,
    fecha           DATE NOT NULL,
    id_asociado     INT NOT NULL
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS proyecto (
    id                  INT AUTO_INCREMENT PRIMARY KEY,
    nombre              VARCHAR(150) NOT NULL,
    departamento_nombre VARCHAR(100) NOT NULL,
    registro_id         INT NOT NULL,
    pais                VARCHAR(100) NOT NULL,
    presupuesto_clp     DECIMAL(15, 2) NOT NULL,
    moneda              CHAR(3) NOT NULL,
    presupuesto_local   DECIMAL(15, 2) NOT NULL,
    tasa_conversion     DECIMAL(20, 10) NOT NULL,
    CONSTRAINT fk_proyecto_departamento
        FOREIGN KEY (departamento_nombre) REFERENCES departamento(nombre),
    CONSTRAINT fk_proyecto_registro
        FOREIGN KEY (registro_id) REFERENCES registro(id)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS proyecto_registro (
    proyecto_id INT NOT NULL,
    registro_id INT NOT NULL,
    PRIMARY KEY (proyecto_id, registro_id),
    FOREIGN KEY (proyecto_id) REFERENCES proyecto(id),
    FOREIGN KEY (registro_id) REFERENCES registro(id)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS proyecto_empleado (
    proyecto_id INT NOT NULL,
    empleado_id INT NOT NULL,
    PRIMARY KEY (proyecto_id, empleado_id),
    FOREIGN KEY (proyecto_id) REFERENCES proyecto(id),
    FOREIGN KEY (empleado_id) REFERENCES empleado(id)
) ENGINE = InnoDB;