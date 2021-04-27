import pytest
import solution

def test_path_finding():
    class _s:
        o=''
    def p(o): _s.o = o
    i = iter(['2', '2', '00', '00'])
    solution.input = lambda: next(i)
    solution.print = p
    solution.solution1()
    print(_s.o)
    assert _s.o == 2

def test_dynamic_approach():
    class _s:
        o=''
    def p(o): _s.o = o
    i = iter(['2', '2', '00', '00'])
    solution.input = lambda: next(i)
    solution.print = p
    solution.solution2()
    print(_s.o)
    assert _s.o == 2

def test_path_finding2():
    class _s:
        o=''
    def p(o): _s.o = o
    i = iter(['3', '3', '000', '000', '000'])
    solution.input = lambda: next(i)
    solution.print = p
    solution.solution1()
    print(_s.o)
    assert _s.o == 6

def test_dynamic_approach2():
    class _s:
        o=''
    def p(o): _s.o = o
    i = iter(['3', '3', '000', '000', '000'])
    solution.input = lambda: next(i)
    solution.print = p
    solution.solution2()
    print(_s.o)
    assert _s.o == 6