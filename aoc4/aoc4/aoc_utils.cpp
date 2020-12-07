#include "aoc_utils.h"


namespace aoc {


void ltrim(std::string& s)
{
    s.erase(s.begin(), std::find_if(s.begin(), s.end(),
        [](unsigned char ch) { return !std::isspace(ch); }));
}


void rtrim(std::string& s)
{
    s.erase(std::find_if(s.rbegin(), s.rend(),
        [](unsigned char ch) { return !std::isspace(ch); }).base(), s.end());
}


void trim(std::string& s)
{
    ltrim(s);
    rtrim(s);
}


std::string replace(std::string source, const std::string& search, const std::string& replace)
{
    size_t pos = 0;
    while ((pos = source.find(search, pos)) != std::string::npos)
    {
        source.replace(pos, search.length(), replace);
        pos += replace.length();
    }
    return source;
}


std::vector<std::string> split(std::string source, std::string delim, bool allow_blanks)
{
    std::vector<std::string> result;

    auto start = 0U;
    auto end = source.find(delim);
    while (end != std::string::npos)
    {
        auto sub = source.substr(start, end - start);
        trim(sub);
        if (allow_blanks || (sub.size() > 0))
            result.push_back(sub);

        start = end + delim.length();
        end   = source.find(delim, start);
    }

    return result;
}


std::vector<std::string> read_lines(std::istream& is, bool allow_blanks)
{
    std::vector<std::string> lines;

    while (!is.eof())
    {
        std::string line;
        std::getline(is, line);
        trim(line);
        if (allow_blanks || (line.size() > 0))
            lines.push_back(line);
    }

    return lines;
}


} // namespace aoc {
