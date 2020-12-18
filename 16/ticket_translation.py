def num_in_ranges(num, ranges):
    for r in ranges:
        start, end = r.split('-')
        if int(start) <= num <= int(end):
            return True
    return False

def invalid_ticket_values(ticket, ranges):
    invalid = []
    for num in ticket:
        if not num_in_ranges(num, ranges):
            invalid.append(num)
    return invalid

def ticket_transalation_01(rules, tickets):
    invalid = []
    rules_values = [r for rule in rules.values() for r in rule]
    for ticket in tickets:
        invalid += invalid_ticket_values(ticket, rules_values)
    return sum(invalid)

def ticket_transalation_02(rules, tickets, your_ticket):
    rules_values = [r for rule in rules.values() for r in rule]
    valid_tickets = [ticket for ticket in tickets if len(invalid_ticket_values(ticket, rules_values)) == 0]

    positions = dict()
    for name, rule in rules.items():
        for i in range(len(valid_tickets[0])):
            if len(invalid_ticket_values([ticket[i] for ticket in valid_tickets], rule)) == 0:
                positions[name] = positions[name]+[i] if name in positions else [i]
    position_keys = list(reversed(dict(sorted(positions.items(), key=lambda item: len(item[1]))).keys()))
    for i, key in enumerate(position_keys[:-1]):
        positions[key] = list(set(positions[key]) - set(positions[position_keys[i + 1]]))
    
    ticket_indices = [i[0] for name, i in positions.items() if name[:3] == 'dep']
    final = 1
    for i in ticket_indices:
        final *= your_ticket[i]
    return final

if __name__ == "__main__":
    with open('input.txt') as f:
        contents = [x.split('\n') for x in f.read().split('\n\n')]
        rules = {g[0]: g[1].split(' or ') for g in [l.split(': ') for l in contents[0]]}
        your_ticket = [int(i) for i in contents[1][1].split(',')]
        nearby_tickets = [list(map(lambda x : int(x), ticket.split(','))) for ticket in contents[2][1:]]

    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(ticket_transalation_01(rules, nearby_tickets)))
        f.write("Part two: {}\n".format(ticket_transalation_02(rules, nearby_tickets, your_ticket)))

