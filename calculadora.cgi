#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(:standard);

my $entrada = param('q');
my $resultado;

if ($entrada =~ /^[0-9\s\+\-\*\/\%\(\)]+$/) {
    my @tokens = split(' ', $entrada);
    $resultado = resolviendo(\@tokens);
} else {
    $resultado = 'Error'; 
}

sub resolviendo {
    my ($tokens) = @_;
    my $resultado = 0;
    my $operador = '+';

    for (my $i = 0; $i < @$tokens; $i++) {
        my $token = $tokens->[$i];

        if ($token eq '(') {
            my $dentrodelParentesis = '';
            my $j = $i + 1;
            my $conteodeParentesis = 1;

            while ($j < @$tokens && $conteodeParentesis > 0) {
                if ($tokens->[$j] eq '(') {
                    $conteodeParentesis++;
                } elsif ($tokens->[$j] eq ')') {
                    $conteodeParentesis--;
                }
                $dentrodelParentesis .= $tokens->[$j] . ' ';
                $j++;
            }

            $dentrodelParentesis =~ s/\s+$//;  #se utiliza para buscar un patrón y reemplazarlo por otra cosa.
            my $sub_resultado = resolviendo([split(' ', $dentrodelParentesis)]);
            $token = $sub_resultado;
            $i = $j - 1;  
        }

        if ($token eq '+') {
            $operador = '+';
        } elsif ($token eq '-') {
            $operador = '-'; 
        } elsif ($token eq '*') {
            $operador = '*'; 
        } elsif ($token eq '/') {
            $operador = '/'; 
        } elsif ($token eq '%') {
            $operador = '%'; 
        } else {
            if ($operador eq '+') {
                $resultado += $token;  
            } elsif ($operador eq '-') {
                $resultado -= $token;  
            } elsif ($operador eq '*') {
                $resultado = ($resultado == 0) ? $token : $resultado * $token;  
            } elsif ($operador eq '/') {
                if ($token != 0) {
                    $resultado = ($resultado == 0) ? $token : $resultado / $token;  
                } else {
                    return 'Error: División por cero';
                }
            } elsif ($operador eq '%') {
                $resultado = ($resultado == 0) ? $token : $resultado % $token;  
            }
        }
    }

    return $resultado;
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

