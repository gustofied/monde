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


GL.glClearColor(0.32, 0.31, 0.30, 1)


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

    glfw.swap_buffers(window)


glfw.terminate()




