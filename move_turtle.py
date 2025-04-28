import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import threading
import curses

class ManualTurtleController(Node):
    def __init__(self):
        super().__init__('manual_turtle_controller')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.get_logger().info('Control manual iniciado. Usa flechas o letras (j, g, r, a, s, b).')
        self.speed = 2.0
        self.angular_speed = 2.0

    def reset_position(self):
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        time.sleep(0.5)

    def draw_j(self):
        self.get_logger().info("Dibujando la letra J.")
        self.reset_position()
        msg = Twist()

        # 1️⃣ Línea a la derecha
        msg.linear.x = 1.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        time.sleep(1.0)  # Ajusta este valor para que la línea sea más o menos larga

        # 2️⃣ Línea corta hacia abajo
        msg.linear.x = 0.0
        msg.angular.z = -1.57  # Gira 90° a la derecha
        self.publisher_.publish(msg)
        time.sleep(2.0)

        msg.angular.z = 0.0
        msg.linear.x = 1.0
        self.publisher_.publish(msg)
        time.sleep(2.0)  # Línea corta hacia abajo

        # 3️⃣ Circunferencia hacia la izquierda
        msg.linear.x = 1.0
        msg.angular.z = -3.0  # Giro hacia la izquierda con movimiento
        self.publisher_.publish(msg)
        time.sleep(4.0)  # Media circunferencia (aproximadamente)

        self.stop()

    def draw_g(self):
        self.get_logger().info("Dibujando la letra G.")
        self.reset_position()
    
        # --- Hacer el círculo de 300 grados ---
        msg = Twist()
        msg.linear.x = 5.0    # Avanzar hacia adelante
        msg.angular.z = 5.5   # Girar a la izquierda (antihorario)
        self.publisher_.publish(msg)
        time_to_turn = 2.0 # aprox
        time.sleep(time_to_turn)
        
        # --- Parar el giro ---
       
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        time.sleep(1.0)

        msg.angular.z = 1.0
        self.publisher_.publish(msg)
        time.sleep(1.0)
        # --- Avanzar línea hacia la izquierda ---
        # Como quedó mirando hacia la izquierda después del círculo,
        # solo debe avanzar recto.
        msg.linear.x = 1.0
        self.publisher_.publish(msg)
        
        # Avanzar un tiempo corto (ajusta si quieres más largo)
        time.sleep(1.0)
        
        # --- Detenerse ---
        self.stop()
    def draw_r(self):
        self.get_logger().info("Dibujando la letra R.")
        self.reset_position()
        msg = Twist()
        msg.linear.x = -1.0
        self.publisher_.publish(msg)
        time.sleep(1)
        msg.angular.z = -4.5
        self.publisher_.publish(msg)
        time.sleep(1)
        msg.linear.x = 2.0
        self.publisher_.publish(msg)
        time.sleep(0.5)
        msg.angular.z = -0.1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        self.publisher_.publish(msg)
        time.sleep(0.25)
       
        self.stop()

    def draw_a(self):
        self.get_logger().info("Dibujando la letra A.")
        self.reset_position()
        msg = Twist()
        msg.linear.x = 1.0
        self.publisher_.publish(msg)
        time.sleep(1)
        msg.angular.z = -1.0
        self.publisher_.publish(msg)
        time.sleep(1)
        msg.linear.x = 0.5
        self.publisher_.publish(msg)
        time.sleep(0.5)
        msg.angular.z = 1.0
        self.publisher_.publish(msg)
        time.sleep(0.5)
        self.stop()

    def draw_s(self):
        self.get_logger().info("Dibujando la letra S.")
        self.reset_position()
        msg = Twist()
        msg.linear.x = 1.0
        self.publisher_.publish(msg)
        time.sleep(1)
        msg.angular.z = 1.0
        self.publisher_.publish(msg)
        time.sleep(1)
        msg.linear.x = -0.5
        self.publisher_.publish(msg)
        time.sleep(0.5)
        msg.angular.z = -1.0
        self.publisher_.publish(msg)
        time.sleep(1)
        msg.linear.x = -0.5
        self.publisher_.publish(msg)
        time.sleep(0.5)
        self.stop()

    def draw_b(self):
        self.get_logger().info("Dibujando la letra B.")
        self.reset_position()
        msg = Twist()
        msg.linear.x = 1.0
        self.publisher_.publish(msg)
        time.sleep(1)
        msg.angular.z = 1.0
        self.publisher_.publish(msg)
        time.sleep(1)
        msg.linear.x = 0.5
        self.publisher_.publish(msg)
        time.sleep(0.5)
        msg.angular.z = -1.0
        self.publisher_.publish(msg)
        time.sleep(1)
        msg.linear.x = 0.5
        self.publisher_.publish(msg)
        time.sleep(0.5)
        self.stop()

    def stop(self):
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)

    def run(self, stdscr):
        curses.curs_set(0)
        stdscr.nodelay(1)
        stdscr.timeout(100)
        msg = Twist()
        last_key = None

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
            elif key in [ord('j'), ord('g'), ord('r'), ord('a'), ord('s'), ord('b')]:
                msg.linear.x = 0.0
                msg.angular.z = 0.0
                self.publisher_.publish(msg)  # Detener antes de empezar a dibujar
                if key == ord('j'):
                    self.draw_j()
                elif key == ord('g'):
                    self.draw_g()
                elif key == ord('r'):
                    self.draw_r()
                elif key == ord('a'):
                    self.draw_a()
                elif key == ord('s'):
                    self.draw_s()
                elif key == ord('b'):
                    self.draw_b()
                last_key = None
            else:
                msg.linear.x = 0.0
                msg.angular.z = 0.0
                last_key = None

            # Publicar solo si hay movimiento
            if last_key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
                self.publisher_.publish(msg)

            time.sleep(0.1)

def main(args=None):
    rclpy.init(args=args)
    node = ManualTurtleController()
    threading.Thread(target=rclpy.spin, args=(node,), daemon=True).start()
    curses.wrapper(node.run)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
