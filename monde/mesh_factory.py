from monde.config import *

def build_triangle_mesh()-> tuple[tuple[int, int], int]:                                            

    position_data = np.array(
    [-0.25, -0.75, 0.0,  
         0.75, -0.75, 0.0,  
         0.0,   0.75, 0.0], dtype=np.float32)

    color_data = np.array(
        [0, 1, 2], dtype=np.uint32)
    
    
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    position_buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, position_buffer)
    glBufferData(GL_ARRAY_BUFFER, position_data.nbytes, position_data, GL_STATIC_DRAW)
    attribute_index = 0
    size = 3
    stride = 12
    offset = 0
    glVertexAttribPointer(attribute_index, size, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(offset))
    glEnableVertexAttribArray(attribute_index)

    color_buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, color_buffer)
    glBufferData(GL_ARRAY_BUFFER, color_data.nbytes, color_data, GL_STATIC_DRAW)
    attribute_index = 1
    size = 1
    stride = 4
    offset = 0
    glVertexAttribIPointer(attribute_index, size, GL_UNSIGNED_INT, stride, ctypes.c_void_p(offset))
    glEnableVertexAttribArray(attribute_index)

    return ((position_buffer, color_buffer), vao)

def build_triangle_mesh2()-> tuple[int, int]:                                            

    vertex_data = np.zeros(3, dtype = data_type_vertex)
    vertex_data[0] = (-0.75, -0.75, 0.0, 0)
    vertex_data[1] = (0.75, -0.75, 0.0, 1)
    vertex_data[2] = (0.0, 0.75, 0.0, 2)
    
    
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    vbo= glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertex_data.nbytes, vertex_data, GL_STATIC_DRAW)
    attribute_index = 0
    size = 3
    stride = data_type_vertex.itemsize
    offset = 0
    glVertexAttribPointer(attribute_index, size, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(offset))
    glEnableVertexAttribArray(attribute_index)
    offset += 12


    attribute_index = 1
    size = 1
    glVertexAttribIPointer(attribute_index, size, GL_UNSIGNED_INT, stride, ctypes.c_void_p(offset))
    glEnableVertexAttribArray(attribute_index)

    return (vbo, vao)