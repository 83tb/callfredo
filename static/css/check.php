<?php

// Get Values from Contact form
$EmailFrom = "info@kobusswartz.co.za";
$EmailTo = "info@kobusswartz.co.za";
$Subject = "Sticky";
$name = Trim(stripslashes($_POST['name'])); 
$cemail = Trim(stripslashes($_POST['cemail'])); 
$curl = Trim(stripslashes($_POST['url'])); 
$ccomment = Trim(stripslashes($_POST['ccomment'])); 

// Assign retrived values to variables for email
$Body = "";
$Body .= "name: ";
$Body .= $name;
$Body .= "\n";
$Body .= "email: ";
$Body .= $cemail;
$Body .= "\n";
$Body .= "url: ";
$Body .= $curl;
$Body .= "\n";
$Body .= "comment: ";
$Body .= $ccomment;
$Body .= "\n";

// Send mail 
$success = mail($EmailTo, $Subject, $Body, "From: <$EmailFrom>");

// When email goes through, redirect to index.html
if ($success){
  print "<meta http-equiv=\"refresh\" content=\"0;URL=index.html\">";
}
else{
  print "<meta http-equiv=\"refresh\" content=\"0;URL=index.html\">";
}
?>