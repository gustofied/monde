import glfw
import numpy as np
import glfw.GLFW as GLFW_CONSTANTS
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import time



SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480



def create_shader_program(vertex_filepath: str, fragment_filepath: str) -> int:

    vertex_module = create_shader_module(vertex_filepath, GL_VERTEX_SHADER)
    fragment_module = create_shader_module(fragment_filepath, GL_FRAGMENT_SHADER)

    shader = compileProgram(vertex_module, fragment_module)

    glDeleteShader(vertex_module)
    glDeleteShader(fragment_module)

    return shader

def create_shader_module(filepath: str, module_type) -> int:

    source_code = ""
    with open(filepath, "r") as file:
        source_code = file.readlines()

    return compileShader(source_code, module_type)
    
class App:



    def _set_color(self, r,g,b,a):
        glClearColor(r, g, b, a)

    def _set_opengl_version(self, major:int, minor:int):
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, major)
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, minor)


    def __init__(self):

        self.initialize_glfw()
        self.initialize_opengl()
        
    
    
    def initialize_glfw(self) -> None:    
            glfw.init()
            glfw.window_hint(
            GLFW_CONSTANTS.GLFW_OPENGL_PROFILE, 
        GLFW_CONSTANTS.GLFW_OPENGL_CORE_PROFILE)
            self._set_opengl_version(3,3)
            glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, GLFW_CONSTANTS.GLFW_TRUE)
            self.window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Monde", None, None)
            glfw.make_context_current(self.window) 
    
    
    def initialize_opengl(self) -> None:
        self._set_color(0.1,0.2,0.7,0.5)
        self.VAO = glGenVertexArrays(1)
        self.shader = create_shader_program("shaders/vertex.txt", "shaders/fragment.txt")
        


    def run(self):
        time_end = glfw.get_time()
        while not glfw.window_should_close(self.window):
            if glfw.get_key(self.window,GLFW_CONSTANTS.GLFW_KEY_ESCAPE) == GLFW_CONSTANTS.GLFW_PRESS:
                glfw.set_window_should_close(self.window, True) 
            glfw.poll_events()
            glClear(GL_COLOR_BUFFER_BIT)
            self._set_color(1,0,1,0.5)
            fps = 1 / (glfw.get_time() - time_end)
            time_end = glfw.get_time()
            glfw.set_window_title(self.window, F" fps = {str(fps)}") 
            glUseProgram(self.shader)
            glBindVertexArray(self.VAO)
            glDrawArrays(GL_TRIANGLES, 0, 3)
            glfw.swap_buffers(self.window)
          
        self.quit()
            
                
    def quit(self):
        glDeleteVertexArrays(1, (self.VAO,))
        glDeleteProgram(self.shader)
        glfw.destroy_window(self.window)
        glfw.terminate()


def main():
    print("Hello from monde!")
    my_app = App()
    my_app.run()


if __name__ == "__main__":
    main()

