import pymunk as p
from pymunk.vec2d import Vec2d
import unittest

####################################################################

class UnitTestGeneral(unittest.TestCase):
    
    def testGeneral(self):
        p.version
        p.inf
        p.chipmunk_version
        
        m = p.moment_for_box(1, 2, 3)
        self.assertAlmostEqual(m, 1.08333333333)
        
        m = p.moment_for_segment(1, Vec2d(-1,0), Vec2d(1,0))
        self.assertAlmostEqual(m, 0.33333333333)
        
           
        
        
class UnitTestBB(unittest.TestCase):
    def setUp(self):
        #print "testing pymunk version " + p.version
        pass
        
    def testCreation(self):
        bb_empty = p.BB()
        
        self.assertEqual(bb_empty.left, 0)
        self.assertEqual(bb_empty.bottom, 0)
        self.assertEqual(bb_empty.right, 0)
        self.assertEqual(bb_empty.top , 0)
        
        bb_defined = p.BB(-10,-5,15,20)
        
        self.assertEqual(bb_defined.left, -10)
        self.assertEqual(bb_defined.bottom, -5)
        self.assertEqual(bb_defined.right, 15)
        self.assertEqual(bb_defined.top, 20)
            
    def testMethods(self):
        bb1 = p.BB(0,0,10,10)
        bb2 = p.BB(10,10,20,20)
        bb3 = p.BB(4,4,5,5)
        v1 = Vec2d(1,1)
        v2 = Vec2d(100,5)
        self.assert_(bb1.intersects(bb2))

        self.assertFalse(bb1.contains(bb2))
        self.assert_(bb1.contains(bb3))
        
        self.assert_(bb1.contains_vect(v1))
        self.assertFalse(bb1.contains_vect(v2))
        
        self.assertEqual(bb1.merge(bb2), p.BB(0,0,20,20))
        
        self.assertEqual(bb1.expand(v1), bb1)
        self.assertEqual(bb1.expand(-v2), p.BB(-100,-5,10,10))
        
        self.assertEqual(bb1.clamp_vect(v2), Vec2d(10,5))
        
        self.assertEqual(bb1.wrap_vect((11,11)), (1,1))

class UnitTestBugs(unittest.TestCase):
    def testManyBoxCrash(self):
        space = p.Space()
        for x in [1,2]:
            for y in range(16):
                size = 10
                box_points = map(Vec2d, [(-size, -size), (-size, size), (size,size), (size, -size)])
                body = p.Body(10,20)
                shape = p.Poly(body, list(box_points), Vec2d(0,0))
                space.add(body, shape)
            space.step(1/50.0)
####################################################################
if __name__ == "__main__":
    print ("testing pymunk version " + p.version)
    unittest.main()