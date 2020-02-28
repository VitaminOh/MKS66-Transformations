from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    with open(fname) as script:
        command = script.readline()
        while command:
            if command.strip("\n") == "line":
                command = script.readline()
                values = command.split()
                add_edge(points, int(values[0]), int(values[1]), int(values[2]), int(values[3]), int(values[4]), int(values[5]))
            if command.strip("\n") == "ident":
                ident(transform)
            if command.strip("\n") == "scale":
                command = script.readline()
                values = command.split()
                scale = make_scale(int(values[0]), int(values[1]), int(values[2]));
                matrix_mult(scale, transform)
            if command.strip("\n") == "move":
                command = script.readline()
                values = command.split()
                translate = make_translate(int(values[0]), int(values[1]), int(values[2]));
                matrix_mult(translate, transform)
            if command.strip("\n") == "rotate":
                command = script.readline()
                values = command.split()
                rotate = new_matrix()
                if values[0] == "x":
                    rotate = make_rotX(int(values[1]))
                elif values[0] == "y":
                    rotate = make_rotY(int(values[1]))
                elif values[0] == "z":
                    rotate = make_rotZ(int(values[1]))
                matrix_mult(rotate, transform)
            if command.strip("\n") == "apply":
                matrix_mult(transform, points)
                round_matrix(points)
            if command.strip("\n") == "display":
                clear_screen(screen)
                draw_lines(points, screen, color)
                display(screen)
            if command.strip("\n") == "save":
                command = script.readline()
                values = command.split()
                clear_screen(screen)
                draw_lines(points, screen, color)
                save_ppm(screen, "img.ppm")
                save_extension(screen, values[0])
            if command.strip("\n") == "quit":
                break
            command = script.readline()
