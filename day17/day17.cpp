#include "utils.h"


using namespace std;


constexpr uint32_t DIM  = 100;
constexpr uint32_t DIMW = 1;
constexpr uint32_t DIMZ = DIM;
constexpr uint32_t DIMY = DIM * DIM;
constexpr uint32_t DIMX = DIM * DIM * DIM;
constexpr uint32_t OFF  = DIM / 2;


uint32_t part2(const vector<string>& data, uint32_t cycles)
{
    set<uint32_t> alive;
    for (uint32_t y = 0; y < data.size(); ++y)
    {
        const auto& row = data[y];
        for (uint32_t x = 0; x < row.size(); ++x)
        {
            if (row[x] == '#')
                alive.insert(DIMX*(x+OFF) + DIMY*(y+OFF) + DIMZ*OFF + DIMW*OFF);            
        }
    }

    for (uint32_t s = 0; s < cycles; ++s)
    {
        map<uint32_t, uint32_t> neighbours;
        for (auto c: alive)
        {
            uint32_t x = (c / DIMX) % DIM;
            uint32_t y = (c / DIMY) % DIM;
            uint32_t z = (c / DIMZ) % DIM;
            uint32_t w = (c / DIMW) % DIM;

            for (uint32_t i = x-1; i <= (x+1); ++i)
            {
                for (uint32_t j = y-1; j <= (y+1); ++j)
                {
                    for (uint32_t k = z-1; k <= (z+1); ++k)
                    {
                        for (uint32_t l = w-1; l <= (w+1); ++l)
                        {
                            if ((i == x) && (j == y) && (k == z) && (l == w))
                                continue;

                            uint32_t p = DIMX*i + DIMY*j + DIMZ*k + DIMW*l;   
                            map<uint32_t, uint32_t>::iterator it = neighbours.find(p);
                            if (it == neighbours.end())         
                                neighbours[p] = 1;
                            else
                                neighbours[p] += 1;
                        }
                    }
                }
            }
        }                

        set<uint32_t> alive2;
        for (auto [k, v]: neighbours)
        {
            if (alive.find(k) != alive.end())
            {
                if (v == 2 || v == 3)
                    alive2.insert(k); 
            }
            else
            {
                if (v == 3)
                    alive2.insert(k); 
            }
        }

        alive = alive2;
    }

    return static_cast<uint32_t>(alive.size());
}


template <typename T>
void run(T t)
{
    auto start = chrono::system_clock::now();

    t();

    chrono::duration<double> diff = chrono::system_clock::now() - start;
    cout << (diff.count() * 1000) << "ms\n";
}


int main()
{
    run([]
    {
        auto data = aoc::read_lines("day17-test.txt");
        cout << "Part2: " << part2(data, 6) << '\n';
    });

    run([]
    {
        auto data = aoc::read_lines("day17-input.txt");
        cout << "Part2: " << part2(data, 6) << '\n';
    });
}

