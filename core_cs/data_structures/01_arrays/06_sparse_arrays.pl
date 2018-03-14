# Enter your code here. Read input from STDIN. Print output to STDOUT
use warnings;
use strict;

chomp(my $number_of_strings = <STDIN>);
my %count;

while($number_of_strings) {
	chomp(my $x = <STDIN>);
	$count{$x}++;
	$number_of_strings--;
}
chomp(my $number_of_query_strings = <STDIN>);

foreach(1..$number_of_query_strings) {
	chomp(my $x = <STDIN>);
	$count{$x}?print "$count{$x}\n":print"0\n";
}
