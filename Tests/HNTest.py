import unittest
from HexNumber import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_convert(self):
         first = LinkedList('F1B3')
         first = first.convert()
         expect = 11

         result = first.head.next.next.val

         self.assertEqual(expect, result)

    def test_reconvert(self):
        first = LinkedList('F1B3')
        first = first.convert()
        first = first.reconvert()
        expect = "B"

        result = first.head.next.next.val

        self.assertEqual(expect, result)

    def test_add(self):
        first = LinkedList('F1B3'[::-1])
        second = LinkedList('89AB82'[::-1])
        expect = "A"

        result = first.add(second)
        result = result.head.next.next.next.next.val

        self.assertEqual(expect, result)

if name == 'main':
    unittest.main()