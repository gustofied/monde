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
vertex_shader_path = dir / "shaders" / "experimental_shaded_vertex.txt"
fragment_shader_path = dir / "shaders" / "experimental_shaded_fragment.txt"

# window

glfw.init()
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, 3 )
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, 3 )
glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, GLFW_CONSTANTS.GLFW_TRUE)
glfw.window_hint(GLFW_CONSTANTS.GLFW_RESIZABLE, GLFW_CONSTANTS.GLFW_TRUE)
window = glfw.create_window(400, 400, "shaded", None, None)
glfw.make_context_current(window)
glfw.swap_interval(0)


# prepare data

vertices = np.array([
    [-0.5, 0.5,  0.0, 1.0, 0.0,  0.0, ],
    [-0.5, -0.5, 0.0, 0.0, 1.0,  0.0, ],
    [0.5, -0.5,  0.0, 0.0, 0.0,  1.0, ]
    ], dtype = np.float32
)


# shaders

## Vertex Shader

with open(vertex_shader_path,"r") as file:
    shaderV = file.read()

vertexShader = glCreateShader(GL_VERTEX_SHADER)
glShaderSource(vertexShader, shaderV)
glCompileShader(vertexShader)


## Fragment Shader

with open( fragment_shader_path, "r") as file:
    shaderF = file.read()

fragmentShader = glCreateShader(GL_FRAGMENT_SHADER)
glShaderSource(fragmentShader, shaderF)
glCompileShader(fragmentShader)


## Compile Programme

shaderProgram = glCreateProgram()

glAttachShader(shaderProgram, vertexShader)
glAttachShader(shaderProgram, fragmentShader)
glLinkProgram(shaderProgram)


successP = glGetProgramiv(shaderProgram, GL_LINK_STATUS)
print(successP)


## Clean Up

glDeleteShader(vertexShader)
glDeleteShader(fragmentShader)


# init

glClearColor(0.2, 0.2, 0.0, 0.2)

# VAO / VBO

vao = glGenVertexArrays(1)
vbo = glGenBuffers(1)

glBindVertexArray(vao)

glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
glEnableVertexAttribArray(0)
glEnableVertexAttribArray(1)



glUseProgram(shaderProgram)
uLoc = glGetUniformLocation(shaderProgram, "uOffest")


# render loop

while not glfw.window_should_close(window):
    
    glfw.poll_events()

    if glfw.get_key(window, GLFW_CONSTANTS.GLFW_KEY_ESCAPE) == GLFW_CONSTANTS.GLFW_PRESS:
        glfw.set_window_should_close(window, True)


    glClear(GL_COLOR_BUFFER_BIT)

    time = glfw.get_time()
    greens = ((np.sin(time) * 0.5) + 0.5)

    glUniform1f(uLoc, greens)





    glBindVertexArray(vao)
    glDrawArrays(GL_TRIANGLES, 0, 3)


    # Render here
    # Draw




    # Swap at end
    glfw.swap_buffers(window)
