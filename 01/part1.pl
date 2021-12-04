open my $file, '<', 'input.txt';

my @input;

while (<$file>) {
    chomp;
    push @input, int $_;
}
close $file;

my $increases = 0;

for (my $i = 1; $i < scalar @input; $i++) {
    $increases += @input[$i] > @input[$i-1];
}

print $increases;
