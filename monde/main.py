from monde.config import *
import monde.mesh_factory as mesh_factory 
 
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
        # self.triangle_buffers, self.triangle_vao = mesh_factory.build_triangle_mesh()
        self.triangle_vbo, self.triangle_vao = mesh_factory.build_triangle_mesh2()
        self.quad_ebo, self.quad_vbo, self.quad_vao = mesh_factory.build_quad_mesh()
        self.shader = create_shader_program("shaders/vertex.txt", "shaders/fragment.txt")
        


    def run(self):
        time_end = glfw.get_time()
        while not glfw.window_should_close(self.window):
            if glfw.get_key(self.window,GLFW_CONSTANTS.GLFW_KEY_ESCAPE) == GLFW_CONSTANTS.GLFW_PRESS:
                glfw.set_window_should_close(self.window, True) 
            glfw.poll_events()


            c = np.cos((glfw.get_time()))
            s = np.sin(np.radians(30))
            transform = np.array(
            [
            [c, -s, 0, 0],
            [s, c, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]], dtype=np.float32)


            glClear(GL_COLOR_BUFFER_BIT)
            self._set_color(1,0,1,0.5)
            fps = 1 / (glfw.get_time() - time_end)
            time_end = glfw.get_time()
            glfw.set_window_title(self.window, F" fps = {str(fps)}") 
            glUseProgram(self.shader)
            location = glGetUniformLocation(self.shader, "model")
            glUniformMatrix4fv(location, 1 , GL_TRUE, transform)
            # glBindVertexArray(self.triangle_vao)
            # glDrawArrays(GL_TRIANGLES, 0, 3)



            glBindVertexArray(self.quad_vao)
            glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_BYTE, ctypes.c_void_p(0))
            glfw.swap_buffers(self.window)
          
        self.quit()
            
                
    def quit(self):
        # glDeleteBuffers(len(self.triangle_buffers), self.triangle_buffers)
        glDeleteBuffers(3, self.triangle_vbo, self.quad_ebo, self.quad_ebo)
        glDeleteVertexArrays(2, (self.triangle_vao, self.quad_vao))
        glDeleteProgram(self.shader)
        glfw.destroy_window(self.window)
        glfw.terminate()


def main():
    print("Hello from monde!")
    my_app = App()
    my_app.run()


if __name__ == "__main__":
    main()

