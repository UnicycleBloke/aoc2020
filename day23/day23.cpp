#include <iostream>
#include <array>
#include <cstdint>
#include <iomanip>


using namespace std;


template <uint32_t SIZE>
void run(const char* input, uint32_t LOOPS, bool is_part1)
{
    static array<uint32_t, SIZE + 1> cups;

    uint32_t first = input[0] - '0';
    uint32_t cup = first;
    for (uint32_t i = 1; i < 9; ++i)
    {
        cups[cup] = input[i] - '0';
        cup = cups[cup];
    }
    for (uint32_t i = 10; i <= SIZE; ++i)
    {
        cups[cup] = i;
        cup = cups[cup];
    }
    cups[cup] = first;

    auto curr = first;
    for (uint32_t loop = 0; loop < LOOPS; ++loop)
    {
        auto move1 = cups[curr]; 
        auto move2 = cups[move1]; 
        auto move3 = cups[move2]; 
        auto dest  = curr - 1;

        while ((dest > 0) && ((move1 == dest) || (move2 == dest) || (move3 == dest))) 
            --dest;
        if (dest == 0)
        {
            dest = SIZE;
            while ((dest > 0) && ((move1 == dest) || (move2 == dest) || (move3 == dest))) 
                --dest;
        }

        auto temp   = cups[dest];        
        cups[dest]  = move1;
        cups[curr]  = cups[move3];
        cups[move3] = temp;

        curr = cups[curr];
    }

    if (is_part1)
    {
        cout << "Part 1: ";

        auto c = cups[1]; 
        for (auto i = 1; i < 9; ++i)
        {
            cout << c;
            c = cups[c];
        }
        cout << "\n";
    }
    else
    {
        auto result1 = cups[1]; 
        auto result2 = cups[result1];
        cout << "Part 2: ";
        cout << result1 << " " << result2 << " " << (uint64_t(result1) * uint64_t(result2)) << '\n';  
    }
}


int main()
{
    const char* crab_input = "389125467"; 
    const char* alan_input = "219748365";
    // Part 1
    constexpr uint32_t SIZE1  =   9; 
    constexpr uint32_t LOOPS1 = 100;
    // Part 2
    constexpr uint32_t SIZE2  =  1'000'000; 
    constexpr uint32_t LOOPS2 = 10'000'000;

    run<SIZE1>(crab_input, LOOPS1, true);
    run<SIZE2>(crab_input, LOOPS2, false);
    
    run<SIZE1>(alan_input, LOOPS1, true);
    run<SIZE2>(alan_input, LOOPS2, false);
}
