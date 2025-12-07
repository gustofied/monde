import glfw
from OpenGL.GL import *
import glfw.GLFW as GLFW_CONSTANTS
from OpenGL.GL.shaders import compileShader
import numpy as np
import ctypes
from pathlib import Path

# Paths

dir = Path(__file__).resolve().parent
vertex_shader_path = dir / "shaders" / "experimental_vertex.txt"
fragment_shader_path = dir / "shaders" / "experimental_fragment.txt"


# glfw 

glfw.init()
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_PROFILE, GLFW_CONSTANTS.GLFW_OPENGL_CORE_PROFILE)
glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, GLFW_CONSTANTS.GLFW_TRUE)
glfw.window_hint(GLFW_CONSTANTS.GLFW_RESIZABLE, GLFW_CONSTANTS.GLFW_TRUE)
window = glfw.create_window(500, 500, "monde", None, None)
glfw.make_context_current(window)
width, height = glfw.get_framebuffer_size(window)
glViewport(0, 0, width, height)
glfw.swap_interval(0)



time_passed = glfw.get_time()

vertices = np.array(
    [
        [-0.5, -0.5, 0.0],
        [0.5, -0.5, 0.0],
        [0.0, 0.5, 0.0]
    ],
    dtype = np.float32
)


# compile object shaders, and shader programme

# vertext shader

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

sucsessP = glGetProgramiv(shaderProgram, GL_LINK_STATUS, GL_COMPILE_STATUS)
print(sucsessP)

# now that we have linked shader objects and compilled our programme, let's delete the objects..

glDeleteShader(vertexShader)
glDeleteShader(fragmentShader)


# VAO / VBO

vao = glGenVertexArrays(1)
vbo = glGenBuffers(1)

glBindVertexArray(vao)
glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

# render loop

while not glfw.window_should_close(window):
    if glfw.get_key(window,GLFW_CONSTANTS.GLFW_KEY_ESCAPE) == GLFW_CONSTANTS.GLFW_PRESS:
        glfw.set_window_should_close(window, True) 
    glfw.poll_events()
    glClearColor(0.5, 0.2, 0, 0.2)
    glClear(GL_COLOR_BUFFER_BIT)
    fps = 1 / (glfw.get_time() - time_passed)
    time_passed = glfw.get_time()
    glfw.set_window_title(window, f" fps = {str(fps)}")


    

    # do stuff here

    glfw.swap_buffers(window)

# cleaning up

glfw.terminate()
