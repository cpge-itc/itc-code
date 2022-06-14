from cpge.ds.priority_queue.list import PriorityList

def test_priority_list():
    elements = [1, 5, 4]
    priorities = [7, 2, 9]
    q = PriorityList(elements, priorities)
    assert(q.take_min() == (5, 2))