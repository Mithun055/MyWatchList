import project
from tabulate import tabulate
import sys
import csv
import glob
import pandas as pd
import pytest


def main():
    test_key_A()
    test_key_U()
    test_key_D()
    test_key_C()


def test_key_C():
    project.key_C(name="test")
    assert project.view(name="test") == "\n".join(
        [
            "╭───────┬────────┬──────────┬──────────╮",
            "│ SNO   │ Name   │ Status   │ Rating   │",
            "├───────┼────────┼──────────┼──────────┤",
            "╰───────┴────────┴──────────┴──────────╯",
        ]
    )


def test_key_A():
    project.key_A(name="test", sno=1, _name="GOT", status="Completed", rating=7.9)
    assert project.view("test") == "\n".join(
        [
            "╭───────┬────────┬───────────┬──────────╮",
            "│   SNO │ Name   │ Status    │   Rating │",
            "├───────┼────────┼───────────┼──────────┤",
            "│     1 │ GOT    │ Completed │      7.9 │",
            "╰───────┴────────┴───────────┴──────────╯",
        ]
    )
    project.key_A(name="test", sno=2, _name="HOD", status="On Hold", rating=8.3)
    assert project.view("test") == "\n".join(
        [
            "╭───────┬────────┬───────────┬──────────╮",
            "│   SNO │ Name   │ Status    │   Rating │",
            "├───────┼────────┼───────────┼──────────┤",
            "│     1 │ GOT    │ Completed │      7.9 │",
            "│     2 │ HOD    │ On Hold   │      8.3 │",
            "╰───────┴────────┴───────────┴──────────╯",
        ]
    )
    project.key_A(
        name="test", sno=3, _name="Breaking Bad", status="Completed", rating=9.7
    )
    assert project.view("test") == "\n".join(
        [
            "╭───────┬──────────────┬───────────┬──────────╮",
            "│   SNO │ Name         │ Status    │   Rating │",
            "├───────┼──────────────┼───────────┼──────────┤",
            "│     1 │ GOT          │ Completed │      7.9 │",
            "│     2 │ HOD          │ On Hold   │      8.3 │",
            "│     3 │ Breaking Bad │ Completed │      9.7 │",
            "╰───────┴──────────────┴───────────┴──────────╯",
        ]
    )


def test_key_U():
    project.key_U(name="test", update="Rating", sno=3, update_=9.9)
    assert project.view("test") == "\n".join(
        [
            "╭───────┬──────────────┬───────────┬──────────╮",
            "│   SNO │ Name         │ Status    │   Rating │",
            "├───────┼──────────────┼───────────┼──────────┤",
            "│     1 │ GOT          │ Completed │      7.9 │",
            "│     2 │ HOD          │ On Hold   │      8.3 │",
            "│     3 │ Breaking Bad │ Completed │      9.9 │",
            "╰───────┴──────────────┴───────────┴──────────╯",
        ]
    )


def test_key_D():
    project.key_D(name="test", row=3)
    assert project.view(name="test") == "\n".join(
        [
            "╭───────┬────────┬───────────┬──────────╮",
            "│   SNO │ Name   │ Status    │   Rating │",
            "├───────┼────────┼───────────┼──────────┤",
            "│     1 │ GOT    │ Completed │      7.9 │",
            "│     2 │ HOD    │ On Hold   │      8.3 │",
            "╰───────┴────────┴───────────┴──────────╯",
        ]
    )


if __name__ == "__main__":
    main()
