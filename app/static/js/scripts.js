$(document).ready(function(){
    $("#profbutton").click(function(){
      $("#updates").slideDown('1500').hide('1000');
      $("#imgform").show('1500');
    });

    $("#submit").click(function(){
      $("#imgform").slideUp('1500');
      $("#updates").slideDown('1500');
    });

    $("#showform").click(function(){
       $("#profileupdate").slideDown('2500');
     });

    $("#submit").click(function(){
       $("#profileupdate").slideUp('1500');
     });

  });

