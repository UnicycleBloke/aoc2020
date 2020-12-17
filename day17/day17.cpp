#include <vector>
#include <string>
#include <set>
#include <map>
#include <iostream>


using namespace std;

constexpr int DIM  = 100;
constexpr int DIMW = 1;
constexpr int DIMZ = DIM;
constexpr int DIMY = DIM * DIM;
constexpr int DIMX = DIM * DIM * DIM;
constexpr int OFF  = DIM / 2;

int part2b(const vector<string>& data, int cycles)
{
    set<int> alive;
    for (int y = 0; y < data.size(); ++y)
    {
        const auto& row = data[y];
        for (int x = 0; x < row.size(); ++x)
        {
            if (row[x] == '#')
                alive.insert(DIMX*(x+OFF) + DIMY*(y+OFF) + DIMZ*OFF + DIMW*OFF);            
        }
    }
    // for (auto t: alive)
    //     cout << t << " ";

    for (int s = 0; s < cycles; ++s)
    {
        map<int, int> neighbours;
        for (auto c: alive)
        {
            int x = (c / DIMX) % DIM;
            int y = (c / DIMY) % DIM;
            int z = (c / DIMZ) % DIM;
            int w = (c / DIMW) % DIM;

            for (int i = x-1; i <= (x+1); ++i)
                for (int j = y-1; j <= (y+1); ++j)
                    for (int k = z-1; k <= (z+1); ++k)
                        for (int l = w-1; l <= (w+1); ++l)
                        {
                            if ((i == x) && (j == y) && (k == z) && (l == w))
                                continue;
                            //cout << i << " " << j << " " << k << " " << l << "\n";

                            int p = DIMX*(i+OFF) + DIMY*(j+OFF) + DIMZ*(k+OFF) + DIMW*(l+OFF);   
                            map<int, int>::iterator it = neighbours.find(p);
                            if (it == neighbours.end())         
                                neighbours[p] = 1;
                            else
                                neighbours[p] += 1;
                        }

            set<int> alive2;
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
            cout << s << " " << alive.size() << '\n';
        }
    }
    return alive.size();
}


int main()
{
    return part2b({".#.", "..#", "###"}, 6);
}

