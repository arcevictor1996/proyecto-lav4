CREATE DATABASE IF NOT EXISTS DB_ACADEMIA;
USE DB_ACADEMIA;

CREATE TABLE IF NOT EXISTS Instructores (
    idInstructores INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Telefono VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS Alumnos (
    Legajo INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Telefono VARCHAR(20),
    Direccion VARCHAR(100),
    DNI VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Cursos (
    Codigo INT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Cuota DECIMAL(10, 2) NOT NULL,
    Duracion INT NOT NULL,
    IDInstructor INT,
    FOREIGN KEY (IDInstructor) REFERENCES Instructores(idInstructores) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Matriculas (
    IDMatricula INT AUTO_INCREMENT PRIMARY KEY,
    LegajoAlumno INT NOT NULL,
    CodigoCurso INT NOT NULL,
    FechaInscripcion DATE,
    FOREIGN KEY (LegajoAlumno) REFERENCES Alumnos(Legajo) ON DELETE CASCADE,
    FOREIGN KEY (CodigoCurso) REFERENCES Cursos(Codigo) ON DELETE CASCADE,
    UNIQUE (LegajoAlumno, CodigoCurso)
);

-- Crear un Trigger para asignar la fecha automáticamente
DELIMITER $$
CREATE TRIGGER SetFechaInscripcion BEFORE INSERT ON Matriculas
FOR EACH ROW
BEGIN
    IF NEW.FechaInscripcion IS NULL THEN
        SET NEW.FechaInscripcion = CURDATE();
    END IF;
END$$
DELIMITER ;
