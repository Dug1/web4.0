import unittest
from "../layout.py" import Layout

class TestLayout(unittest.TestCase):

    def setUp(self):
        self.base = Layout({"x":0, "y":0, "width":1000, "height": 500})

    def testInit(self):
        base = self.base
        self.assertEqual(base.get_x(), 0)
        self.assertEqual(base.get_y(), 0)
        self.assertEqual(base.get_height(), 500)
        self.assertEqual(base.get_width(), 1000)
    
    def testAddChild(self):
        base = self.base
        child = Layout({"width":500, "height":500})
        self.base.add_child(child)

        self.assertEqual(len(base.get_children), 1)
        self.assertTrue(child in base.get_children())
        self.assertIs(child.parent(), self.base)
        
        self.base.add_child(child)
        self.assertEqual(len(base.get_children()), 1)

        self.remove_child(child)
        self.assertEqual(len(base.get_children()), 0)

    def testFloating(self):
        base = self.base
        child = Layout({"width":500, "height":500})
        base.add_child(child)

        self.assertEqual(base.get_vertical_float(), "top")
        self.assertEqual(base.get_horizontal_float(), "left")
        child.assertEqual(child.get_x(), 0)
        child.assertEqual(child.get_y(), 0)

        grandchild = Layout({"width":100, "height":200})
        child.add_child(grandchild)
        child.set_vertical_float("center")
        child.set_horizontal_float("center")
        self.assertEqual(base.get_x(), 200)
        self.assertEqual(base.get_y(), 150)
        
        base.set_horizontal_float("right")
        self.assertEqual(child.get_x(), 500)
        self.assertEqual(child.get_y(), 0)
        self.assertEqual(child.get_x(), 700)
        self.assertEqual(child.get_y(), 150)

    def testRelativeSizing(self):
        child = Layout({"width":0.5, "height":0.1, "parent":self.base})
        self.assertEqual(child.get_height(), 50)
        self.assertEqual(child.get_width(), 500)

        self.base.set_x(600)
        self.assertEqual(child.get_height(), 50)
        self.assertEqual(child.get_width(), 300)
        
        self.base.set_y(1000)
        self.assertEqual(child.get_height(),100)
        self.assertEqual(child.get_width(), 300)

        grandchild = Layout({"width":1.0, "height":0.6, "parent":self.child})
        self.assertEqual(grandchild.get_width(), 300)
        self.assertEqual(grandchild.get_height(), 60)
        
        self.base.set_x(1000)
        self.assertEqual(child.get_width(), 500)
        self.assertEqual(grandchild.get_width(), 500)

        self.base.set_y(500)
        self.assertEqual(child.get_height(), 50)
        self.assertEqual(grandchild.get_height(), 25)

    def testOrientation(self):
        base = self.base
        self.assertEqual(base.get_orientation(), "vertical")
        
        child = Layout({"width":100, "height":100})
        child2 = Layout({"width":100, "height":100})
        child3 = Layout({"width":100, "height":100})


        self.assertEqual(child.get_x(), 0)
        self.assertEqual(child.get_y(), 0)
        self.assertEqual(child.get_x(), 0)
        self.assertEqual(child.get_y(), 100)
        self.assertEqual(child.get_x(), 0)
        self.assertEqual(child.get_y(), 200)
        
        base.set_orientation("horizontal")

        self.assertEqual(child.get_x(), 0)
        self.assertEqual(child.get_y(), 0)
        self.assertEqual(child.get_x(), 100)
        self.assertEqual(child.get_y(), 0)
        self.assertEqual(child.get_x(), 200)
        self.assertEqual(child.get_y(), 0)

        #Test float with float
        base.set_horizontal_float("


