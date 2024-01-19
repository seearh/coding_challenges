### Repository ###
This is a personal repository, belonging to Tay Cong Run, to store 
solutions to code challenges that are sourced from various platforms 
(e.g. HackerRank, Advent of Code, etc). They can be freely referenced
by anyone for educational purposes.

### Directory Structure ###
kdb (Coding challenge solutions in kdb)
  aoc_2023 (Advent of Code 2023)
  unit_tests (All k4unit test cases & files)
    aoc_2023
python (Coding challenge solutions in Python)
  hackerrank (Hacker Rank Challenges)
  unit_tests (All Python unittest cases)

### Unit Testing ###
kdb
  Unit testing for kdb uses the k4unit framework. To be exact, it is a
  forked repository of the vanilla k4unit that is embedded into this
  repository as a git submodule. The forked k4unit additionally supports
  test discovery and command-line arguments. To begin, run the
  coding_challenges/kdb/unit_tests/k4unit/k4unit.q file from anywhere.

Python
  Unit testing for Python uses the unittest framework. The directory
  structure and test files have been written to work with VSCode Python
  Extension. See https://code.visualstudio.com/docs/python/testing.

