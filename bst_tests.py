import unittest
from bst import *
class TestCases(unittest.TestCase):
    def test_node(self):
        node = BSTNode(1, 2, 3)
        self.assertEqual(node, BSTNode(1,2,3))

    def test_bst(self):
        bst = BinarySearchTree(False, BSTNode(1, None, None))
        self.assertEqual(bst, BinarySearchTree(False, BSTNode(1, None, None)))

    def test_comes_before1(self):
        self.assertFalse(comes_before(None, 1))

    def test_comes_before2(self):
        self.assertFalse(comes_before(1, None))

    def test_comes_before3(self):
        self.assertFalse(comes_before(4, 1))

    def test_comes_before4(self):
        self.assertTrue(comes_before(1, 2))

    def test_is_empty1(self):
        bst = BinarySearchTree(False)
        self.assertTrue(is_empty(bst))

    def test_is_empty2(self):
        bst = BinarySearchTree(False, 1)
        self.assertFalse(is_empty(bst))

    def test_lookup1(self):
        bst = BinarySearchTree(False)
        self.assertFalse(lookup(bst,0))

    def test_lookup2(self):
        bst = BinarySearchTree(False, BSTNode(2,BSTNode(1,None,None),BSTNode(3,None,None)))
        self.assertFalse(lookup(bst, 0))

    def test_lookup3(self):
        bst = BinarySearchTree(False, BSTNode(2,BSTNode(1,None,None),BSTNode(3,None,None)))
        self.assertTrue(lookup(bst, 1))

    def test_lookup_help1er1(self):
        bst = BinarySearchTree(False)
        self.assertFalse(lookup_helper(bst.bst_node, 1))

    def test_lookup_helper2(self):
        node = BSTNode(1,None,None)
        self.assertTrue(lookup_helper(node, 1))

    def test_lookup_helper3(self):
        node = BSTNode(2,BSTNode(1,None,None),BSTNode(3,None,None))
        self.assertTrue(lookup_helper(node,3))

    def test_lookup_helper4(self):
        node = BSTNode(2,BSTNode(1,None,None),BSTNode(3,None,None))
        self.assertTrue(lookup_helper(node,1))

    def test_lookup_helper5(self):
        node = BSTNode(2,BSTNode(1,None,None),BSTNode(3,None,None))
        self.assertFalse(lookup_helper(node,0))

    def test_delete1(self):
        bst = BinarySearchTree(False)
        self.assertEqual(delete(bst,0),bst)

    def test_delete2(self):
        bst = BinarySearchTree(False, BSTNode(2,BSTNode(1,None,None),BSTNode(3,None,None)))
        self.assertEqual(delete(bst, 0),bst)

    def test_delete3(self):
        bst = BinarySearchTree(False, BSTNode(2,BSTNode(1,None,None),BSTNode(3,None,None)))
        bst1 = BinarySearchTree(False, BSTNode(2,None,BSTNode(3,None,None)))
        self.assertEqual(delete(bst, 1),bst1)

    def test_delete_helper1(self):
        node = BSTNode(2,BSTNode(1,None,None),BSTNode(3,None,None))
        self.assertEqual(delete_helper(node,0),node)

    def test_delete_helper2(self):
        bst = BinarySearchTree(False)
        self.assertEqual(delete_helper(bst.bst_node, 1),bst.bst_node)

    def test_delete_helper3(self):
        node = BSTNode(2,BSTNode(1,None,None),BSTNode(3,None,None))
        node1 = BSTNode(1,None,BSTNode(3,None,None))
        self.assertEqual(delete_helper(node,2),node1)

    def test_delete_helper4(self):
        node = BSTNode(2,BSTNode(1,None,None),BSTNode(3,None,None))
        node1 = BSTNode(2,BSTNode(1,None,None),None)
        self.assertTrue(delete_helper(node,3),node1)

    def test_delete_helper5(self):
        node = BSTNode(2,BSTNode(1,None,None),BSTNode(3,None,None))
        node1 = BSTNode(2,None,BSTNode(3,None,None))
        self.assertEqual(delete_helper(node,1),node1)

    def test_isert1(self):
        bst = BinarySearchTree(False)
        bst1 = BinarySearchTree(False, BSTNode(1,None,None))
        self.assertEqual(insert(bst, 1),bst1)

    def test_isert2(self):
        bst = BinarySearchTree(False, BSTNode(2,None,BSTNode(3,None,None)))
        bst1 = BinarySearchTree(False, BSTNode(2,BSTNode(1,None,None),BSTNode(3,None,None)))
        self.assertEqual(insert(bst, 1),bst1)

    def test_isert3(self):
        bst = BinarySearchTree(False, BSTNode(2,BSTNode(1,None,None),None))
        bst1 = BinarySearchTree(False, BSTNode(2,BSTNode(1,None,None),BSTNode(3,None,None)))
        self.assertEqual(insert(bst, 3),bst1)

    def test_insert_helper1(self):
        bst = BinarySearchTree(False)
        node1 = BSTNode(1,None,None)
        self.assertEqual(insert_helper(bst.bst_node, 1),node1)

    def test_insert_helper2(self):
        node = BSTNode(2,BSTNode(1,None,None),BSTNode(3,None,None))
        node1 = BSTNode(2,None,BSTNode(3,None,None))
        self.assertEqual(insert_helper(node1,1),node)

    def test_insert_helper3(self):
        node = BSTNode(2,BSTNode(1,None,None),BSTNode(3,None,None))
        node1 = BSTNode(2,BSTNode(1,None,None),None)
        self.assertEqual(insert_helper(node1,3),node)


if __name__ == '__main__':
    unittest.main()
