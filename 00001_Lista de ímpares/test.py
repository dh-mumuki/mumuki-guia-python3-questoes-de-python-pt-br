class Test(unittest.TestCase):

  def test_deve_retornar_numeros_impares(self):
    input = [1,2,3,127,256,377]
    self.assertListEqual(impares(input), [1,3,127,377])