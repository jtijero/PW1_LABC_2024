#!/usr/bin/perl
use strict;
use warnings;
use CGI;

my $cgi = CGI->new;
print $cgi->header(-type => 'text/html', -charset => 'utf-8');
my $query = $cgi->param('q') || '';

print <<HTML;
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Resultados de búsqueda</title>
</head>
<body>
    <h1>Resultados de búsqueda</h1>
    <form action="/cgi-bin/busquedaU.cgi" method="get">
        <input type="text" name="q" placeholder="Buscar universidades..." value="$query">
        <button type="submit">Buscar</button>
    </form>
HTML

# Mensaje de búsqueda
print "<p>Buscando: $query</p>";

print "</body></html>";

