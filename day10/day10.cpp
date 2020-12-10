#include "utils.h"


using namespace std;
using Int = unsigned long long;


Int part1(const vector<Int>& nums)
{
    return 0;    
}


Int part2(const vector<Int>& nums)
{
    return 0;
}


void solution(const char* file)
{
    cout << "Input: " << file << '\n';
    std::ifstream is{file};
    auto nums  = aoc::read_ints<Int>(is);
    
    auto p1 = part1(nums);
    cout << "Part1: " << p1 << '\n';

    auto p2 = part2(nums);
    cout << "Part2: " << p2 << '\n';
}


int main(int argc, char** argv)
{
    solution("day10-test.txt");
    solution("day10-test2.txt");
    solution("day10-input.txt");
}
