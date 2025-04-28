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


Se presenta el diagrama de flujo implementado:

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
    n10 --> n12["tecla==R?<br>"]
    n12 --> n13["si"] & n14["No <br>"]
    n14 --> n15["tecla==A? <br>"]
    n13 --> n16["Dibujar R <br>"]
    n15 --> n17["No <br>"] & n18["Si <br>"]
    n17 --> n19["tecla==S? <br>"]
    n18 --> n20["Dibujar A <br>"]
    n19 --> n21["No <br>"] & n22["Si <br>"]
    n22 --> n23["Dibujar S <br>"]
    n21 --> n24["tecla==b?<br>"]
    n24 --> n25["No <br>"] & n26["Si"]
    n26 --> n27["Dibujar B <br>"]
    n4 --> B
    n25 --> n28["tecla ==q?<br>"]
    n28 --> n29["No <br>"] & n30["Si <br>"]
    n29 --> B
    n30 --> n31["Salir"]
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
    n28@{ shape: diam}
    n29@{ shape: text}
    n30@{ shape: text}
    n31@{ shape: rounded}



```


### Movimiento libre 

Mediante una serie de condiciones basadas en la presión de las teclas correspondientes a las flechas del teclado, se busca obtener un control manual sobre la trayectoria seguida por la tortuga. Esta funcionalidad permite mover la tortuga en diferentes direcciones (arriba, abajo, izquierda, derecha) según las teclas presionadas, logrando un movimiento libre e interactivo.
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



```
```python

        while True:
            key = stdscr.getch()

            if key == ord('q'):
                self.get_logger().info('Saliendo del control manual')
                break

            # Flechas para movimiento manual
            if key == curses.KEY_UP:
                msg.linear.x = float(self.speed)
                msg.angular.z = 0.0
                last_key = curses.KEY_UP
            elif key == curses.KEY_DOWN:
                msg.linear.x = float(-self.speed)
                msg.angular.z = 0.0
                last_key = curses.KEY_DOWN
            elif key == curses.KEY_LEFT:
                msg.linear.x = 0.0
                msg.angular.z = float(self.angular_speed)
                last_key = curses.KEY_LEFT
            elif key == curses.KEY_RIGHT:
                msg.linear.x = 0.0
                msg.angular.z = float(-self.angular_speed)
                last_key = curses.KEY_RIGHT

```
```python


```



### Dibujo de letras
Se seleccionaron un total de 6 letras correspondientes a "J", "G", "R", "A", "S" y "B", las cuales fueron dibujadas mediante el desplazamiento de la tortuga. Este movimiento fue controlado mediante una combinación de funciones, donde linear.x regula la velocidad lineal, angular.z controla la velocidad angular y self.wait() maneja el tiempo de duración de los movimientos. La combinación de estos parámetros permitió que la tortuga dibujara formas que se asemejan a las letras objetivo.





