import glfw
import numpy as np
import glfw.GLFW as GLFW_CONSTANTS
from OpenGL.GL import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class App:
    def __init__(self):
        glfw.init()
        
        glfw.window_hint(
        GLFW_CONSTANTS.GLFW_OPENGL_PROFILE, 
       GLFW_CONSTANTS.GLFW_OPENGL_CORE_PROFILE)
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, 3)

        glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, GLFW_CONSTANTS.GLFW_TRUE)
        self.window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Monde", None, None)
        glfw.make_context_current(self.window)
        glClearColor(4.1,0.2,1.4,1.0)


    def run(self):
        while not glfw.window_should_close(self.window):
            
            glfw.poll_events()

            glClear(GL_COLOR_BUFFER_BIT)
            glfw.swap_buffers(self.window)

    def quit(self):
        glfw.destroy_window(self.window)
        glfw.terminate()


def main():
    print("Hello from monde!")
    my_app = App()
    my_app.run()
    my_app.quit()


if __name__ == "__main__":
    main()
