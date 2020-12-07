#include <vector>
#include <string>
#include <iostream>


namespace aoc {


void ltrim(std::string& s);
void rtrim(std::string& s);
void trim(std::string& s);
std::string replace(std::string source, const std::string& search, const std::string& replace);
std::vector<std::string> split(std::string source, std::string delim, bool allow_blanks);
std::vector<std::string> read_lines(std::istream& is, bool allow_blanks);


} // namespace aoc {


