<!DOCTYPE html>
<html lang="en">
<head>
                <meta charset="UTF-8">
                <title>ASK</title>
                <link rel="stylesheet" href="css/materialize.min.css">
                <style>body { background-color:Teal; } </style>
</HEAD>
<BODY>
<?php

     	// llamada para insertar header
                error_reporting(E_ALL);
                require_once("header.php");

	// llamada constantes
		require_once("constantes.php");
?>
<!--Contenedor-->

<div class="container ">
<div class="card-panel Gainsboro">
 <div class="col s4 "><h5>
 Sistema Pregunta Respuesta sobre Salmonella
  </h5><br>
<?php
	// creamos variables útiles para la consulta
		$ask = $_GET["ask"];

	// Quitamos los espacios iniciales y finales en la solicitud
		$ask = trim($ask);	

	// evitamos que nos hackeen, porque no deja "agregar" texto de html al docuento original
		$ask = filter_var($ask, FILTER_SANITIZE_STRING);
               
	//evita heckeo con codigo shell
           
                $ask = escapeshellcmd($ask);

   // Conectamos con MySQL
                $conn = mysqli_connect(SERVERNAME, USERNAME, PASSWORD, DBNAME);
        // Evaluamos la conexión
$check=0;
                if(!$conn){
                        die("Connection Failed". mysqli_connect_error());
                }else  { // sí si se conectó                       
			$sql ="select * from Info WHERE info like '${ask}%';";
			$result = mysqli_query($conn, $sql);
                        if (mysqli_num_rows($result)>0){
			   $r=1;    
$filename="/home/mrivero/public_html/bionlp/" . $ask . ".txt";
             		$file =fopen ($filename, "w");
        while ($row = mysqli_fetch_assoc($result)){ 
				$line = $r ."\t".$row["info"]."\n"."\n" ;
				fwrite($file,$line);
                               echo $r ;   echo ".-";
				echo $row["info"];       echo  '<br><br>';
			$r++;
	}         //deberia cerrar primer while      
fclose($file); ?> <a href="<?php echo $ask; ?>.txt">Download file</a> <?php
                        }//debe cerrar  el segundo if     if (mysqli_num_rows($result)>0)     linea 88
                        else {
                              	echo "Lo sentimos, aún no contamos con resultados para tu búsqueda";
                        }
                }//deberia cerrar el primer else de la conexion exitosa
                mysqli_close($conn);
?> 
   </BODY>
</HTML>
