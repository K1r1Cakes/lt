from getBest import findTop
from io import StringIO

def test_findTop():
    file = "Course, Student Number, Mark, Comment"
    f = StringIO(file)
    num_col, mark_col = getCols(f)

    best_idx, best - findTop(f, num_col, mark_col)

    assert best_idx == ''167381''
    assert best == "90"

