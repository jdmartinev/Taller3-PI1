## Instalación de paquetes necesarios

Dado que este workshop es la continuación de los dos anteriores, se asumirá que ya deben tener instalado ``Python``, ``Django`` y ``Pillow``.

Adicional a estas librerías, vamos a instalar lo siguiente:

- ``google-generativeai``: Librería para acceder a modelos de inteligencia artificial
-  ``python-dotenv``: Manejo de api_keys de forma segura
-  ``numpy``: Operaciones matemáticas y de álgebra lineal
-  ``requests``: Consultas a algunas API de openAI

Abra el archivo ``requirements.txt``. Notará que este archivo tiene la siguiente estructura:

 <div align="center">
  <a>
    <img src="imgs/install.png">
  </a>
  </div>

En este archivo se deben listar todas las librerías necesarias para el funcionamiento del proyecto. Si se necesita una versión específica de alguna librería se debe especificar de la siguiente forma:

``numpy==1.20.1``

Por ahora, dado que no requerimos versiones específicas, se puede dejar el archivo como está.

Después, desde la consola ubicada en la carpeta donde se encuentra el archivo ``requirements.txt`` escriba lo siguiente:

``pip install -r requirements.txt``

 <div align="center">
  <a>
    <img src="imgs/install2.png">
  </a>
  </div>

Después de unos segundos la instalación debe quedar completa.

Puedes verificar con el siguiente comando pip si estan instalados todos los paquetes necesarios

``pip list``

![image](https://github.com/user-attachments/assets/36b8e843-ba84-45ee-a8d8-204760114c02)


**RECUERDA:** Si estás usando un entorno virtual (virtualenv), asegúrate de activarlo antes de ejecutar el comando para ver los paquetes instalados en ese entorno.


Como mas adelante utilizaremos HuggingFace, crea una cuenta en dicha pagina para posteriormente
generar el token (https://huggingface.co/welcome):
![image](https://github.com/user-attachments/assets/39e90049-eed2-4499-9924-4d9082c7a623)



Una vez creada, instala el paquete y accede al apartado de tokens.
``pip install huggingface_hub`` 

![image](https://github.com/user-attachments/assets/e1a233bb-88d1-40fc-a08e-ce3d9023d4ad)


Vamos a settings/Access tokens
![image](https://github.com/user-attachments/assets/c4725a9b-002d-45f2-b331-0bed7c771bad)


y generaremos nuestro nuevo token:
![image](https://github.com/user-attachments/assets/071ab31d-4c0b-4074-8e99-b20065ed92b0)


Le ponemos un nombre y le otorgamos los permisos necesarios: 

![image](https://github.com/user-attachments/assets/c619f6c5-f21e-4c63-8e82-bc12a114c491)


![image](https://github.com/user-attachments/assets/5c6dec90-7189-472a-b470-d681523a9c64)

Bajamos, creamos y copiamos el codigo del token **(guardalo en el archivo .env de tu proyecto!)**
![image](https://github.com/user-attachments/assets/c78f07ae-9a10-45f9-a28e-3f08882ba743)

![image](https://github.com/user-attachments/assets/5a60cf9a-c794-434f-9bcd-aa0dcb1dfa57)


