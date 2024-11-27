#!/usr/bin/perl
use strict;
use warnings;
use DBI;
use CGI qw(:standard);

# Encabezado HTTP
print header('text/html; charset=UTF-8');

# HTML para el formulario con estilo CSS
print <<'END_HTML';
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Buscar Películas por Año</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bungee+Spice&family=Hubot+Sans:ital,wght@1,300&family=Monoton&family=Montserrat+Alternates:ital,wght@0,200;1,200&family=Playwrite+GB+S:ital,wght@0,100..400;1,100..400&family=Sedgwick+Ave+Display&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: "Montserrat Alternates", sans-serif;
            font-weight: 200;
            font-style: italic;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background: white;
            padding: 20px; /* Espacio interno */
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 600px; /* Ancho máximo */
            width: 100%; /* Ancho completo */
        }

        h2 {
            color: #333; /* Color del encabezado */
            margin-bottom: 20px; /* Espacio inferior */
        }

        form {
            margin: 20px 0; /* Espacio alrededor del formulario */
            display: flex; /* Para alinear en una fila */
            justify-content: center; /* Centrar los elementos del formulario */
            align-items: center; /* Alinear verticalmente */
        }

        input[type="text"] {
            padding: 10px; /* Espacio interno */
            border: 1px solid #007bff; /* Borde azul */
            border-radius: 4px; /* Bordes redondeados */
            width: 60%; /* Ancho del campo de texto */
            box-sizing: border-box; /* Incluye padding y borde en el ancho */
            margin-right: 10px; /* Espacio a la derecha */
        }

        input[type="submit"] {
            background-color: #007bff; /* Fondo azul */
            color: white; /* Texto blanco */
            padding: 10px 15px; /* Espacio interno */
            border: none; /* Sin borde */
            border-radius: 4px; /* Bordes redondeados */
            cursor: pointer; /* Cambia el cursor al pasar el mouse */
            font-size: 1em; /* Tamaño de fuente */
        }

        input[type="submit"]:hover {
            background-color: #0056b3; /* Color al pasar el mouse */
        }

        p {
            color: black; /* Color del texto de los resultados */
            margin: 5px 0; /* Espacio entre párrafos */
            font-family: "Hubot Sans", sans-serif; /* Fuente para los resultados */
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Buscar Películas por Año</h2>
        <form action="/cgi-bin/busquedaporaño.cgi" method="post">
            <input type="text" name="year" required>
            <input type="submit" value="Buscar">
        </form>
        <br></br>
END_HTML

# Conexión a la Base de Datos (sin usuario ni contraseña)
my $dbh = DBI->connect("DBI:mysql:database=prueba;host=localhost", undef, undef, 
    { RaiseError => 1, PrintError => 0 }) or die "No se pudo conectar: $DBI::errstr";

# Obtener el año desde la consulta
my $year = param('year');

# Si se ha ingresado un año, realizar la búsqueda
if ($year) {
    # Consulta SQL para obtener películas del año especificado
    my $sth = $dbh->prepare("SELECT p.nombre AS pelicula, a.nombre AS actor, c.papel 
                              FROM peliculas p 
                              JOIN casting c ON p.pelicula_id = c.pelicula_id 
                              JOIN actores a ON c.actor_id = a.actor_id 
                              WHERE p.year = ?");
    $sth->execute($year);

    # Mostrar resultados
    print "<h1>Resultados para el año $year</h1>";
    if (my @row = $sth->fetchrow_array) {
        do {
            print "<p>Pelicula: $row[0], Actor: $row[1], Papel: $row[2]</p>";
        } while (@row = $sth->fetchrow_array);
    } else {
        print "<p>No se encontraron resultados para el año $year.</p>";
    }

    # Cerrar la conexión
    $sth->finish();
}

# Cerrar la conexión a la base de datos
$dbh->disconnect();

print "</div></body></html>";
