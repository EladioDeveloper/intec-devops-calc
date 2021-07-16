Ejercicio 1: Ejecutar un contenedor alpine
docker ps
docker run alpine
docker ps -a    

Ejercicio 2: Eliminar y Renombrar contenedor
docker run --name my-hello-world alpine echo "Hello world"
docker run --name my-hello-world alpine echo "Hello world 2"
docker rm my-hello-world
docker run --name my-hello-world alpine echo "Hello world 2"


Ejercicio 3: Ejecutar terminal al inicar un contenedor
docker run --name my-hello-world alpine echo "Hello World 2"
docker run --rm --name my-hello-world -ti alpine /bin/sh
whoami
pwd
cat /etc/passwd

Ejercicio 4: Iniciar nginx en background
docker run --name nginx -d -p 5962:80 nginx:1.21.0-alpine

Ejercicio 5: Crear archivo dentro del contenedor y validar que se elimina al terminar al container
docker exec -ti nginx /bin/bash
docker exec -ti nginx /bin/bash
mkdir my-carpeta
echo "Hoy es viernes" > demo.txt
exit
docker excec -ti nginx cat /my-carpeta/demo.txt
docker stop nginx
docker rm nginx
docker run --name nginx -d -p 5962:80 nginx:1.21.0-alpine
docker exec -ti nginx cat /my-carperta/demo.txt

Ejercicio 6> Crear imagen docker
###DOCKERFILE###
FROM alpine

ENV HOY=viernes

RUN echo "Comando de imagen"

CMD echo "Comando de Inicializacion $HOY"
###END DOCKERFILE###

docker build -t mi-primera-imagen:v1 .
docker run --rm mi-primera-imagen:v1


Ejercicio 7: Crear imagenes de Apps
###DOCKERFILE###
FROM python:3.8

WORKDIR /app

COPY . .

CMD python hello-world.python

###END DOCKERFILE###

###.dockerignore###
Dockerfile
###end .dockerignore###


###hello-world.py###
print("Hello World)

###End hello-world.py####
docker build -t mi-primera-imagen-python:v1 .
docker run --rm mi-primera-imagen-python:v1
docker run --rm mi-primera-imagen-python:v1 ls