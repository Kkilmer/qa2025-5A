import unittest
from imc import calcular_imc, classificar_imc

class TestIMC(unittest.TestCase):

    def test_cal_imc_valido(self):
        self.assertEqual(calcular_imc(70, 1.75), 22.86)

    def testClassificacaoAbaixoPeso(self):
        self.assertEqual(classificar_imc(17.5), "Abaixo do peso")

    def testClassificacaoPesoNormal(self):
        self.assertEqual(classificar_imc(22.0), "Peso normal")

    def testClassificacaoSobrepeso(self):
        self.assertEqual(classificar_imc(27.0), "Sobrepeso")

    def testClassificacaoObesidadeGrau1(self):
        self.assertEqual(classificar_imc(32.0), "Obesidade grau 1")

    def testClassificacaoObesidadeGrau2(self):
        self.assertEqual(classificar_imc(37.0), "Obesidade grau 2")

    def testClassificacaoObesidadeGrau3(self):
        self.assertEqual(classificar_imc(42.0), "Obesidade grau 3")
    
    def testValoresInvalidos(self):
        with self.assertRaises(ValueError):
            calcular_imc(0, 1.75)
        with self.assertRaises(ValueError):
            calcular_imc(70, 0)
        with self.assertRaises(ValueError):
            calcular_imc(-5, 1.75)

if __name__ == '__main__':
    unittest.main()