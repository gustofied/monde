import OpenGL.GL as GL
from OpenGL.GL import glCompileShader
import glfw
import glfw.GLFW as GLFW_CONSTANTS
import numpy as np
from pathlib import Path
import math
import ctypes
# window


glfw.init()
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, GLFW_CONSTANTS.GLFW_TRUE)
window = glfw.create_window(400, 400, "Line", None, None)
glfw.make_context_current(window)
glfw.swap_interval(0)

# paths

dir = Path(__file__).resolve().parent
vertex_shader_path = dir / "shaders" / "experimental_line_vertex.txt"
fragment_shader_path = dir / "shaders" / "experimental_line_fragment.txt"

print(vertex_shader_path.exists())
print(fragment_shader_path.exists())

with open(vertex_shader_path) as file:
    shaderV = file.read()

with open(fragment_shader_path) as file:
    shaderF = file.read()

print(shaderV)
print(shaderF)

vertexShader = GL.glCreateShader(GL.GL_VERTEX_SHADER)
GL.glShaderSource(vertexShader, shaderV)
glCompileShader(vertexShader)

fragmentShader = GL.glCreateShader(GL.GL_FRAGMENT_SHADER)
GL.glShaderSource(fragmentShader, shaderF)
glCompileShader(fragmentShader)

shaderProgamme = GL.glCreateProgram()
GL.glAttachShader(shaderProgamme, vertexShader)
GL.glAttachShader(shaderProgamme, fragmentShader)
GL.glLinkProgram(shaderProgamme)

GL.glDeleteShader(vertexShader)
GL.glDeleteShader(fragmentShader)

vertices = np.array([
    [0.2, 0.5, 0.0],
    [-0.2, 0.9, 0.0]], dtype=np.float32)

N = 50
R = 5

angles = np.linspace(0, 2*np.pi, N)
print(angles)

x_coordinates = R * np.cos(angles)
y_coordinates = R * np.sin(angles)
z_coordinates = np.zeros(N)

xyz_coordintes = np.concatenate([x_coordinates, y_coordinates, z_coordinates], axis=0).astype(np.float32)
print(xyz_coordintes)
# vao and vbo

vao = GL.glGenVertexArrays(1)
vbo = GL.glGenBuffers(1)
ebo = GL.glGenBuffers(1)

GL.glBindVertexArray(vao)
GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vbo)
GL.glBufferData(GL.GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL.GL_STATIC_DRAW)
GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 12, ctypes.c_void_p(0))
GL.glEnableVertexAttribArray(0)



GL.glUseProgram(shaderProgamme)

while not glfw.window_should_close(window):
    glfw.poll_events()
    if glfw.get_key(window,GLFW_CONSTANTS.GLFW_KEY_ESCAPE) == GLFW_CONSTANTS.GLFW_PRESS:
        glfw.set_window_should_close(window, GLFW_CONSTANTS.GLFW_TRUE)
    
    GL.glClearColor(0.75, 0.25, 0.75, 1)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    ## draw
    GL.glDrawArrays(GL.GL_LINES, 0, 2)

    glfw.swap_buffers(window)