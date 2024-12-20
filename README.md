# Визуализация эквипотенциальных линий и электрических полей

## Описание

Этот проект реализует интерактивную визуализацию эквипотенциальных линий и электрических полей, создаваемых системой точечных зарядов и диполей. Пользователь может добавлять заряды, задавать их величины и координаты, а также добавлять диполи, задавая их положения, направления и величины дипольных моментов. Программа рассчитывает и отображает направления и величины сил и моментов, действующих на диполи.

## Используемые формулы и законы

- **Электрический потенциал** для точечного заряда:

  <p align="center">
    V = Q / r
  </p>

  где:
  - Q — величина заряда,
  - r — расстояние от заряда до точки наблюдения.

  Суммарный потенциал в каждой точке плоскости рассчитывается как сумма вкладов всех зарядов:

  <p align="center">
    V<sub>total</sub> = Σ (Qᵢ / rᵢ)
  </p>

  где rᵢ — расстояние от i-го заряда до точки наблюдения.

- **Электрическое поле** создаётся градиентом потенциала и представляется векторным полем:
  
  <p align="center">
    E = -∇V
  </p>

- **Сила, действующая на диполь**, рассчитывается по формуле:
  
  <p align="center">
    F = (p · ∇)E
  </p>

  где:
  - \(p\) — дипольный момент,
  - \(E\) — электрическое поле.

- **Момент силы на диполе** рассчитывается как:
  
  <p align="center">
    τ = p × E
  </p>

  где:
  - \(p\) — дипольный момент,
  - \(E\) — электрическое поле в точке диполя.

## Как использовать

### Запуск приложения:

1. Скачайте и запустите файл `run.exe`.
2. Откроется окно приложения, в котором вы сможете добавлять заряды, диполи, удалять их и наблюдать график.

### Настройка параметров:

- Для добавления **заряда**:
  1. Нажмите кнопку **"Добавить заряд"**.
  2. Введите величину заряда (может быть положительной или отрицательной).
  3. Введите координаты \(X\) и \(Y\).
  4. Заряд добавится на график и отобразится в информационном окне.

- Для добавления **диполя**:
  1. Нажмите кнопку **"Добавить диполь"**.
  2. Введите координаты центра диполя (\(X, Y\)).
  3. Введите модуль дипольного момента (\(p\)).
  4. Введите угол направления диполя в градусах (\(θ\)).
  5. Диполь добавится на график и отобразится в информационном окне с расчётом силы \(F\) и момента \(\tau\).

### Построение графика:

После добавления зарядов и диполей нажмите кнопку **"Построить потенциал и поле"**, чтобы построить график. Программа отобразит:

1. **Эквипотенциальные линии** (синие изолинии).
2. **Линии электрического поля** (черные стрелки).
3. **Заряды и диполи**:
   - Заряды отображаются как точки (красные для положительных и синие для отрицательных).
   - Диполи отображаются как зелёные стрелки, указывающие направление дипольного момента.

### График:

- Диапазон координат: от \(-20\) до \(20\) по осям \(X\) и \(Y\).
- Масштаб фиксированный, чтобы обеспечить наглядность распределения поля.

### Расчёт результатов:

Для каждого диполя программа рассчитывает:
- **Силу \(F\)**, действующую на диполь.
- **Момент силы \(\tau\)**.

Эти значения отображаются в информационном окне рядом с параметрами диполя.


## Видео
https://github.com/user-attachments/assets/ac2581a8-65a7-4c04-acb2-9dc82ec69b91
