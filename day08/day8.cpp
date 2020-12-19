#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <regex>
#include <filesystem>
#include "utils.h"


using namespace std;


enum class Opcode { acc, jmp, nop };


struct Instruction
{
    Opcode opcode;
    int    number;
};


using Program = vector<Instruction>;


class Machine
{
public:
    bool run(const Program& prog);

    int acc() const { return m_acc; }
    int pc() const  { return m_pc; }

private:
    int m_acc{};
    int m_pc{};    
};


bool Machine::run(const Program& prog)
{
    set<int> seen;

    m_acc = 0;
    m_pc  = 0;
    while (true)
    {
        // End of program
        if (m_pc == prog.size())
        {
            return true;
        }

        // Already been to this address
        if (seen.find(m_pc) != seen.end())
        {
            return false;
        }
        seen.insert(m_pc);

        // Process the instruction
        const auto& inst = prog[m_pc];
        switch (inst.opcode)
        {
            case Opcode::acc:
                m_acc += inst.number;
                m_pc  += 1;
                break;
            case Opcode::jmp:
                m_pc  += inst.number;
                break;
            case Opcode::nop:
                m_pc  += 1;
                break;
        }
    } 
}


Opcode opcode_of(const string& str)
{
    static const map<string, Opcode> opcodes 
    {
        { "acc", Opcode::acc },
        { "jmp", Opcode::jmp },
        { "nop", Opcode::nop },
    };

    auto it = opcodes.find(str);
    if (it == opcodes.end())
        throw runtime_error{"Unknown opcode"};
    return it->second;
}


// Find acc just before infinite loop
void part1(const Program& prog)
{
    Machine m;
    m.run(prog);
    cout << "Part1: " << m.acc() << '\n';    
}


// Find acc on completion after fixing one instruction
void part2(Program& prog)
{
    cout << "Part2: ";

    Machine m;
    for (int pc = 0; pc < prog.size(); ++pc)
    {
        auto& inst = prog[pc];
        switch (inst.opcode)
        {
            case Opcode::acc:
                break;

            case Opcode::jmp:
                inst.opcode = Opcode::nop;
                if (m.run(prog)) 
                {
                    cout << m.acc() << '\n';    
                    return;
                }
                inst.opcode = Opcode::jmp;
                break;

            case Opcode::nop:
                inst.opcode = Opcode::jmp;
                if (m.run(prog)) 
                {
                    cout << m.acc() << '\n';    
                    return;
                }
                inst.opcode = Opcode::nop;
                break;
        }
    }
}


void solution(std::istream& is)
{
    auto lines = aoc::read_lines(is);

    Program prog;
    for (const auto& line: lines)
    {
        std::smatch sm;
        if (regex_match(line, sm, std::regex{ R"((\w+)\s+(.+))" }))
        {
            prog.push_back({opcode_of(sm[1]), stoi(sm[2])});
        }
        else
        {
            throw runtime_error{"Regex failure"};
        }
        
    }

    part1(prog);
    part2(prog);
}


int main(int argc, char** argv)
{
    if (argc < 2)
    {
        std::cout << "Provide input file name\n";
        return -1;
    }
    if (!std::filesystem::is_regular_file(argv[1]))
    {
        std::cout << "Provide valid input file name\n";
        return -1;
    }

    std::ifstream is{argv[1]};
    try 
    {
        solution(is);
    }
    catch (runtime_error& e)
    {
        cout << "ERROR: " << e.what() << '\n';
    }
}
