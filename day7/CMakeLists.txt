cmake_minimum_required(VERSION 3.10) 

set(AOC_PROGRAM_NAME "day7")

project(${AOC_PROGRAM_NAME} LANGUAGES CXX)

add_executable(${AOC_PROGRAM_NAME}
    day7.cpp
    ../utils/utils.cpp
)

target_include_directories(${AOC_PROGRAM_NAME} PUBLIC 
    .
    ../utils
)

target_compile_options(${AOC_PROGRAM_NAME} PUBLIC /std:c++17)

