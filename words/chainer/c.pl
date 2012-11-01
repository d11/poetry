#!/usr/bin/env perl
use Data::Dumper;

my $n = 3;

my %dict = ();
my %starts = ();
my %ends = ();

{

   while (<>) {
      next if $_ =~ /^;;;/;
      chomp(my $in = $_);
      my @ws = split(/ +/, $in);

      my $word = shift @ws;
      next if (scalar @ws < $n);
      my @start = @ws[0 .. $n-1];
      my @end = @ws[-$n..-1];

      my $gram_start = join("-", @start);
      my $gram_end = join("-", @end);

      if (!exists $starts{$gram_start})
      {
         $starts{$gram_start} = [];
      }
      push @{$starts{$gram_start}}, $word;

      if (!exists $ends{$gram_end})
      {
         $ends{$gram_end} = [];
      }
      push @{$ends{$gram_end}}, $word;

      $dict{$word} = [ @ws ];

   }

}

while(1) {

   print "Enter a starting word: ";
   chomp(my $curr_word = uc(<STDIN>));


   my @curr_phon = @{$dict{$curr_word}};
   print join(" ", @curr_phon),"\n";

   my @end = @curr_phon[-$n..-1];

   my $gram_end = join("-", @end);
   print "End: ", $gram_end, "\n";

   my @nexts = @{$starts{$gram_end}};
   print join("\n", @nexts);

}

