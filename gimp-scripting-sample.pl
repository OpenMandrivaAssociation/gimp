#!/usr/bin/perl

# For faster multiple execs, start a gimp, and do Xtns/Perl/Server.

#- (gc) this shit wasted me something like 2 hours: opposedly to what's
#- claimed in the doc, we need to precise `:auto' in the imports, grrrrr..
use Gimp qw(:consts main xlfd_size :auto);

Gimp::init();
#- disable the following when your script is finished
Gimp::set_trace(TRACE_ALL);

my $img = gimp_file_load("/tmp/t.png", "/tmp/t.png");

my $w = gimp_image_width($img);
my $h = gimp_image_height($img);

my $rot = gimp_rotate(gimp_image_active_drawable($img), 1, 0.0872664625997165);

gimp_crop($img, $w, $h, 0, 0);

gimp_file_save($img, $rot, "/tmp/t_.png", "/tmp/t_.png");

Gimp::end();

