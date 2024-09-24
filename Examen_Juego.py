'''
Examen 1era Unidad
'''
import tkinter as tk
from tkinter import messagebox
import random

# Clase del juego
class Game:
    def __init__(self):
        self.score = 0  # Puntaje inicial
        self.level = 1  # Nivel inicial

    def mostrar_puntaje_total(self):
        messagebox.showinfo("Puntaje Total", f"Tu puntaje total es: {self.score}")

# Ventana de bienvenida
def mostrar_bienvenida():
    bienvenida = tk.Tk()
    bienvenida.title("Bienvenido a NitoAttack")
    bienvenida.geometry("400x300")

    lbl_bienvenida = tk.Label(bienvenida, text="¡Bienvenido a NitoAttack!", font=("Helvetica", 16))
    lbl_bienvenida.pack(pady=50)

    btn_comenzar = tk.Button(bienvenida, text="Comenzar", command=lambda: iniciar_ventana_principal(bienvenida), width=20)
    btn_comenzar.pack(pady=10)

    btn_instrucciones = tk.Button(bienvenida, text="Instrucciones", command=lambda: [bienvenida.destroy(), mostrar_instrucciones()], width=20)
    btn_instrucciones.pack(pady=10)

    btn_salir = tk.Button(bienvenida, text="Salir", command=bienvenida.quit, width=20)
    btn_salir.pack(pady=10)

    bienvenida.mainloop()

# Ventana de instrucciones
def mostrar_instrucciones():
    instrucciones = tk.Tk()
    instrucciones.title("Instrucciones")
    instrucciones.geometry("800x600")
    instrucciones.resizable(False, False)

    texto_instrucciones = (
        "Instrucciones del juego:\n\n"
        "1. Selecciona 'Jugar' para iniciar la batalla.\n"
        "2. Durante el juego, elige atacar o huir.\n"
        "3. Atacar destruye a tu enemigo.\n"
        "4. Huir hace que consigas menos puntos pero logres tu objetivo.\n"
        "5. Derrota a todos los enemigos para conseguir una puntuación máxima.\n"
        "6. Tu puntaje aumentará con cada enemigo derrotado.\n"
    )

    tk.Label(instrucciones, text=texto_instrucciones, font=("Helvetica", 14), justify="left").pack(pady=20)
    tk.Button(instrucciones, text="Jugar", command=lambda: [instrucciones.destroy(), iniciar_ventana_principal(None)]).pack(pady=10)

    instrucciones.mainloop()

# Ventana principal
def iniciar_ventana_principal(bienvenida):
    if bienvenida:
        bienvenida.destroy()  # Cerrar la ventana de bienvenida
    global root
    root = tk.Tk()
    root.title("NitoAttack")
    root.geometry("800x600")

    global game
    game = Game()

    btn_play = tk.Button(root, text="Jugar", command=iniciar_juego, width=20)
    btn_play.pack(pady=10)

    btn_exit = tk.Button(root, text="Salir", command=lambda: [game.mostrar_puntaje_total(), root.quit()], width=20)
    btn_exit.pack(pady=10)

    root.mainloop()

# Nueva función para iniciar el juego en una nueva ventana
def iniciar_juego():
    global game_window, board
    root.withdraw()  # Ocultar la ventana principal

    game_window = tk.Tk()
    game_window.title("NitoAttack - Juego en Progreso")
    game_window.geometry("800x600")

    board = tk.Canvas(game_window, width=400, height=400)
    board.pack()

    control_frame = tk.Frame(game_window)
    control_frame.pack()

    tk.Button(control_frame, text="Arriba", command=lambda: move_player(0, -1)).grid(row=0, column=1)
    tk.Button(control_frame, text="Izquierda", command=lambda: move_player(-1, 0)).grid(row=1, column=0)
    tk.Button(control_frame, text="Derecha", command=lambda: move_player(1, 0)).grid(row=1, column=2)
    tk.Button(control_frame, text="Abajo", command=lambda: move_player(0, 1)).grid(row=2, column=1)

    draw_board(board)
    move_enemies_randomly()
    game_window.mainloop()

# Configuración inicial del juego
board_size = 8
player_position = (0, 0)
queen_position = (board_size-1, board_size-1)
enemies = {}
current_level = 1

def init_enemies(level):
    global enemies
    enemy_count = level + 2
    enemies = {
        "pawn": [(random.randint(1, board_size-1), random.randint(1, board_size-1)) for _ in range(enemy_count)],
        "knight": [(random.randint(1, board_size-1), random.randint(1, board_size-1)) for _ in range(level)],
        "rook": [(random.randint(1, board_size-1), random.randint(1, board_size-1)) for _ in range(1)]
    }

init_enemies(current_level)

def draw_board(canvas):
    canvas.delete("all")
    square_size = 50
    for i in range(board_size):
        for j in range(board_size):
            color = "white" if (i + j) % 2 == 0 else "gray"
            canvas.create_rectangle(i*square_size, j*square_size, (i+1)*square_size, (j+1)*square_size, fill=color)

    px, py = player_position
    canvas.create_oval(px*square_size+10, py*square_size+10, (px+1)*square_size-10, (py+1)*square_size-10, fill="blue")

    qx, qy = queen_position
    canvas.create_oval(qx*square_size+10, qy*square_size+10, (qx+1)*square_size-10, (qy+1)*square_size-10, fill="red")

    for pos in enemies["pawn"]:
        ex, ey = pos
        canvas.create_rectangle(ex*square_size+10, ey*square_size+10, (ex+1)*square_size-10, (ey+1)*square_size-10, fill="green")
    for pos in enemies["knight"]:
        ex, ey = pos
        canvas.create_rectangle(ex*square_size+10, ey*square_size+10, (ex+1)*square_size-10, (ey+1)*square_size-10, fill="purple")
    for pos in enemies["rook"]:
        ex, ey = pos
        canvas.create_rectangle(ex*square_size+10, ey*square_size+10, (ex+1)*square_size-10, (ey+1)*square_size-10, fill="yellow")

def move_player(dx, dy):
    global player_position
    new_x = player_position[0] + dx
    new_y = player_position[1] + dy

    if 0 <= new_x < board_size and 0 <= new_y < board_size:
        player_position = (new_x, new_y)
        check_collisions()
        draw_board(board)

def check_collisions():
    global current_level
    if player_position == queen_position:
        tk.messagebox.showinfo("Victoria", f"¡Has derrotado a la Reina en el nivel {current_level}! Avanzas al siguiente nivel.")
        current_level += 1
        if current_level > 3:
            game.mostrar_puntaje_total()  # Mostrar puntaje total
            game_window.quit()  # Cierra la ventana del juego
            root.quit()  # Cierra la ventana de la aplicación principal
            exit()  # Cierra la aplicación completamente
        else:
            reset_game()

    for enemy_type, positions in enemies.items():
        if player_position in positions:
            action = tk.messagebox.askquestion("¡Enemigo!", f"Te has encontrado con un {enemy_type}. ¿Quieres enfrentarlo?")
            if action == 'yes':
                defeat_enemy(enemy_type, player_position)
            else:
                move_player(-1, -1)

def defeat_enemy(enemy_type, position):
    enemies[enemy_type].remove(position)
    tk.messagebox.showinfo("Éxito", f"¡Has derrotado al {enemy_type}!")
    if enemy_type == "pawn":
        game.score += 15
    elif enemy_type == "knight":
        game.score += 25
    elif enemy_type == "rook":
        game.score += 50
    draw_board(board)

def reset_game():
    global player_position, queen_position
    player_position = (0, 0)
    queen_position = (board_size-1, board_size-1)
    init_enemies(current_level)
    draw_board(board)

def move_enemies_randomly():
    for enemy_type in enemies:
        new_positions = []
        for ex, ey in enemies[enemy_type]:
            new_x = ex + random.choice([-1, 0, 1])
            new_y = ey + random.choice([-1, 0, 1])
            if 0 <= new_x < board_size and 0 <= new_y < board_size:
                new_positions.append((new_x, new_y))
        enemies[enemy_type] = new_positions
    draw_board(board)
    game_window.after(1000, move_enemies_randomly)

# Iniciar el juego
if __name__ == "__main__":
    mostrar_bienvenida()
