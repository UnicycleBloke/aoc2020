#include <iostream>
#include <vector>
#include <chrono>


using namespace std;


int run(const vector<uint32_t>& v, uint32_t count)
{
    auto start = chrono::system_clock::now();

    // Don't put the last item into mem. -1 means the 
    // index hasn't been seen yet.
    vector<uint32_t> mem(count, -1);
    for (uint32_t i = 0; i < v.size() - 1; ++i)
    {
        mem[v[i]] = i;
    }

    // The last item is not yet in mem, so we can check if 
    // it is its first appearance.
    uint32_t idx = static_cast<uint32_t>(v.size());
    uint32_t val = v[idx - 1];

    while (idx < count)
    {
        uint32_t next = (mem[val] == -1) ? 0 : idx - mem[val] - 1;
        mem[val] = idx - 1;
        val = next;
        ++idx;
    }

    auto end = chrono::system_clock::now();
    chrono::duration<double> diff = end - start;
    cout << (diff.count() * 1000) << "ms\n";

    return val;    
}


int main()
{
    cout << "Part1: " << run({19, 20, 14, 0, 9, 1}, 2020) << '\n';
    cout << "Part2: " << run({19, 20, 14, 0, 9, 1}, 30'000'000) << '\n';
}