#! /usr/bin/perl
print "Content-type: text/html \n\n";

print <<EOF;

<style>
h1 {
margin: 0px;
padding : 0px;
width: 300px;
display:block;
font-size: 20px;
font-family: "Tahoma";
}
h2,h3 {
margin: 10px 0px 0px 25px;
padding : 0px;
<!--border: 1px solid #000000;-->
width: 300px;
<!--background-color: #c3d8a9;-->
display:block;
font-size: 15px;
font-family: "Tahoma";
}
h3 {
margin-left : 50px;
}
body {
  background-color: beige;
}
img {

  width : 25px;
  height : 25px;
}
#indent {
  margin-left: 10px;
  float: left;
}
#indent2 {
  margin-left: 32px;
  float: left;
}
#indent3 {
  margin-left: 54px;
  float: left;
}
#plus {
  float: right;
  padding-right : 4px;
}
#plus a:link, #plus a:active, #plus a:visited {
  color: #b4d28e;
  text-decoration : none;
}
#plus a:hover {
  color: #c30000;
}
</style>
EOF

use strict;
use feature "switch";
my $Context_Tree;
my ($level_one,$level_down);
my ($Context_Node_HashRef,$Content_Node_ArrayRef);
my (@level_one,$l1_ref);
@level_one = ("Retail Tech","Fin Tech", "Civic Tech");
$l1_ref = \@level_one;


my $context_href = CreateContextNode(0,"Startup Context","Initial Context");
printContextNode($context_href);
printBranch($context_href);
my $context_href2 = CreateContextNode(1,${$l1_ref}[0]);
printContextNode($context_href2);
#pass margin-left as 32px for 2nd level indent
printBranch($context_href2);
$context_href2 = CreateContextNode(2,"E-Commerce");
printContextNode($context_href2);
printBranch();
$context_href2 = CreateContextNode(1,${$l1_ref}[1]);
printContextNode($context_href2);
my $content_href = CreateContentNode(3,"Meeting with E-Commerce Consultant");
printContentNode($content_href);

print $ENV{'HTTP_USER_AGENT'};
print %ENV;
sub printBranch(){
  my $i = 0;
#  do {print"<br>|";emulateTab(); $i++;} while $i <= 5; 
  my $href = shift;
  my $indent_class;
  for(${$href}{'node_level'}){
    #print $_;
    when(/1/) {$indent_class = "indent2";}
    when(/2/) {$indent_class = "indent";}
    default {$indent_class = "indent"};
  }
  print "<img id=\"$indent_class\" src=\"076-enter.png\"/>";
}

sub emulateTab(){
  my $i = 0;
  do {
    print "&nbsp;-"; 
    $i++;
  } 
  while $i <= 5;
}
sub printContentNode {
  my $href = shift;
  my ($begin_tag,$end_tag);
  for (${$href}{'node_level'}){
    #when (/0/) {$begin_tag = "<p>"; $end_tag="</p>"; }
    default {$begin_tag="<h6>"; $end_tag="</h6>";}
  }
  print $begin_tag;
  print "<img src=\"clipboard-3.png\"/>";
  print ${$href}{'node_name'};
  print $end_tag;
  print "\n";
}

sub printContextNode {
  my $href = shift;
  my ($begin_tag,$end_tag);
  for (${$href}{'node_level'}){
    when (/0/) {$begin_tag = "<h1>"; $end_tag="</h1>"; }
    when (/1/) {$begin_tag = "<h2>"; $end_tag="</h2>"; }
    when (/2/) {$begin_tag = "<h3>"; $end_tag="</h3>"; }
    default {$begin_tag="<h6>"; $end_tag="</h6>";}
  }
  print $begin_tag;
  print "<img src=\"clipboard-4.png\"/>";
  print ${$href}{'node_name'};
  print "<span id=\"plus\"><a href=\"context.html\">+</a></span>";
  print $end_tag;
  print "\n";
}

sub CreateContentNode {


  my $node_level = shift;
  my $node_name = shift;
  my $node_desc = shift;
  my %content_struct = (
      node_level => $node_level,
      node_name => $node_name,
      node_desc => $node_desc,
      );

#  print $context_struct{node_name};
#  print "\n";
#return reference to Context node
  return \%content_struct;  

}
sub CreateContextNode {


  my $node_level = shift;
  my $node_name = shift;
  my $node_desc = shift;
  my %context_struct = (
      node_level => $node_level,
      node_name => $node_name,
      node_desc => $node_desc,
      );

#  print $context_struct{node_name};
#  print "\n";
#return reference to Context node
  return \%context_struct;  

}
