import glfw
from OpenGL.GL import *
import glfw.GLFW as GLFW_CONSTANTS
from OpenGL.GL.shaders import compileShader
import numpy as np
import ctypes
from pathlib import Path
import math
# Paths

dir = Path(__file__).resolve().parent
vertex_shader_path = dir / "shaders" / "experimental_square_vertex.txt"
fragment_shader_path = dir / "shaders" / "experimental_square_fragment.txt"


glfw.init()
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, 3 )
glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, 3 )
glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, GLFW_CONSTANTS.GLFW_TRUE)
glfw.window_hint(GLFW_CONSTANTS.GLFW_RESIZABLE, GLFW_CONSTANTS.GLFW_TRUE)
window = glfw.create_window(400,400, "testing", None, None)
glfw.make_context_current(window)
glfw.swap_interval(0)
glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)



# hollow circle 

r_0 = 0.25
N_0 = 12

angles_0 = np.linspace(0, 2*np.pi, N_0, endpoint=False).astype(np.float32)
x_0_coordinates = r_0 * np.cos(angles_0) + 0.25
y_0_coordinates = r_0 * np.sin(angles_0) + 0.25
z_0_coordinates = np.zeros_like(x_0_coordinates)

vertices_0 = np.stack((x_0_coordinates, y_0_coordinates, z_0_coordinates), axis= 1).astype(np.float32)

# triangle, repeat circle

r_1 = 0.5
N_1 = 100

angles_1 = np.linspace(0, 2*np.pi, N_1, endpoint=False).astype(np.float32)

x_1_coordinates = r_1 * np.cos(angles_1) - 0.50
y_1_coordinates = r_1 * np.sin(angles_1) - 0.50
z_1_coordinates = np.zeros_like(x_1_coordinates)
origo_1 = np.array([-0.5, -0.5, 0]).astype(np.float32)

tri_vertices_1 = np.stack([x_1_coordinates, y_1_coordinates, z_1_coordinates], axis=1)

triangles_1 = np.stack(
    (tri_vertices_1, np.roll(tri_vertices_1, -1, axis=0), np.broadcast_to(origo_1, tri_vertices_1.shape)),
    axis=1
).astype(np.float32) 

vertices_1 = triangles_1.reshape(-1, 3)

# print(vertices_1)


# Triangle Fan

r_2 = 0.15
N_2 = 64

angles_2 = np.linspace(0, 2*np.pi, N_2, endpoint=False).astype(np.float32)
x_2_coordinates = r_2 * np.cos(angles_2) - 0.50
y_2_coordinates = r_2 * np.sin(angles_2) + 0.25
z_2_coordinates = np.zeros_like(x_2_coordinates)
origo_2 = np.array([-0.5, 0.25, 0]).astype(np.float32)


vertices_2_gen = np.stack((x_2_coordinates, y_2_coordinates, z_2_coordinates), axis= 1).astype(np.float32)
vertices_2 = np.vstack((origo_2, vertices_2_gen)).astype(np.float32)
print(vertices_2[:10])
# this is the ammount of attributes OpengGL can give on this mac?


# Indexed Fan

r_3 = 0.40
N_3 = 500

angles_3 = np.linspace(0, 2*np.pi, N_3, endpoint=False).astype(np.float32)
x_3_coordinates = r_3 * np.cos(angles_3) + 0.50
y_3_coordinates = r_3 * np.sin(angles_3) - 0.25
z_3_coordinates = np.zeros_like(x_3_coordinates)
origo_3 = np.array([0.5, -0.25, 0]).astype(np.float32)


vertices_3_gen = np.stack((x_3_coordinates, y_3_coordinates, z_3_coordinates), axis= 1).astype(np.float32)
vertices_3 = np.vstack((origo_3, vertices_3_gen)).astype(np.float32)

print(vertices_3[0:1])

tri_list = [[0, i, i+1] for i in range(1, N_3)] 
tri_list.append([0, N_3, 1])
indices = np.array(tri_list, dtype=np.uint32).reshape(-1) 
print(indices)


nr_attributes = glGetIntegerv(GL_MAX_VERTEX_ATTRIBS)
print(nr_attributes)


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

successP = glGetProgramiv(shaderProgram, GL_LINK_STATUS)
print(successP)

# now that we have linked shader objects and compilled our programme, let's delete the objects..

glDeleteShader(vertexShader)
glDeleteShader(fragmentShader)


# VAO / VBO

# hollow circle

vao_0 = glGenVertexArrays(1)
vbo_0 = glGenBuffers(1)

glBindVertexArray(vao_0)

glBindBuffer(GL_ARRAY_BUFFER, vbo_0)
glBufferData(GL_ARRAY_BUFFER, vertices_0.nbytes, vertices_0, GL_STATIC_DRAW)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))
glEnableVertexAttribArray(0)

# triagle circle

vao_1 = glGenVertexArrays(1)
vbo_1 = glGenBuffers(1)

glBindVertexArray(vao_1)

glBindBuffer(GL_ARRAY_BUFFER, vbo_1)
glBufferData(GL_ARRAY_BUFFER, vertices_1.nbytes, vertices_1, GL_STATIC_DRAW)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))
glEnableVertexAttribArray(0)



# triagle fan

vao_2 = glGenVertexArrays(1)
vbo_2 = glGenBuffers(1)

glBindVertexArray(vao_2)

glBindBuffer(GL_ARRAY_BUFFER, vbo_2)
glBufferData(GL_ARRAY_BUFFER, vertices_2.nbytes, vertices_2, GL_STATIC_DRAW)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))
glEnableVertexAttribArray(0)


# indexed triangle

vao_3 = glGenVertexArrays(1)
vbo_3 = glGenBuffers(1)
ebo_3 = glGenBuffers(1)

glBindVertexArray(vao_3)

glBindBuffer(GL_ARRAY_BUFFER, vbo_3)
glBufferData(GL_ARRAY_BUFFER, vertices_3.nbytes, vertices_3, GL_STATIC_DRAW)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo_3)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))
glEnableVertexAttribArray(0)

# render loop

while not glfw.window_should_close(window):
    if glfw.get_key(window,GLFW_CONSTANTS.GLFW_KEY_ESCAPE) == GLFW_CONSTANTS.GLFW_PRESS:
        glfw.set_window_should_close(window, True) 
    glfw.poll_events()
    glClearColor(0.5, 0.2, 0, 0.2)
    glClear(GL_COLOR_BUFFER_BIT)

    time_passed = glfw.get_time()
    glfw.set_window_title(window, f"Experimental")

    glUseProgram(shaderProgram)
    time = glfw.get_time()
    glUniform1f(glGetUniformLocation(shaderProgram, "u_time"), time)
    glBindVertexArray(vao_0)
    glDrawArrays(GL_LINE_STRIP, 0, N_0) # hollow circle # GL_LINE_LOOP instead too
    glBindVertexArray(vao_1)
    glDrawArrays(GL_TRIANGLES, 0, vertices_1.shape[0]- 10) # triangle  3*N_1
    glBindVertexArray(vao_2)
    glDrawArrays(GL_TRIANGLE_FAN, 0, vertices_2.shape[0]) # triangle fan
    glBindVertexArray(vao_3)
    glDrawElements(GL_TRIANGLES, indices.size, GL_UNSIGNED_INT, ctypes.c_void_p(0))
    
    # do stuff here

    glfw.swap_buffers(window)

# cleaning up

glfw.terminate()
