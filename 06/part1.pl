use warnings; use strict;

open my $file, '<', 'input.txt';

my @input = split /,/, <$file>;

close $file;

sub grow_fish {
    my ($days) = @_;
    for (my $i = 0; $i < $days; $i++) {
        my $size = scalar @input;
        for (my $j = 0; $j < $size; $j++) {
            if ($input[$j] == 0) {
                push @input, 8;
                $input[$j] = 6;
            } else {
                $input[$j]--;
            }
        }
    }
    return scalar @input;
}



print grow_fish(80)."\n";
