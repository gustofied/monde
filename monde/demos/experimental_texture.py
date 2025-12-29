import numpy as np
import glfw
import glfw.GLFW as GLFW_CONSTANTS
from OpenGL import GL
from OpenGL.GL.shaders import compileShader
import ctypes
from pathlib import Path
import math



# paths

dir: Path = Path(__file__).resolve().parent
vertex_shader_path = dir / "shaders" / "experimental_texture_vertex.txt"
fragment_shader_path = dir / "shaders" / "experimental_texture_fragment.txt"

print(vertex_shader_path.exists())
print(fragment_shader_path.exists())


# window

glfw.init()
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, 3 )
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, 3 )
glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, GLFW_CONSTANTS.GLFW_TRUE) # could always just say 1..
glfw.window_hint(GLFW_CONSTANTS.GLFW_RESIZABLE, GLFW_CONSTANTS.GLFW_TRUE)
window = glfw.create_window(400, 400, "TexTure", None, None)
glfw.make_context_current(window)
glfw.swap_interval(0)
GL.glPolygonMode(GL.GL_FRONT_AND_BACK, GL.GL_LINE)



# shaders and sader progamme.

with open(vertex_shader_path, "r") as file:
    shaderV = file.read()

with open(fragment_shader_path, "r") as file:
    shaderF = file.read()


vertexShader = GL.glCreateShader(GL.GL_VERTEX_SHADER)
GL.glShaderSource(vertexShader, shaderV)
GL.glCompileShader(vertexShader)


fragmentShader = GL.glCreateShader(GL.GL_FRAGMENT_SHADER)
GL.glShaderSource(fragmentShader, shaderF)
GL.glCompileShader(fragmentShader)

shadeProgramme = GL.glCreateProgram()
GL.glAttachShader(shadeProgramme, vertexShader)
GL.glAttachShader(shadeProgramme, fragmentShader)
GL.glLinkProgram(shadeProgramme)

GL.glDeleteShader(vertexShader)
GL.glDeleteShader(fragmentShader)


GL.glClearColor(0.0, 0.75, 0.75, 1.0)

# since we have one programme  we put it outside our render loop

GL.glUseProgram(shadeProgramme)

# some data on our CPU

vertices = np.array([
    [0.5, -0.75, 0.0],
    [-0.5, -0.75, 0],
    [-0.5, 0.75, 0]
], dtype=np.float32
)

print(vertices)


# VAO, VBO

vao = GL.glGenVertexArrays(1)
vbo = GL.glGenBuffers(1)

GL.glBindVertexArray(vao)

GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vbo)
GL.glBufferData(GL.GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL.GL_STATIC_DRAW)

GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 12, ctypes.c_void_p(0))
GL.glEnableVertexAttribArray(0)


# render loop


previous_time = glfw.get_time()

while not glfw.window_should_close(window):


    frames = 1 / (glfw.get_time() - previous_time) 
    glfw.set_window_title(window,title=f"FPS {frames:.2f}")
    previous_time = glfw.get_time()
    glfw.poll_events()


    if glfw.get_key(window,GLFW_CONSTANTS.GLFW_KEY_ESCAPE) == GLFW_CONSTANTS.GLFW_PRESS:
        glfw.set_window_should_close(window, True) 
    
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    GL.glBindVertexArray(vao)
    GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)



    # Render here
    # Draw

    # Swap at end

    time = glfw.get_time()

    glfw.swap_buffers(window)



