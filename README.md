# Docker Pub/Sub 

Crear una aplicación tipo publicación/subscripción usando Docker, Python, MQTT y Redis.

Lo primero que haremos es crear los contenedores para MQTT y Redis.

  **Para MQTT (Eclipse Mosquitto)**

    docker run -dit --name mosquitto -p 1883:1883 eclipse-mosquitto
  
  **Para Redis**

    docker run -dit --name redis -p 6379:6379 redis

Ahora vamos a clonar el repositorio que contiene el código para el publicador y el subscriptor.

    git clone https://github.com/WilliamMolina/docker-demo.git

Abrimos el código con nuestro editor de código favorito.

Procedemos a construir las imagenes del publicador y el subscriptor.

**Publicador**

    cd publisher
    docker build -t publicador .
 **Subscriptor**
 

    cd subscriber
    docker build -t subscriptor .
Por último iniciamos un contenedor para cada uno de los componentes
**Publicador**

    docker run -dit --name publicador -p 5000:5000 --link mosquitto:mosquitto publicador
  **Subscriptor**
  

    docker run -dit --name subscriptor --link redis:redis --link mosquitto:mosquitto subscriptor

Finalmente probamos el publicador y validamos que los datos hayan sido guardados en Redis.

**Prueba**

    curl --location --request POST 'http://localhost:5000/events/log' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "id":"123",
        "data":"prueba"
    }'

**Validación en Redis**

    docker exec -it redis redis-cli
    get "event:123"
