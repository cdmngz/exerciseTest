<?php
    
    $foo = "¿Son mulas o cívicos alumnos?";

    $foo = iconv('UTF-8','ASCII//TRANSLIT', $foo);  //Quitamos las tildes
    $foo = preg_replace('/[^\w]/', '', $foo);       //Quitamos todo lo que no sea letra o número
    $foo = strtolower($foo);                        //Pasamos todo a minúscula
    
    $mitadTamanio = (strlen($foo)/2)+1;
    
    $primerSegmento = substr($foo, 0, $mitadTamanio);
    $segundoSegmento = substr($foo, -$mitadTamanio);
        
    echo "Evaluaremos a $foo\nLa mitad es $mitadTamanio\n\nLa primera parte es: $primerSegmento\nLa segunda parte es: $segundoSegmento\n";
        
    $primerSegmentoRev = strrev($primerSegmento);
        
    echo "La palabra volte es: $primerSegmentoRev";
    
    if($primerSegmentoRev == $segundoSegmento) {
        echo "\n\nEs palíndromo!!!";
    } else {
        echo "\n\nNo es una palabra palíndromo.";
    }
?>