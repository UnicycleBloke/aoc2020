#include "utils.h"


struct Field
{
    string name;
    int    min1;
    int    max1;
    int    min2;
    int    max2;
};
using Fields  = vector<Field>;
using Ticket  = vector<int>;
using Tickets = vector<Ticket>;


bool matches_field(const Field& field, int value)
{
    if ((value >= field.min1) && (value <= field.max1)) return true;
    if ((value >= field.min2) && (value <= field.max2)) return true;
    return false;
}


bool matches_any_field(const Fields& fields, int value)
{
    for (const auto& field: fields)
        if (matches_field(field, value)) return true;
    return false;
}


int sum_invalid_fields(const Fields& fields, const Ticket& ticket)
{
    int result = 0;
    for (auto value: ticket)
    {
        if (!matches_any_field(fields, value))
        {
            result += value;
        }
    }
    return result;
}

int part1(const Fields& fields, const Tickets& nearby_tickets, const Ticket& ticket)
{
    int result = 0;
    for (const auto& nearby: nearby_tickets)
    {
        result += sum_invalid_fields(fields, nearby);
    }
    return result;
}


bool is_valid_ticket(const Fields& fields, const Ticket& ticket)
{
    for (auto value: ticket)
    {
        if (!matches_any_field(fields, value))
        {
            return false;
        }
    }
    return true;
}


bool matches_ticket(const Field& field, const Ticket& ticket, int index)
{
    return matches_field(field, ticket[index]);
}


bool matches_all_tickets(const Field& field, const Tickets& tickets, int index)
{
    for (const auto& ticket: tickets)
    {
        if (!matches_ticket(field, ticket, index))
            return false;
    }
    return true;
}


int part2(const Fields& fields, const Tickets& nearby_tickets, const Ticket& ticket)
{
    // Eliminate duff tickets.
    Tickets valid_tickets;
    for (const auto& nearby: nearby_tickets)
    {
        if (is_valid_ticket(fields, nearby))
            valid_tickets.push_back(nearby);
    }

    // Grid of fields and columns. All zeroes at first. A one means all tickets match 
    Tickets grid;
    for (const auto& field: fields)
    {
        Ticket row;
        for (int i = 0; i < fields.size(); ++i)
            row.push_back(matches_all_tickets(field, nearby_tickets, i));
    }

    // Now examine the grid to solve the constraints.

    return 0;
}


void solve(const string& filename)
{
    auto lines = aoc::read_lines(filename);
    lines.push_back(""); // Terminator
    size_t i = 0;

    Fields fields;
    while (true)
    {
        const auto& line = lines[i++];
        smatch sm;
        if (!regex_search(line, sm, regex{ R"((.*):\s+(\d+)-(\d+)\s+or\s+(\d+)-(\d+))" })) 
            break;
        fields.push_back(Field{sm[1], stoi(sm[2]), stoi(sm[3]), stoi(sm[4]), stoi(sm[5])});
    }

    Ticket ticket;
    auto items = aoc::split(lines[i++], ",", false);
    for (const auto& p: items)
        ticket.push_back(stoi(p));

    Tickets nearby_tickets;
    ++i;
    while (true)
    {
        const auto& line = lines[i++];
        if (line.size() == 0) break;
        auto items = aoc::split(line, ",", false);

        Ticket ticket;
        for (const auto& p: items)
            ticket.push_back(stoi(p));
        nearby_tickets.push_back(ticket);
    }

    cout << filename << '\n';
    cout << "Part1: " << part1(fields, nearby_tickets, ticket) << '\n';
    cout << "Part2: " << part2(fields, nearby_tickets, ticket) << '\n';
}


int main()
{
    solve("C:\\Projects\\aoc2020\\day16\\day16-input.txt");
}