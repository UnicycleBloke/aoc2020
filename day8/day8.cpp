#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <regex>
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


int main(int argc, char** argv)
{
    if (argc < 2)
    {
        std::cout << "Provide input file name\n";
        return -1;
    }

    std::ifstream is{argv[1]};
    //auto lines = aoc::read_lines(is);
    auto lines = aoc::read_groups(is);

    for (const auto& line: lines)
    {
        cout << line << "\n\n";
    }

    // map<string, vector<pair<int, string>>> data;

    // for (auto line: lines)
    // {
    //     line = aoc::replace(line, "bags", ":");
    //     line = aoc::replace(line, "bag", ":");
    //     line = aoc::replace(line, "contains", ":");
    //     line = aoc::replace(line, "contain", ":");
    //     line = aoc::replace(line, ",", ":");
    //     line = aoc::replace(line, ".", ":");

    //     auto spl = aoc::split(line, ":", false);

    //     vector<pair<int, string>> contains;
    //     for (int i = 1; i < spl.size(); ++i)
    //     {
    //         std::smatch sm;
    //         if (std::regex_match(spl[i], sm, std::regex{ R"((\d+)\s+(.+))" }))
    //         {
    //             contains.push_back(std::make_pair<int, string>(std::stoi(sm[1]), sm[2]));
    //         }
    //     }

    //     data[spl[0]] = contains;
    // }

    part1();
    part2();
}
