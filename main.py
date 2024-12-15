import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import simpledialog, messagebox
import math

class Charge:
    def __init__(self, q, x, y):
        self.q = q
        self.x = x
        self.y = y

class Dipole:
    def __init__(self, px, py, x, y, angle_deg):
        self.px = px  # Dipole moment in x
        self.py = py  # Dipole moment in y
        self.x = x    # Position x
        self.y = y    # Position y
        self.angle_deg = angle_deg  # Direction angle in degrees
        self.force = (0, 0)  # To be calculated
        self.torque = 0      # To be calculated

class EquipotentialApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Визуализация эквипотенциальных линий и линий электрического поля")

        # Списки зарядов и диполей
        self.charges = []
        self.dipoles = []

        # Настройка интерфейса
        self.setup_ui()

        # Построить график при запуске
        self.plot_initial_graph()

    def setup_ui(self):
        # Верхняя панель с кнопками
        btn_frame = tk.Frame(self.master)
        btn_frame.pack(side=tk.TOP, pady=10)

        add_charge_btn = tk.Button(btn_frame, text="Добавить заряд", command=self.add_charge)
        add_charge_btn.pack(side=tk.LEFT, padx=5)

        add_dipole_btn = tk.Button(btn_frame, text="Добавить диполь", command=self.add_dipole)
        add_dipole_btn.pack(side=tk.LEFT, padx=5)

        plot_btn = tk.Button(btn_frame, text="Построить потенциал и поле", command=self.plot_potential)
        plot_btn.pack(side=tk.LEFT, padx=5)

        clear_btn = tk.Button(btn_frame, text="Очистить заряды и диполи", command=self.clear_entities)
        clear_btn.pack(side=tk.LEFT, padx=5)

        # Информационная панель для зарядов и диполей
        info_frame = tk.Frame(self.master)
        info_frame.pack(side=tk.TOP, pady=10)

        # Фрейм для зарядов
        charge_frame = tk.Frame(info_frame)
        charge_frame.pack(side=tk.LEFT, padx=10)

        charge_label = tk.Label(charge_frame, text="Заряды:")
        charge_label.pack()
        self.charge_list = tk.Listbox(charge_frame, height=5, width=30)
        self.charge_list.pack()

        # Фрейм для диполей
        dipole_frame = tk.Frame(info_frame)
        dipole_frame.pack(side=tk.LEFT, padx=10)

        dipole_label = tk.Label(dipole_frame, text="Диполи:")
        dipole_label.pack()
        self.dipole_list = tk.Listbox(dipole_frame, height=5, width=50)
        self.dipole_list.pack()

        # Полотно для графика
        self.figure, self.ax = plt.subplots(figsize=(8, 6))  # Увеличенный размер графика
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def add_charge(self):
        # Диалог для ввода параметров заряда
        try:
            q_str = simpledialog.askstring("Ввод", "Введите величину заряда (q):", parent=self.master)
            if q_str is None:
                return  # Пользователь отменил ввод
            q = float(q_str)
            x_str = simpledialog.askstring("Ввод", "Введите координату X:", parent=self.master)
            if x_str is None:
                return
            x = float(x_str)
            y_str = simpledialog.askstring("Ввод", "Введите координату Y:", parent=self.master)
            if y_str is None:
                return
            y = float(y_str)
            charge = Charge(q, x, y)
            self.charges.append(charge)
            self.charge_list.insert(tk.END, f"q={q} @ ({x}, {y})")
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректный ввод. Пожалуйста, введите числовые значения.")

    def add_dipole(self):
        # Диалог для ввода параметров диполя
        try:
            x_str = simpledialog.askstring("Ввод", "Введите координату X диполя:", parent=self.master)
            if x_str is None:
                return
            x = float(x_str)
            y_str = simpledialog.askstring("Ввод", "Введите координату Y диполя:", parent=self.master)
            if y_str is None:
                return
            y = float(y_str)
            p_str = simpledialog.askstring("Ввод", "Введите модуль дипольного момента (p):", parent=self.master)
            if p_str is None:
                return
            p = float(p_str)
            angle_str = simpledialog.askstring("Ввод", "Введите угол направления диполя (в градусах):", parent=self.master)
            if angle_str is None:
                return
            angle_deg = float(angle_str)
            angle_rad = math.radians(angle_deg)
            px = p * math.cos(angle_rad)
            py = p * math.sin(angle_rad)
            dipole = Dipole(px, py, x, y, angle_deg)
            self.dipoles.append(dipole)
            # Первоначальное добавление диполя без сил и моментов
            self.dipole_list.insert(tk.END, f"p={p} @ ({x}, {y}) θ={angle_deg}° F=(-, -) τ=-")
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректный ввод. Пожалуйста, введите числовые значения.")

    def clear_entities(self):
        self.charges.clear()
        self.dipoles.clear()
        self.charge_list.delete(0, tk.END)
        self.dipole_list.delete(0, tk.END)
        self.ax.clear()
        self.plot_initial_graph()

    def plot_initial_graph(self):
        # Построить пустую область графика с увеличенным масштабом и уменьшенными шрифтами
        self.ax.clear()
        self.ax.set_xlim(-20, 20)  # Увеличенный масштаб
        self.ax.set_ylim(-20, 20)  # Увеличенный масштаб
        self.ax.set_title("Эквипотенциальные линии и линии электрического поля", fontsize=8)  # Уменьшенный размер шрифта
        self.ax.set_xlabel("X", fontsize=7)  # Уменьшенный размер шрифта
        self.ax.set_ylabel("Y", fontsize=7)  # Уменьшенный размер шрифта
        self.ax.set_aspect('equal')
        self.ax.grid(True)
        self.canvas.draw()

    def plot_potential(self):
        if not self.charges and not self.dipoles:
            messagebox.showwarning("Предупреждение", "Нет зарядов или диполей для отображения.")
            return

        # Создание сетки
        x = np.linspace(-20, 20, 500)  # Увеличенный диапазон для масштабирования
        y = np.linspace(-20, 20, 500)  # Увеличенный диапазон для масштабирования
        X, Y = np.meshgrid(x, y)

        # Вычисление потенциала
        V = np.zeros_like(X)
        epsilon0 = 1  # Для упрощения единиц

        # Вклад от зарядов
        for charge in self.charges:
            r = np.sqrt((X - charge.x)**2 + (Y - charge.y)**2)
            r[r == 0] = 1e-9  # Избежание деления на 0
            V += charge.q / r

        # Вклад от диполей
        for dipole in self.dipoles:
            dx = X - dipole.x
            dy = Y - dipole.y
            r_squared = dx**2 + dy**2
            r = np.sqrt(r_squared)
            # Потенциал диполя
            V += (dipole.px * dx + dipole.py * dy) / (r_squared * r)

        # Ограничение потенциала для улучшения визуализации
        V = np.clip(V, -100, 100)

        # Вычисление электрического поля
        E_x, E_y = self.compute_electric_field(X, Y)

        # Вклад от диполей в электрическое поле
        for dipole in self.dipoles:
            dx = X - dipole.x
            dy = Y - dipole.y
            r_squared = dx**2 + dy**2
            r = np.sqrt(r_squared)
            r_five = r_squared**2.5
            # Избежание деления на 0
            r_five[r_five == 0] = 1e-9
            # Электрическое поле диполя
            E_x += (3 * (dipole.px * dx + dipole.py * dy) * dx - dipole.px * r_squared) / r_five
            E_y += (3 * (dipole.px * dx + dipole.py * dy) * dy - dipole.py * r_squared) / r_five

        # Очистка предыдущего графика
        self.ax.clear()

        # Построение линий электрического поля
        magnitude = np.sqrt(E_x**2 + E_y**2)
        # Чтобы избежать слишком плотных линий, можно установить маску
        E_x_plot = np.ma.masked_where(magnitude == 0, E_x)
        E_y_plot = np.ma.masked_where(magnitude == 0, E_y)
        self.ax.streamplot(X, Y, E_x_plot, E_y_plot, color='k', density=1.0, linewidth=0.5, arrowsize=1)

        # Построение изолиний потенциала
        levels = np.linspace(-50, 50, 100)
        contours = self.ax.contour(X, Y, V, levels=levels, cmap='Blues')
        self.ax.set_title("Эквипотенциальные линии и линии электрического поля", fontsize=8)  # Уменьшенный размер шрифта
        self.ax.set_xlabel("X", fontsize=7)  # Уменьшенный размер шрифта
        self.ax.set_ylabel("Y", fontsize=7)  # Уменьшенный размер шрифта
        self.ax.set_aspect('equal')

        # Фиксация масштаба
        self.ax.set_xlim(-20, 20)  # Увеличенный масштаб
        self.ax.set_ylim(-20, 20)  # Увеличенный масштаб

        # Отображение зарядов
        for charge in self.charges:
            color = 'r' if charge.q > 0 else 'b'
            self.ax.plot(charge.x, charge.y, marker='o', color=color, markersize=10)

        # Отображение диполей и расчёт сил и моментов
        for dipole in self.dipoles:
            # Визуализация диполя как стрелки
            # Уменьшение длины для лучшей визуализации
            self.ax.arrow(dipole.x, dipole.y, dipole.px*0.05, dipole.py*0.05,
                          head_width=0.5, head_length=1, fc='g', ec='g')

            # Расчёт электрического поля в точке диполя
            E_dipole_x, E_dipole_y = self.compute_electric_field_at_point(dipole.x, dipole.y)

            # Расчёт градиентов электрического поля в точке диполя
            grad_E = self.compute_field_gradients_at_point(dipole.x, dipole.y)

            # Расчёт силы: F = (p · ∇)E
            F_x = dipole.px * grad_E['E_x_dx'] + dipole.py * grad_E['E_x_dy']
            F_y = dipole.px * grad_E['E_y_dx'] + dipole.py * grad_E['E_y_dy']
            dipole.force = (F_x, F_y)

            # Расчёт момента силы: τ = p × E
            torque = dipole.px * E_dipole_y - dipole.py * E_dipole_x
            dipole.torque = torque

        # Добавление легенды
        charge_positive = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='r', markersize=5, label='Положительный заряд')
        charge_negative = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='b', markersize=5, label='Отрицательный заряд')
        self.ax.legend(handles=[charge_positive, charge_negative], fontsize=5, loc='upper right')

        # Обновление информационных панелей
        self.update_info_panels()

        self.ax.grid(True)
        self.canvas.draw()

    def update_info_panels(self):
        # Обновление списка диполей с информацией о силе и моменте
        self.dipole_list.delete(0, tk.END)
        for dipole in self.dipoles:
            force_x, force_y = dipole.force
            torque = dipole.torque
            self.dipole_list.insert(tk.END, f"p={math.sqrt(dipole.px**2 + dipole.py**2):.2f} @ ({dipole.x}, {dipole.y}) θ={dipole.angle_deg:.1f}° F=({force_x:.2f}, {force_y:.2f}) τ={torque:.2f}")

    def compute_electric_field(self, X, Y):
        E_x = np.zeros_like(X)
        E_y = np.zeros_like(Y)
        for charge in self.charges:
            dx = X - charge.x
            dy = Y - charge.y
            r_squared = dx**2 + dy**2
            r_cubed = np.power(r_squared, 1.5)
            r_cubed[r_cubed == 0] = 1e-9  # Избежание деления на 0
            E_x += charge.q * dx / r_cubed
            E_y += charge.q * dy / r_cubed
        return E_x, E_y

    def compute_electric_field_at_point(self, x, y):
        E_x = 0
        E_y = 0
        for charge in self.charges:
            dx = x - charge.x
            dy = y - charge.y
            r_squared = dx**2 + dy**2
            r_cubed = r_squared * math.sqrt(r_squared)
            if r_cubed == 0:
                continue  # Избежание деления на 0
            E_x += charge.q * dx / r_cubed
            E_y += charge.q * dy / r_cubed
        # Вклад от диполей
        for dipole in self.dipoles:
            dx = x - dipole.x
            dy = y - dipole.y
            r_squared = dx**2 + dy**2
            r_five = r_squared**2.5
            if r_five == 0:
                continue
            E_x += (3 * (dipole.px * dx + dipole.py * dy) * dx - dipole.px * r_squared) / r_five
            E_y += (3 * (dipole.px * dx + dipole.py * dy) * dy - dipole.py * r_squared) / r_five
        return E_x, E_y

    def compute_field_gradients_at_point(self, x, y):
        # Вычисление градиентов электрического поля в точке (x, y)
        dE_x_dx = 0
        dE_x_dy = 0
        dE_y_dx = 0
        dE_y_dy = 0
        for charge in self.charges:
            dx = x - charge.x
            dy = y - charge.y
            r_squared = dx**2 + dy**2
            r = math.sqrt(r_squared)
            r_five = r_squared**2.5
            if r_five == 0:
                continue  # Избежание деления на 0
            q = charge.q
            # Производные электрического поля для точечного заряда
            dE_x_dx += q * (3 * dx**2) / r_five
            dE_x_dy += q * (3 * dx * dy) / r_five
            dE_y_dx += q * (3 * dx * dy) / r_five
            dE_y_dy += q * (3 * dy**2) / r_five
        # Вклад от диполей в градиенты поля
        for dipole in self.dipoles:
            dx = x - dipole.x
            dy = y - dipole.y
            r_squared = dx**2 + dy**2
            r = math.sqrt(r_squared)
            r_five = r_squared**2.5
            if r_five == 0:
                continue
            px = dipole.px
            py = dipole.py
            # Производные электрического поля для диполя
            dE_x_dx += (3 * px * dx * dx - px * r_squared) / r_five
            dE_x_dy += (3 * px * dx * dy) / r_five
            dE_y_dx += (3 * py * dx * dy) / r_five
            dE_y_dy += (3 * py * dy * dy - py * r_squared) / r_five
        return {'E_x_dx': dE_x_dx, 'E_x_dy': dE_x_dy,
                'E_y_dx': dE_y_dx, 'E_y_dy': dE_y_dy}

def main():
    root = tk.Tk()
    app = EquipotentialApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
