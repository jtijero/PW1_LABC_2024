#!/usr/bin/perl
use strict;
use warnings;
use DBI;
use CGI qw(:standard);

# Encabezado HTTP
print header('text/html; charset=UTF-8');

# HTML básico
print <<'END_HTML';
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mostrar Actor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Detalles del Actor</h2>
END_HTML

# Conexión a la Base de Datos (sin usuario ni contraseña)
my $dbh = DBI->connect("DBI:mysql:database=prueba;host=localhost", undef, undef, 
    { RaiseError => 1, PrintError => 0 }) or die "No se pudo conectar: $DBI::errstr";

# Consulta SQL para obtener el actor con id 5
my $sth = $dbh->prepare("SELECT nombre FROM actores WHERE actor_id = ?");
$sth->execute(5);

# Mostrar resultados
if (my @row = $sth->fetchrow_array) {
    my $nombre_actor = $row[0];
    print "<p>El actor con ID 5 es: <strong>$nombre_actor</strong></p>";
} else {
    print "<p>No se encontró un actor con ID 5.</p>";
}

# Cierre de la conexión a la base de datos
$sth->finish();
$dbh->disconnect();

# Cierre del HTML
print <<'END_HTML';
    </div>
</body>
</html>
END_HTML

