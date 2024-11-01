#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(:standard);
my ceviche = param('q');
my resultado;
print <<HTML;
 <div class="calculadora">
        <div class="encabezado">Resultado</div>
        <div class="contenedor-resultado">
            <input type="text" class="resultado" value="$resultado" readonly>
        </div>
        <a href="index.html">Volver</a>
    </div>
HTML
