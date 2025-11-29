import glfw
from OpenGL.GL import *
import glfw.GLFW as GLFW_CONSTANTS
from OpenGL.GL.shaders import compileShader
import numpy as np
import ctypes



# glfw 

glfw.init()
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_PROFILE, GLFW_CONSTANTS.GLFW_OPENGL_CORE_PROFILE)
glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, GLFW_CONSTANTS.GLFW_TRUE)
glfw.window_hint(GLFW_CONSTANTS.GLFW_RESIZABLE, GL_FALSE)
window = glfw.create_window(500, 500, "monde", None, None)
glfw.make_context_current(window)
width, height = glfw.get_framebuffer_size(window)
glViewport(0, 0, width, height)
glfw.swap_interval(0)

# render loop

time_passed = glfw.get_time()
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
