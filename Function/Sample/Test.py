import unittest
import Sample
   
class SimpleTest(unittest.TestCase):
	def testadd1(self):
		self.assertEquals(Sample.add(4,5),9)
      
if __name__ == '__main__':
   unittest.main()
