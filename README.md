# Taller PHP

Este proyecto corresponde a un taller de **PHP**, en el cual se desarrollan formularios para registrar y acceder a usuarios, además de mostrar mensajes de bienvenida y validar datos. Desarrollado en Replit. 

## Archivos del proyecto

- **index.php**  
  Archivo principal que carga el formulario de registro (`formulario.php`).

- **formulario.php**  
  Contiene un formulario HTML para el registro de usuarios con los siguientes campos:  
  - Cédula (10 dígitos)  
  - Nombre (30 caracteres máximo)  
  - Género (opciones: No responder, Masculino, Femenino, Otro)  
  - Correo electrónico  
  - Clave (mínimo 6 caracteres, permite letras, dígitos o guiones bajos)  
  Incluye los botones **Registrar** y **Resetear**.

- **bienvenido.php**  
  Procesa los datos enviados desde el formulario de registro o desde el formulario de acceso:  
  - Si recibe 2 campos (cedula y clave), usa la función `acceder()` para validar las credenciales y, si son correctas, muestra un mensaje de bienvenida con un emoji aleatorio, un enlace a un video de YouTube y el mensaje **Ingreso correcto**. En caso contrario, redirige a `acceso.php`.  
  - Si recibe 5 campos (registro), verifica con la función `validar()` si la cédula ya existe; si no existe, muestra un mensaje de bienvenida con un emoji aleatorio.  
  - Las contraseñas son cifradas con `md5` y se preparan en el array `$datos`, aunque no se almacenan en el CSV en este archivo.

- **usuario.php**  
  Contiene funciones para manejar los usuarios:  
  - `registrarDatos($datos)`: Genera una línea con los datos y la guarda en `usuarios.csv`.  
  - `validar($cedula)`: Comprueba si la cédula existe en `usuarios.csv`.  
  - `acceder($cedula, $clave)`: Valida las credenciales comparando la cédula y la contraseña cifrada en `usuarios.csv`.

- **acceso.php**  
  Formulario para el inicio de sesión solicitando cédula y clave.

- **tabla.php**  
  Plantilla HTML que muestra los datos del usuario en una tabla.

- **usuarios.csv**  
  Archivo de texto donde se almacenan los usuarios registrados (cédula, nombre, género, correo, clave cifrada).

## Funcionalidades implementadas

- Formulario de registro de usuarios con validación de campos en `formulario.php`.  
- En `bienvenido.php` se muestra un mensaje de bienvenida con un emoji aleatorio.  
- Validación de credenciales con `acceder()` para el inicio de sesión.  
- Redirección al formulario de acceso si las credenciales son incorrectas o si la cédula ya existe.  
- Las contraseñas se manejan usando `md5`.

## Requisitos

- Entorno con soporte PHP (Replit o servidor local con PHP).  
- Navegador web 
