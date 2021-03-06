#!/usr/bin/env python3

# 94th/84th for part 1 and 2 respectively. Cast at
# https://asciinema.org/a/0ja296g1KGbDEnfrkRzq4egGz


def solve(start, states, bursts, transitions):
    next_state = dict(zip(transitions, transitions[1:] + transitions))
    d = (-1, 0)
    p = start
    infected = 0
    for _ in range(bursts):
        state = states.get(p, 'clean')
        if state == 'clean':
            if d[1] == 0:
                d = (0, d[0])
            else:
                d = (-1 * d[1], 0)
        elif state == 'infected':
            if d[1] == 0:
                d = (0, -1 * d[0])
            else:
                d = (d[1], 0)
        elif state == 'flagged':
            d = (-1 * d[0], -1 * d[1])
        state = next_state[state]
        if state == 'infected':
            infected += 1
        states[p] = state
        p = (p[0] + d[0], p[1] + d[1])
    return infected


states = {}
lines = [l.strip() for l in open('input')]
for r, row in enumerate(lines):
    for c, v in enumerate(row.strip()):
        if v == '#':
            states[(r, c)] = 'infected'

start = (len(lines) // 2, len(lines[0]) // 2)
print('A', solve(start, dict(states), 10000, ['clean', 'infected']))
print('B',
      solve(start, dict(states), 10000000,
            ['clean', 'weakened', 'infected', 'flagged']))
