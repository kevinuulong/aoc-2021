open my $file, '<', 'input.txt';

my @input;

while (<$file>) {
    chomp;
    push @input, int $_;
}
close $file;

my $increases = 0;

for (my $i = 0; $i < scalar @input - 2; $i++) {
    $increases += @input[$i] + @input[$i+1] + @input[$i+2] > @input[$i] + @input[$i-1] + @input[$i+1];
}

print $increases;
