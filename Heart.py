import turtle
import math
import time
import colorsys


def heart_point(t, scale):
    """Returns (x, y) on the parametric heart curve for angle t."""
    x = scale * 16 * math.sin(t) ** 3
    y = scale * (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )
    return x, y


def dim_color(rgb, factor):
    """Returns a darker version of an (r, g, b) color, for the glow halo."""
    r, g, b = rgb
    return (r * factor, g * factor, b * factor)


def draw_glow_segment(screen, x1, y1, x2, y2, color):
    """Draws one segment 3 times (wide+dim, medium+dim, thin+bright)
    to fake a soft neon glow, since turtle has no real transparency."""
    glow_pen = turtle.Turtle(visible=False)
    glow_pen.speed(0)
    glow_pen.penup()
    glow_pen.goto(x1, y1)
    glow_pen.pendown()

    for width, factor in ((9, 0.25), (5, 0.5), (2, 1.0)):
        glow_pen.pensize(width)
        glow_pen.pencolor(dim_color(color, factor))
        glow_pen.goto(x2, y2)
        glow_pen.goto(x1, y1)

    glow_pen.goto(x2, y2)


def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("Nebula Heart")
    screen.tracer(0)

    scale = 12
    steps = 360          # fewer points = a bit chunkier but much faster to draw
    delay = 0.012        # pause between points -> controls drawing speed

    hue = 0.0
    prev_x, prev_y = heart_point(0, scale)
    path_points = [(prev_x, prev_y)]

    # --- draw the glowing outline, point by point ---
    for i in range(1, steps + 1):
        t = (i / steps) * 2 * math.pi
        x, y = heart_point(t, scale)

        hue = (hue + 0.0025) % 1.0
        color = colorsys.hsv_to_rgb(hue, 1, 1)

        draw_glow_segment(screen, prev_x, prev_y, x, y, color)
        path_points.append((x, y))

        prev_x, prev_y = x, y
        screen.update()
        time.sleep(delay)

    # --- fill the heart with a rainbow gradient ---
    # turtle only allows ONE solid color per fill, so to get a rainbow
    # look we draw several nested hearts (100% down to ~15% size),
    # each a different hue, layered largest-to-smallest.
    fill_pen = turtle.Turtle(visible=False)
    fill_pen.speed(0)

    layers = 40
    for layer in range(layers):
        layer_scale = scale * (1 - layer / layers * 0.85)
        hue = layer / layers  # sweeps through the whole RGB rainbow
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)

        fill_pen.penup()
        fill_pen.goto(heart_point(0, layer_scale))
        fill_pen.pendown()
        fill_pen.pencolor((r, g, b))   # match the outline to the fill
        fill_pen.fillcolor((r, g, b))
        fill_pen.begin_fill()
        for i in range(steps + 1):
            t = (i / steps) * 2 * math.pi
            fill_pen.goto(heart_point(t, layer_scale))
        fill_pen.end_fill()

    screen.update()

    screen.mainloop()


if __name__ == "__main__":
    main()