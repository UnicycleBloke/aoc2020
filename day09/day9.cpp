#include "utils.h"


using namespace std;
using Int = unsigned long long;


bool sum_of_two(const vector<Int>& nums, std::size_t start, std::size_t end, Int value)
{
    for (std::size_t i = start; i < end; ++i)
        for (std::size_t j = i + 1; j < end; ++j)
            if ((nums[i] + nums[j]) == value) return true;
    return false;
}


Int part1(const vector<Int>& nums, std::size_t size)
{
    for (std::size_t i = size; i < nums.size(); ++i)
    {        
        if (!sum_of_two(nums, i - size, i, nums[i]))
        {
            return nums[i];
        }
    }
    return 0;    
}


Int part2(const vector<Int>& nums, Int value)
{
    for (std::size_t i = 0; i < nums.size(); ++i)
    {
        for (std::size_t j = i + 1; j < nums.size(); ++j)
        {
            auto s   = nums.begin() + i;
            auto e   = nums.begin() + j;
            auto acc = std::accumulate(s, e, Int{});
            if (acc == value)
                return *std::min_element(s, e) + *std::max_element(s, e);
            if (acc > value)
                break;
        }
    }
    return 0;
}


void solution(const char* file, std::size_t size)
{
    cout << "Input: " << file << '\n';
    std::ifstream is{file};
    auto nums  = aoc::read_ints<Int>(is);
    
    auto p1 = part1(nums, size);
    cout << "Part1: " << p1 << '\n';

    auto p2 = part2(nums, p1);
    cout << "Part2: " << p2 << '\n';
}


int main(int argc, char** argv)
{
    solution("day9-test.txt", 5);
    solution("day9-input.txt", 25);
}
