#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use utf8;
use Encode qw(decode encode);

my $cgi = CGI->new;
print $cgi->header(-type => 'text/html', -charset => 'utf-8');
my $query = decode('UTF-8', $cgi->param('q') || '');

print <<HTML;
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Resultados de búsqueda</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; }
    </style>
</head>
<body>
    <h1>Resultados de búsqueda</h1>
    <form action="/cgi-bin/busquedaU.cgi" method="get">
        <input type="text" name="q" placeholder="Buscar universidades..." value="$query">
        <button type="submit">Buscar</button>
    </form>
HTML

# Abrir y leer el archivo CSV
open(my $fh, '<:encoding(UTF-8)', '/usr/lib/cgi-bin/universidades.csv') or die "No se pudo abrir el archivo: $!";
my $encabezado = <$fh>;

my $resultados = 0;
my @resultados_html;

# Mensaje de búsqueda
print "<p>Buscando: $query</p>";

if ($resultados == 0) {
    print "<p>No se encontraron resultados para \"$query\".</p>";
} else {
    print "<p>Se encontraron $resultados resultados para \"$query\".</p>";
    print join("", @resultados_html);
}

print "</div></body></html>";
