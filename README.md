# Laboratorio-01-2025-I
#### Integrantes:
Juliana Gongora Rassmusen

correo:

Gerhaldine Alejandra Suárez Bernal

correo: gesuarezb@unal.edu.co

## Robótica de Desarrollo, Intro a ROS 2 Humble - Turtlesim
En el presente informe se describen los resultados obtenidos al utilizar ROS 2 Humble para controlar el simulador Turtlesim mediante programación en Python. Se desarrolló un script que permite desplazar la tortuga de Turtlesim mediante comandos de teclado predefinidos, gestionando tanto movimientos lineales como angulares. Asimismo, se implementó la funcionalidad de dibujar letras específicas a partir de la pulsación de teclas correspondientes.

### Objetivos
- Crear un nodo en Python capaz de controlar la posición de la tortuga mediante feedback, estableciendo la conexión entre ROS 2 y Python.

- Desarrollar un sistema para mover la tortuga utilizando comandos controlados por las teclas de flechas del teclado.

- Implementar un sistema en el cual, al presionar una tecla, la tortuga trace un camino que forme la figura de la letra correspondiente.
### Procedimiento realizado



```mermaid
---
config:
  theme: redux
---
flowchart TD
    A(["Inicio <br>"]) --> B["Leer tecla<br>"]
    B --> D["tecla == flechas?<br>"]
    D --> n1["No <br>"] & n2["Si"]
    n1 --> n3["tecla == J? <br>"]
    n2 --> n4["Movimiento libre<br>"]
    n3 --> n5["No <br>"] & n6["Si <br>"]
    n6 --> n7["Dibujar J <br>"]
    n5 --> n8["tecla == G?<br>"]
    n8 --> n9["Si"] & n10["No"]
    n9 --> n11["Dibujar G<br>"]
    n10 --> n12["tecla R?<br>"]
    n12 --> n13["si"] & n14["No <br>"]
    n14 --> n15["tecla A? <br>"]
    n13 --> n16["Dibujar R <br>"]
    n15 --> n17["No <br>"] & n18["Si <br>"]
    n17 --> n19["tecla S? <br>"]
    n18 --> n20["Dibujar A <br>"]
    n19 --> n21["No <br>"] & n22["Si <br>"]
    n22 --> n23["Dibujar S <br>"]
    n21 --> n24["tecla b?<br>"]
    n24 --> n25["No <br>"] & n26["Si"]
    n26 --> n27["Dibujar B <br>"]
    n27 --> B
    n4 --> B
    B@{ shape: rect}
    D@{ shape: diam}
    n1@{ shape: text}
    n2@{ shape: text}
    n3@{ shape: diam}
    n4@{ shape: subproc}
    n5@{ shape: text}
    n6@{ shape: text}
    n8@{ shape: diam}
    n10@{ shape: rect}
    n12@{ shape: diam}
    n13@{ shape: text}
    n14@{ shape: text}
    n15@{ shape: diam}
    n17@{ shape: text}
    n18@{ shape: text}
    n19@{ shape: diam}
    n21@{ shape: text}
    n22@{ shape: text}
    n24@{ shape: diam}
    n25@{ shape: text}
    n26@{ shape: text}


```
```mermaid
---
config:
  theme: redux
---
flowchart TD
    A(["Inicio"]) --> B{"tecla==arriba? <br>"}
    B --> C["No"] & D["Si <br>"]
    D --> n1["Avanzar hacia adelante <br>"]
    C --> n2["tecla==abajo? <br>"]
    n2 --> n3["Si <br>"] & n4["No"]
    n3 --> n5["retroceder <br>"]
    n4 --> n6["tecla==derecha? <br>"]
    n6 --> n7["Si <br>"] & n8["No <br>"]
    n8 --> n9["tecla==izquierda?"]
    n7 --> n10["Girar a la derecha <br>"]
    n9 --> n11["Si <br>"] & n12["No"]
    n11 --> n14["Girar a la izquierda <br>"]
    n12 --> n15["Fin <br>"]
    C@{ shape: text}
    D@{ shape: text}
    n2@{ shape: diam}
    n3@{ shape: text}
    n4@{ shape: text}
    n6@{ shape: diam}
    n7@{ shape: text}
    n8@{ shape: text}
    n9@{ shape: diam}
    n11@{ shape: text}
    n12@{ shape: text}
    n15@{ shape: rounded}
