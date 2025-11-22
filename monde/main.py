import glfw
import numpy as np
import glfw.GLFW as GLFW_CONSTANTS
from OpenGL.GL import *
import time



SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class App:

    def _set_color(self, r,g,b,a):
        glClearColor(r, g, b, a)

    def _set_opengl_version(self, major:int, minor:int):
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, major)
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, minor)


    def __init__(self):
        glfw.init()
        glfw.window_hint(
        GLFW_CONSTANTS.GLFW_OPENGL_PROFILE, 
       GLFW_CONSTANTS.GLFW_OPENGL_CORE_PROFILE)
        self._set_opengl_version(3,3)
        glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, GLFW_CONSTANTS.GLFW_TRUE)
        self.window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Monde", None, None)
        glfw.make_context_current(self.window) 
        self._set_color(0.1,0.2,0.7,0.5)
        


    def run(self):
        time_end = glfw.get_time()
        while not glfw.window_should_close(self.window):
            if glfw.get_key(self.window,GLFW_CONSTANTS.GLFW_KEY_ESCAPE) == GLFW_CONSTANTS.GLFW_PRESS:
                glfw.set_window_should_close(self.window, True) 
            glfw.poll_events()
            glClear(GL_COLOR_BUFFER_BIT)
            glfw.swap_buffers(self.window)
            self._set_color(1,0,1,0.5)
            fps = 1 / (glfw.get_time() - time_end)
            time_end = glfw.get_time()
            glfw.set_window_title(self.window, F" fps = {str(fps)}") 
        self.quit()
            
                
    def quit(self):
        glfw.destroy_window(self.window)
        glfw.terminate()


def main():
    print("Hello from monde!")
    my_app = App()
    my_app.run()


if __name__ == "__main__":
    main()

        