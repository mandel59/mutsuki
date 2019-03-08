#!/usr/bin/perl
while (<>) {
    if (/^StartChar: (uni(3[4-9A-D]|4[EF]|[5-9][0-9A-F])[0-9A-F]{2}|u2[0-9A-F]{4})$/ .. /^EndChar$/) {
        # print STDERR "omit $1\n";
    } else {
        s/Mutsuki/Mutsuki Kana/g;
        s/\+MIAwZDBN/\+MIAwZDBNMEswag/g; # s/むつき/むつきかな/g
        print $_;
    }
}
