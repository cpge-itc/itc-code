from cpge import PriorityQueue

def test_priority_dict():
    q = PriorityQueue()
    q.add('a', 1)
    q.add('b', 2)
    assert(q.take_min() == 'a')
    q.add('c', 3)
    q.update('c', 1.5)
    assert(q.take_min() == 'c')
