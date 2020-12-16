cmake_minimum_required(VERSION 3.10) 

set(AOC_PROGRAM_NAME "day15")

project(${AOC_PROGRAM_NAME} LANGUAGES CXX)

add_executable(${AOC_PROGRAM_NAME}
    ${AOC_PROGRAM_NAME}.cpp
)

target_include_directories(${AOC_PROGRAM_NAME} PUBLIC 
    .
)

target_compile_options(${AOC_PROGRAM_NAME} PUBLIC /std:c++17)

