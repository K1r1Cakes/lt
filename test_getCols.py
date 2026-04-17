from getbest import getCols
from io import StringIO

def test_getCols():
    file = StringIO("Course, Student Number, Mark, Comment")
    
    num_col, mark_col = getCols(File)

    assert num_col == 1
    assert mark_col == 2


