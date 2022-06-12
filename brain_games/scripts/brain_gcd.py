#!/usr/bin/env python
from brain_games.engine import engine
from brain_games.games.gcd import gcd


def main():
    engine(gcd)


if __name__ == '__main__':
    main()
