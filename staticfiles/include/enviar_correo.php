
<?php

require_once('phpmailer/class.phpmailer.php');

$correo = new PHPMailer();

$correo->IsSMTP();

if( $_POST['template-contactform-name'] != '' AND $_POST['template-contactform-email'] != '' AND $_POST['template-contactform-message'] != '' ) {

        $name = $_POST['template-contactform-name'];
        $email = $_POST['template-contactform-email'];
        $phone = $_POST['template-contactform-phone'];
        $service = $_POST['template-contactform-service'];
        $subject = $_POST['template-contactform-subject'];
        $message = $_POST['template-contactform-message'];
}

// Timeout para el servidor de correos. Por defecto es valor es '10'
$correo->Timeout=30;

// Codificación UTF8. Obligado utilizarlo en aplicaciones en Español
$correo->CharSet = 'UTF-8';
$correo->SMTPAuth = true;
$correo->SMTPSecure = 'SSL';
$correo->Host = "smtp.zoho.com";
$correo->Port = 465;
$correo->Username   = "info@mu.com.py";
$correo->Password   = "infomu2016";
$correo->SetFrom("info@mu.com.py", "Info");

$correo->AddAddress("info@mu.com.py", "Info");

$correo->Subject = "Presentacion MU - Registro";

$correo->MsgHTML("Mi Mensaje en <strong>HTML</strong>");

if(!$correo->Send()) {
  echo "Hubo un error: " . $correo->ErrorInfo;
} else {
  echo "Mensaje enviado con exito.";
}

?>