#!/usr/bin/env perl
use Data::Dumper;

my %dict = ();

while (<>) {
   next if $_ =~ /^;;;/;
   chomp(my $in = $_);
   my @ws = split(/ +/, $in);

   my $word = shift @ws;
   next if (scalar @ws < $n);

   $dict{$word} = [ @ws ];
}

while (1) {

print "Enter text\n";
chomp(my $input = <STDIN>);

for my $word (split / /,$input) {
   my $ra_p = $dict{uc($word)};
   if ($ra_p) {
      my @phones = @{$dict{uc($word)}};
      #print Dumper(\@phones);

      my $prev = shift @phones;
      while (my $phon = shift @phones) {
         #print $prev," ", $phon, "\n";
         if ((grep $prev, qw(B BB)) and (grep $phon, qw(IY0 IY1 Y))) {
            $word =~ s/b[aeoiy]*/BEE/i;
            #   print $word, "\n";
         }
         $prev = $phon;
      }
   }
         
   print $word, " ";
}

}
