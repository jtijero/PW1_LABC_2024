#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(:standard);

my $entrada = param('q');
my $resultado;


if ($entrada =~ /^[0-9+\-]+$/) {
    my @tokens = split(' ', $entrada);
    $resultado = 0; 
    my $operador = '+';

    for (my $i = 0; $i < @tokens; $i++) {
        my $token = $tokens[$i];
        if ($token eq '+') {
            $operador = '+';
        } elsif ($token eq '-') {
            $operador = '-'; 
        } else {
            if ($operador eq '+') {
                $resultado += $token;  
            } elsif ($operador eq '-') {
                $resultado -= $token;  
            }
        }
} else {
    $resultado = 'Error';
}

print header('text/html');
print <<HTML;
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Resultado</title>
</head>
<body>
    <div class="calculadora">
        <div class="encabezado">Resultado</div>
        <div class="contenedor-resultado">
            <input type="text" class="resultado" value="$resultado" readonly>
        </div>
        <a href="/html/index.html">Volver</a>
    </div>
</body>
</html>
HTML

