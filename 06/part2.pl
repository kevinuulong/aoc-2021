use warnings; use strict;
use List::Util 'sum';

open my $file, '<', 'input.txt';

my @input = split /,/, <$file>;

close $file;

my %fish;

foreach (@input) {
    $fish{$_}++;
}


sub grow_fish {
    my ($days) = @_;
    for (my $i = 0; $i < $days; $i++) {
        my %fish_copy;
        foreach (keys %fish) {
            if ($_ != 0) {
                $fish_copy{$_-1} += $fish{$_};
            } else {
                $fish_copy{8} += $fish{$_};
                $fish_copy{6} += $fish{$_};
            }
        }
        %fish = %fish_copy;
    }
    return sum(values %fish);
}



print grow_fish(256)."\n";
