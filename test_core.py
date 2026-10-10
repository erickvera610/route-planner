import unittest
from core import shortest_path,dijkstra
class Tests(unittest.TestCase):
    def test_open_grid(self): self.assertEqual(shortest_path(4,[0,0],[3,3],[])['distance'],6)
    def test_blocked_route(self): self.assertEqual(shortest_path(3,[0,0],[2,2],[[1,0],[0,1]])['path'],[])
    def test_same_endpoint(self): self.assertEqual(shortest_path(3,[0,0],[0,0],[])['distance'],0)
    def test_weighted(self): self.assertEqual(dijkstra({'a':[('b',8),('c',2)],'c':[('b',1)]},'a','b'),3)
    def test_negative(self):
        with self.assertRaises(ValueError): dijkstra({'a':[('b',-1)]},'a','b')
    def test_avoids_obstacles(self):
        r=shortest_path(4,[0,0],[3,3],[[1,0]]);self.assertNotIn([1,0],r['path'])
