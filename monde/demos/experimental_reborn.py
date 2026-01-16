import numpy as np
import OpenGL.GL as GL
from OpenGL.GL.shaders import compileShader
import ctypes
import glfw
import glfw.GLFW as GLFW_CONSTANTS
from pathlib import Path

# Let's begin with window

glfw.init()
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, GLFW_CONSTANTS.GLFW_TRUE)
window = glfw.create_window(400, 400, "reborn", None, None)
glfw.make_context_current(window)
glfw.swap_interval(0)

# oki our window is done, now we have to do what's next and that's perhaps create some shaders, and compile them



my_dir = Path(__file__).resolve().parent
print(my_dir)

pathen_to_vertex = my_dir / "shaders" / "experimental_reborn_vertex.txt"
pathen_to_fragment = my_dir / "shaders" / "experimental_reborn_fragment.txt"

# now lets open and read them

with open(pathen_to_vertex, "r") as file:
    vertex_shader = file.read()

print(vertex_shader)

with open(pathen_to_fragment, "r") as file:
    fragment_vertex = file.read()

print(fragment_vertex)

# now let's compile them

myvertext = GL.glCreateShader(GL.GL_VERTEX_SHADER)
GL.glShaderSource(myvertext, vertex_shader)
GL.glCompileShader(myvertext)


myfragment = GL.glCreateShader(GL.GL_FRAGMENT_SHADER)
GL.glShaderSource(myfragment, fragment_vertex)
GL.glCompileShader(myfragment)



programme = GL.glCreateProgram()
GL.glAttachShader(programme, myvertext)
GL.glAttachShader(programme, myfragment)
GL.glLinkProgram(programme)


GL.glDeleteShader(myvertext)
GL.glDeleteShader(myfragment)


GL.glClearColor(0.32, 0.31, 0.30, 1)


# some data

arrayen = np.array([
    [ 0.75,  0.75, 0.0],
    [ 0.75, -0.75, 0.0],
    [-0.75, -0.75, 0.0]
], dtype=np.float32)

vao = GL.glGenVertexArrays(1)
vbo = GL.glGenBuffers(1)

GL.glBindVertexArray(vao)

GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vbo)
GL.glBufferData(GL.GL_ARRAY_BUFFER, arrayen.nbytes, arrayen, GL.GL_STATIC_DRAW)

GL.glVertexAttribPointer(
    0,                   
    3,                    
    GL.GL_FLOAT,    
    GL.GL_FALSE,          
    3 * 4,           
    ctypes.c_void_p(0)      
)
GL.glEnableVertexAttribArray(0)


GL.glUseProgram(programme)


old_time = glfw.get_time()

while not glfw.window_should_close(window):

    glfw.poll_events()

    dif_timer = glfw.get_time() - old_time
    fps = 1 / dif_timer
    old_time = glfw.get_time()

    if glfw.get_key(window, GLFW_CONSTANTS.GLFW_KEY_ESCAPE) == GLFW_CONSTANTS.GLFW_PRESS:
        glfw.set_window_should_close(window, True)
        
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    glfw.set_window_title(window, F"FPS is {fps:.2f}")

    GL.glBindVertexArray(vao)
    GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)
    GL.glBindVertexArray(0)

    glfw.swap_buffers(window)


glfw.terminate()




