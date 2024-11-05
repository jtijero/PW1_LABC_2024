#!/usr/bin/perl
use strict;
use warnings;
use CGI;

my $cgi = CGI->new;
my $query = $cgi->param('q');

$query = $cgi->escapeHTML($query);

print $cgi->redirect(-uri => "https://www.google.com/images?q=$query");

