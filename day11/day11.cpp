#include "utils.h"


using namespace std;


bool step1(vector<string>& grid1, vector<string>& grid2)
{
    for (int r = 1; r < (grid1.size() - 1); ++r)
    {
        for (int c = 1; c < (grid1[0].size() - 1); ++c)
        {
            int occ = 0;
            //occ += (grid1[r  ][c] == '#') ? 1 : 0;
            occ += (grid1[r+1][c]   == '#') ? 1 : 0;
            occ += (grid1[r-1][c]   == '#') ? 1 : 0;
            occ += (grid1[r  ][c+1] == '#') ? 1 : 0;
            occ += (grid1[r+1][c+1] == '#') ? 1 : 0;
            occ += (grid1[r-1][c+1] == '#') ? 1 : 0;
            occ += (grid1[r  ][c-1] == '#') ? 1 : 0;
            occ += (grid1[r+1][c-1] == '#') ? 1 : 0;
            occ += (grid1[r-1][c-1] == '#') ? 1 : 0;

            if ((occ == 0) && (grid1[r][c] == 'L'))
                grid2[r][c] = '#';
            else if ((occ >= 4) && (grid1[r][c] == '#'))
                grid2[r][c] = 'L';
            else 
                grid2[r][c] = grid1[r][c];
        }
    }

    return (grid2 == grid1);
}


int visible(vector<string>& grid1, int r, int c, int rdel, int cdel)
{
    while (true)
    {
        r += rdel;
        if ((r == 0) || (r == (grid1.size() - 1)))
            return 0; 
        c += cdel;
        if ((c == 0) || (c == (grid1[0].size() - 1)))
            return 0;
        if (grid1[r][c] == '#')
            return 1;
        if (grid1[r][c] == 'L')
            return 0;
    }
    return 0;
}


bool step2(vector<string>& grid1, vector<string>& grid2)
{
    for (int r = 1; r < (grid1.size() - 1); ++r)
    {
        for (int c = 1; c < (grid1[0].size() - 1); ++c)
        {
            int occ = 0;
            occ += visible(grid1, r, c,  1,  1);
            occ += visible(grid1, r, c,  1,  0);
            occ += visible(grid1, r, c,  1, -1);
            occ += visible(grid1, r, c,  0,  1);
            //occ += visible(grid1, r, c,  0,  0);
            occ += visible(grid1, r, c,  0, -1);
            occ += visible(grid1, r, c, -1,  1);
            occ += visible(grid1, r, c, -1,  0);
            occ += visible(grid1, r, c, -1, -1);

            if ((occ == 0) && (grid1[r][c] == 'L'))
                grid2[r][c] = '#';
            else if ((occ >= 5) && (grid1[r][c] == '#'))
                grid2[r][c] = 'L';
            else 
                grid2[r][c] = grid1[r][c];
        }
    }

    return (grid2 == grid1);
}


int part1(const vector<string>& grid)
{
    vector<string> grid2 = grid;
    vector<string> grid1 = grid;
    while (true)
    {
        if (step1(grid1, grid2)) break;
        if (step1(grid2, grid1)) break;
    }        

    int result = 0;
    for (int r = 1; r < grid1.size() - 1; ++r)
        for (int c = 1; c < grid1[0].size() - 1; ++c)
            if (grid1[r][c] == '#')
                result += 1;
    return result;
}


// Not exactly DRY, but not important for AOC...
int part2(const vector<string>& grid)
{
    vector<string> grid2 = grid;
    vector<string> grid1 = grid;
    while (true)
    {
        if (step2(grid1, grid2)) break;
        if (step2(grid2, grid1)) break;
    }        

    int result = 0;
    for (int r = 1; r < grid1.size() - 1; ++r)
        for (int c = 1; c < grid1[0].size() - 1; ++c)
            if (grid1[r][c] == '#')
                result += 1;
    return result;
}


void solution(const char* file)
{
    cout << "Input: " << file << '\n';
    std::ifstream is{file};
    auto lines = aoc::read_lines(is);

    // Create a grid with a border to avoid edge checks.
    vector<string> grid;
    grid.push_back(string(lines[0].size() + 2, '.'));
    for (const auto& line: lines)
    {
        grid.push_back(string(string{'.'} + line + '.'));
    }
    grid.push_back(string(lines[0].size() + 2, '.'));

    auto p1 = part1(grid);
    cout << "Part1: " << p1 << '\n';

    auto p2 = part2(grid);
    cout << "Part2: " << p2 << '\n';
}


int main(int argc, char** argv)
{
    solution("day11-test.txt");
    solution("day11-input.txt");
}
