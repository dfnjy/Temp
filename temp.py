import unittest

class Solution(object):
    '''
    Based on description, I assume that:
        1. Each doctor was presented by id, following with a vector of features (specific specialty, area, review score etc.). Features are discretized. So doctors are coming as an matrix.
            1.1 Specialty is an integer (Radiologist=1, Dentist=2). If we need to include similarities of the specialties, we could use a tree like numberings (General Dentist=100, Orthodontist=101, etc.)
            1.2 Area is the first 5 digits of zip code.
            1.3 Score is an int
            1.4 All features are standardized to (0,1). Or I can do it once.
        2. We can define an weight vector for features if needed. Here I just use numbers from 1 to 5 increased by 1, assuming that the features are ordered so that more important features are closer to the front.
    So my algorithm is sorting the doctors by something like weighted Euclidean distance.
    
    '''
    def __init__(self, doctors):
        self.mat_doctors=doctors
        self.num_doctors=len(doctors)
        self.weight=5

    def FindSimilarDoctor(self, doc_idx):
        if (self.num_doctors==0 or doc_idx>=self.num_doctors):
            return []
        doctors=[x[:] for x in self.mat_doctors]
        target_doctor = self.mat_doctors[doc_idx]
        for i in range(self.num_doctors):
            for j in range(1, len(doctors[0])):
                doctors[i][j] = abs(doctors[i][j]-target_doctor[j]) * (self.weight-j+1)
        sorted_doctors = sorted(doctors, key=lambda x: sum(x[1:]))
        return [row[0] for row in sorted_doctors][1:]

class MyTest(unittest.TestCase):

    def test_edge(self):
        doctors=[]
        self.sol=Solution(doctors)
        self.assertEqual(self.sol.FindSimilarDoctor(1), [])
        self.assertEqual(self.sol.FindSimilarDoctor(0), [])

    def test_func(self):
        doctors=[[0,0.2,0.2],[1,0.7,0.7],[2,0.5,0.2],[3,0.2,0.1],[4,0.6,0.7]]
        self.sol=Solution(doctors)
        self.assertEqual(self.sol.FindSimilarDoctor(0), [3,2,4,1])
        self.assertEqual(self.sol.FindSimilarDoctor(1), [4,2,0,3])
        self.assertEqual(self.sol.FindSimilarDoctor(2), [0,3,4,1])
        self.assertEqual(self.sol.FindSimilarDoctor(3), [0,2,4,1])
        self.assertEqual(self.sol.FindSimilarDoctor(4), [1,2,0,3])

if __name__=="__main__":
    unittest.main()

