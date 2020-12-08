#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <regex>
#include "utils.h"


using namespace std;


bool part1_impl(map<string, vector<pair<int, string>>>& rules, const string& colour)
{
    const auto& rule = rules[colour];
    for (const auto& pair : rule)
    {
        if (pair.second == "shiny gold")
            return true;
        else if (part1_impl(rules, pair.second))
            return true;
    }
    return false;
}


void part1(map<string, vector<pair<int, string>>>& rules)
{
    int count = 0;
    for (const auto& rule: rules)
    {
        count += part1_impl(rules, rule.first);
    }
    cout << "Part1: " << count << '\n';
}


int part2_impl(map<string, vector<pair<int, string>>>& rules, const string& colour)
{
    int sum = 0;
    const auto& rule = rules[colour];
    for (const auto& pair : rule)
    {
        sum += pair.first * (1 + part2_impl(rules, pair.second));
    }
    return sum;
}


void part2(map<string, vector<pair<int, string>>>& rules)
{
    cout << "Part2: " << part2_impl(rules, "shiny gold") << '\n';
}


int main(int argc, char** argv)
{
    if (argc < 2)
    {
        std::cout << "Provide input file name\n";
        return -1;
    }

    map<string, vector<pair<int, string>>> data;

    std::ifstream is{argv[1]};
    auto lines = aoc::read_lines(is, false);

    for (auto line: lines)
    {
        line = aoc::replace(line, "bags", ":");
        line = aoc::replace(line, "bag", ":");
        line = aoc::replace(line, "contains", ":");
        line = aoc::replace(line, "contain", ":");
        line = aoc::replace(line, ",", ":");
        line = aoc::replace(line, ".", ":");

        auto spl = aoc::split(line, ":", false);

        vector<pair<int, string>> contains;
        for (int i = 1; i < spl.size(); ++i)
        {
            std::smatch sm;
            if (std::regex_match(spl[i], sm, std::regex{ R"((\d+)\s+(.+))" }))
            {
                contains.push_back(std::make_pair<int, string>(std::stoi(sm[1]), sm[2]));
            }
        }

        data[spl[0]] = contains;
    }

    part1(data);
    part2(data);
}
