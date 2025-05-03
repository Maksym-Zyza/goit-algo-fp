import turtle
import math

def draw_pythagoras_tree(t, length, depth):
    if depth == 0:
        return

    # Draw square
    for _ in range(4):
        t.forward(length)
        t.left(90)

    # Save current position and angle
    pos = t.pos()
    angle = t.heading()

    # Left branch
    t.left(45)
    new_length = length * math.sqrt(2) / 2
    draw_pythagoras_tree(t, new_length, depth - 1)

    # Restore position
    t.setpos(pos)
    t.setheading(angle)

    # Right branch
    t.right(45)
    t.forward(length)
    t.right(45)
    draw_pythagoras_tree(t, new_length, depth - 1)

    # Restore position
    t.setpos(pos)
    t.setheading(angle)

def main():
    try:
        depth = int(input("Enter recursion depth (0–10): "))
        if depth < 0:
            print("Please enter a non-negative integer.")
            return
        elif depth > 10:
            print("Depth too high. Using 10.")
            depth = 10

        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.goto(-50, -200)
        t.setheading(90)
        t.pendown()
        t.color("green")

        draw_pythagoras_tree(t, 100, depth)

        turtle.done()

    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
