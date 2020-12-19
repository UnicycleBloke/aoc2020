// aoc4.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <sstream>
#include <fstream>
#include <regex>


bool has_pid(const std::string cred)
{
    std::smatch sm;
    //return std::regex_match(cred, sm, std::regex{ R"(pid:.*)" });
    return std::regex_search(cred, sm, std::regex{ R"(pid:)" });
}

bool has_pid(const std::string cred, bool part1)
{
    std::smatch sm;
    return std::regex_search(cred, sm, std::regex{ part1 ? R"(pid:)" : R"(pid:(\d{9}))" });
}


bool valid_pid(const std::string cred)
{
    std::smatch sm;
    return std::regex_match(cred, sm, std::regex{ R"(pid:(\d{9}))" });
}


bool valid_byr(const std::string& cred)
{
    std::smatch sm;
    if (std::regex_match(cred, sm, std::regex{ R"(byr:(\d{4}))" }))
    {
        auto year = std::stoi(sm[1]);
        return (year >= 1920) && (year <= 2002);
    }
    return false;
}


std::vector<std::string> split(const std::string& s, char delimiter)
{
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream is(s);
    while (std::getline(is, token, delimiter))
    {
        tokens.push_back(token);
    }
    return tokens;
}


static inline void ltrim(std::string& s) 
{
    s.erase(s.begin(), std::find_if(s.begin(), s.end(), [](unsigned char ch) 
    {
        return !std::isspace(ch);
    }));
}
static inline void rtrim(std::string& s) 
{
    s.erase(std::find_if(s.rbegin(), s.rend(), [](unsigned char ch) 
    {
        return !std::isspace(ch);
    }).base(), s.end());
}
static inline void trim(std::string& s) 
{
    ltrim(s);
    rtrim(s);
}


int main2(int argc, char** argv)
{
    if (argc > 1)
    {
        std::ifstream is{argv[1]};

        std::string cred;
        while (!is.eof())
        {
            std::string line;
            std::getline(is, line);
            trim(line);
            if (line.size() > 0)
            {
                cred = cred + ' ' + line;
            }
            else
            {
                auto items = split(cred, ' ');
                for (const auto& item : items)
                    std::cout << "'" << item << "', ";
                std::cout << '\n';
                cred.clear();

                for (const auto& item : items)
                {
                    if (has_pid(item))
                        std::cout << "Has pid" << '\n';
                    if (valid_pid(item))
                        std::cout << "Valid pid" << '\n';
                    if (valid_byr(item))
                        std::cout << "Valid byr" << '\n';
                }
            }
        }
    }

    return 0;
}
