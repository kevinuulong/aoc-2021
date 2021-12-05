use warnings; use strict;
use List::Util 'min', 'max';

open my $file, '<', 'input.txt';

my @input;

while (<$file>) {
    chomp;
    push @input, $_;
}
close $file;

my $grid = {};
my $overlaps = 0;

for (@input) {
    my @digits = $_ =~ /(\d+)/g;
    if ($digits[0] == $digits[2]) {
        for my $y (min($digits[1], $digits[3])..max($digits[1], $digits[3])) {
            point($digits[0], $y);
        }
    } elsif ($digits[1] == $digits[3]) {
        for my $x (min($digits[0], $digits[2])..max($digits[0], $digits[2])) {
            point($x, $digits[1]);
        }
    } else {
        my @x_range = (min($digits[0], $digits[2])..max($digits[0], $digits[2]));
        @x_range = reverse @x_range if ($digits[0] < $digits[2]);
        my @y_range = (min($digits[1], $digits[3])..max($digits[1], $digits[3]));
        @y_range = reverse @y_range if ($digits[1] < $digits[3]);
        for (my $i = 0; $i < scalar @x_range; $i++) {
            point($x_range[$i], $y_range[$i]);
        }
    }
}

sub point {
    my ($x, $y) = @_;

    $grid->{$x}->{$y}++;
    $overlaps++ if ($grid->{$x}->{$y} == 2);
}

print "$overlaps\n";