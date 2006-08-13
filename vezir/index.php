<?php

    #Get Config and Set Lang vars
    require_once ('etc/config.php');
    require_once ('lang/'.$LF); 

    #Get Sysvars,Connection and String Functions
    require_once ('etc/sysvars.php');
    require_once ('lib/vezir.php');
    require_once ('lib/parser.php');

    #create an instance for connection to database
    $Vezir = new Vezir($CF);

    #if any Vezir errors show them.
    if ($Vezir)
        $Vezir->ShowLogs();

    #Set Entries
    $Entries = $Vezir->GetRecord("Entries");

    #Get template file
    include_once('template/'.$CF['Theme'].'/index.tmpl');
?>
