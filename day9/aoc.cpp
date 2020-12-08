#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <regex>
#include <filesystem>
#include "utils.h"


using namespace std;


void part1()
{
    cout << "Part1: " << '\n';
}


void part2()
{
    cout << "Part2: " << '\n';
}


void solution(std::istream& is)
{
    auto lines = aoc::read_lines(is);
    //auto lines = aoc::read_groups(is);

    // Place holder for creating data structure.
    for (const auto& line: lines)
    {
        cout << line << "\n\n";
    }

    part1();
    part2();
}


int main(int argc, char** argv)
{
    if (argc < 2)
    {
        std::cout << "Provide input file name\n";
        return -1;
    }
    if (!std::filesystem::is_regular_file(argv[1]))
    {
        std::cout << "Provide valid input file name\n";
        return -1;
    }

    std::ifstream is{argv[1]};
    solution(is);
}
