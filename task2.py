import turtle

def draw_pifagoras_tree(t, branch_length, level):
    if level == 0:
        return
    t.forward(branch_length)
    t.left(45)
    draw_pifagoras_tree(t, branch_length * 0.6, level - 1)
    t.right(90)
    draw_pifagoras_tree(t, branch_length * 0.6, level - 1)
    t.left(45)
    t.backward(branch_length)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    branch_length = 100

    t = turtle.Turtle()
    my_window = turtle.Screen()

    t.speed(0)
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    draw_pifagoras_tree(t, branch_length, level)

    my_window.mainloop()


if __name__ == "__main__":
    main()