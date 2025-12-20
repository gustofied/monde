import glfw
from OpenGL.GL import *
import glfw.GLFW as GLFW_CONSTANTS
from OpenGL.GL.shaders import compileShader
import numpy as np
import ctypes
from pathlib import Path
import math
# Paths

dir = Path(__file__).resolve().parent
vertex_shader_path = dir / "shaders" / "experimental_square_vertex.txt"
fragment_shader_path = dir / "shaders" / "experimental_square_fragment.txt"


glfw.init()
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, 3 )
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, 3 )
glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, GLFW_CONSTANTS.GLFW_TRUE)
glfw.window_hint(GLFW_CONSTANTS.GLFW_RESIZABLE, GLFW_CONSTANTS.GLFW_TRUE)
window = glfw.create_window(400,400, "testing", None, None)
glfw.make_context_current(window)
glfw.swap_interval(0)


vertices = np.array(
    [
        [0.5, 0.5, 0.0],
        [0.5, -0.5, 0.0],
        [-0.5, -0.5, 0.0],
    ],
    dtype = np.float32
) 

r = 1
N = 64

angles = np.linspace(0, 2*np.pi, N, endpoint=False).astype(np.float32)
x_coordinates = r * np.cos(angles)
y_coordinates = r * np.sin(angles)
z_coordaintes = np.zeros_like(x_coordinates)

vertices = np.column_stack((x_coordinates, y_coordinates, z_coordaintes)).astype(np.float32)





with open(vertex_shader_path, 'r') as file:
    shaderV = file.read()

vertexShader = glCreateShader(GL_VERTEX_SHADER)
glShaderSource(vertexShader, shaderV)
glCompileShader(vertexShader)

successV = glGetShaderiv(vertexShader, GL_COMPILE_STATUS)
print(successV) # 1 means it compiled successfully ..

# fragment shader

with open(fragment_shader_path, 'r') as file:
    shaderF = file.read()

fragmentShader = glCreateShader(GL_FRAGMENT_SHADER)
glShaderSource(fragmentShader, shaderF)
glCompileShader(fragmentShader)

successF = glGetShaderiv(fragmentShader, GL_COMPILE_STATUS)
print(successF) # 1 means it compiled successfully ..

# shader programme

shaderProgram = glCreateProgram()

glAttachShader(shaderProgram, vertexShader)
glAttachShader(shaderProgram, fragmentShader)
glLinkProgram(shaderProgram)

successP = glGetProgramiv(shaderProgram, GL_LINK_STATUS)
print(successP)

# now that we have linked shader objects and compilled our programme, let's delete the objects..

glDeleteShader(vertexShader)
glDeleteShader(fragmentShader)


# VAO / VBO

vao = glGenVertexArrays(1)
vbo = glGenBuffers(1)

glBindVertexArray(vao)

glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))
glEnableVertexAttribArray(0)


# render loop

while not glfw.window_should_close(window):
    if glfw.get_key(window,GLFW_CONSTANTS.GLFW_KEY_ESCAPE) == GLFW_CONSTANTS.GLFW_PRESS:
        glfw.set_window_should_close(window, True) 
    glfw.poll_events()
    glClearColor(0.5, 0.2, 0, 0.2)
    glClear(GL_COLOR_BUFFER_BIT)

    time_passed = glfw.get_time()
    glfw.set_window_title(window, f"Experimental")

    glUseProgram(shaderProgram)
    glBindVertexArray(vao)
    glDrawArrays(GL_LINE_LOOP, 0, 64)
    glDrawArrays(GL_TRIANGLES, 0, 3)

    
    # do stuff here

    glfw.swap_buffers(window)

# cleaning up

glfw.terminate()
