import glfw
import glfw.GLFW as GLFW_CONSTANTS
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import ctypes
from pathlib import Path

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

BASE_DIR = Path(__file__).resolve().parent


data_type_vertex = np.dtype({
    "names": ["x","y", "z", "color"],
    "formats":[np.float32, np.float32, np.float32, np.uint32],
    "offsets": [0, 4, 8, 12],
    "itemsize": 16
})

def create_shader_program(vertex_filepath: str, fragment_filepath: str) -> int:

    vertex_module = create_shader_module(vertex_filepath, GL_VERTEX_SHADER)
    fragment_module = create_shader_module(fragment_filepath, GL_FRAGMENT_SHADER)

    shader = compileProgram(vertex_module, fragment_module)

    glDeleteShader(vertex_module)
    glDeleteShader(fragment_module)

    return shader

def create_shader_module(filepath: str, module_type) -> int:

    full_path = BASE_DIR / filepath

    source_code = ""
    with full_path.open("r") as file:
        source_code = file.readlines()

    return compileShader(source_code, module_type)