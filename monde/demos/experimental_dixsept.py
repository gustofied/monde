import numpy as np
import OpenGL.GL as GL
from OpenGL.GL.shaders import compileShader
import glfw
import glfw.GLFW as GLFW_CONSTANTS
import ctypes
from pathlib import Path


# Let's start with a window...

glfw.init()
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, GLFW_CONSTANTS.GLFW_TRUE)
window = glfw.create_window(300, 300, "dixsept", None, None)
glfw.make_context_current(window)
glfw.swap_interval(0)


# shaders

my_dir = Path(__file__).resolve().parent
v_path = my_dir / "shaders" / "experimental_dixsept_vertex.txt"
f_path = my_dir / "shaders" / "experimental_dixsept_fragment.txt"

print(v_path.exists())
print(f_path.exists())

# read them and store them

with open(v_path, "r") as file:
    vertex_shader = file.read()

with open(f_path, "r") as file:
    fragment_shader  = file.read()    

# compile and link our proamme

vertexShader = GL.glCreateShader(GL.GL_VERTEX_SHADER)
GL.glShaderSource(vertexShader, vertex_shader)
GL.glCompileShader(vertexShader)


fragmentShader = GL.glCreateShader(GL.GL_FRAGMENT_SHADER)
GL.glShaderSource(fragmentShader, fragment_shader)
GL.glCompileShader(fragmentShader)

programmen = GL.glCreateProgram()
GL.glAttachShader(programmen, vertexShader)
GL.glAttachShader(programmen, fragmentShader)
GL.glLinkProgram(programmen)


# now let's get some data in here

arrayen = np.array([
    [-0.75, 0.75, 0],
    [-0.75, -0.75, 0],
    [0.75, -0.75, 0]
], dtype=np.float32)

# now next up from this would be..
# we need to store it in a vbo, give an attribpointer, and the a vao given to this ctx

vao = GL.glGenVertexArrays(1)
vbo = GL.glGenBuffers(1)

GL.glBindVertexArray(vao) # binding vao to our context
GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vbo)
GL.glBufferData(GL.GL_ARRAY_BUFFER, arrayen.nbytes, arrayen, GL.GL_STATIC_DRAW)
GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 12, ctypes.c_void_p(0))
GL.glEnableVertexAttribArray(0)

GL.glClearColor(0.29, 0.19, 0.29, 1)


GL.glUseProgram(programmen)



old_time = glfw.get_time()

while not glfw.window_should_close(window):
    glfw.poll_events()

    if glfw.get_key(window, GLFW_CONSTANTS.GLFW_KEY_ESCAPE) == GLFW_CONSTANTS.GLFW_PRESS:
        glfw.set_window_should_close(window, True)

    new_time = glfw.get_time()
    elapsed = new_time - old_time
    fps = 1 / elapsed

    old_time = glfw.get_time()
    glfw.set_window_title(window, F"FPS is {fps:.2f}")

    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    GL.glBindVertexArray(vao)
    GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)

    

    glfw.swap_buffers(window)


glfw.terminate()



