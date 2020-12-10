#include <iostream>
#include <fstream>
#include <sstream>

#include <vector>
#include <map>
#include <set>
#include <numeric>
#include <algorithm>

#include <string>
#include <regex>
#include <filesystem>
#include <type_traits>


namespace aoc {


void ltrim(std::string& s);
void rtrim(std::string& s);
void trim(std::string& s);

std::string replace(std::string source, const std::string& search, const std::string& replace);
std::vector<std::string> split(std::string source, std::string delim, bool allow_blanks);

std::vector<std::string> read_lines(std::istream& is, bool allow_blanks = false);
std::vector<std::string> read_groups(std::istream& is);


template <typename T>
std::vector<T> read_ints(std::istream& is)
{
    std::vector<T> ints;

    while (!is.eof())
    {
        std::string line;
        std::getline(is, line);
        trim(line);
        if (line.size() > 0)
        {
            if constexpr (std::is_same_v<T, unsigned long long>)
            {
                ints.push_back(stoull(line));
            }
            else
            {
                throw std::runtime_error("Invalid integer type");
            }
        }
    }

    return ints;
}


} // namespace aoc {


