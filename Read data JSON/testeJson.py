import pyautogui as pa
import json

with open("Teste/dados.json") as dados:
  data = json.load(dados)

det = (data['det'])

# Constantes
ARRED_VALOR = 7
N_DI = 2406559431
D_DI = "27032024"
L_LOC_DESEMM = "URUGUAIANA"
UF_DES = "RS"
D_DESMB = "27032024"
TP_VIA_TRANSP = 7
TP_INTERMEDIO = 1
C_EXPORTADOR = "TECNOPERFILES S.A"

for i in range(len(data["det"])):
  cProd = det[i].get("prod").get("cProd")
  qCom = int(float(det[i].get("prod").get("qCom")))
  vUnCom = round(float(det[i].get("prod").get("vUnCom")),ARRED_VALOR)
  vFrete = det[i].get("prod").get("vFrete")
  vSeg = det[i].get("prod").get("vSeg")
  vOutro = det[i].get("prod").get("vOutro")
  nAdicao = det[i].get("prod").get("DI").get("adi").get("nAdicao")
  nSeqAdic = det[i].get("prod").get("DI").get("adi").get("nSeqAdic")
  cFabricante = det[i].get("prod").get("DI").get("adi").get("cFabricante")
  
  # IMPOSTOS
  # ICMS
  icms_vBC = det[i].get("imposto").get("ICMS").get("ICMS00").get("vBC")
  icms_pICMS = det[i].get("imposto").get("ICMS").get("ICMS00").get("pICMS")
  icms_vICMS = det[i].get("imposto").get("ICMS").get("ICMS00").get("vICMS")
  # IPI
  ipi_vBC = det[i].get("imposto").get("IPI").get("IPITrib").get("vBC")
  ipi_pIPI = det[i].get("imposto").get("IPI").get("IPITrib").get("pIPI")
  ipi_vIPI = det[i].get("imposto").get("IPI").get("IPITrib").get("vIPI")
  # II
  ii_vBC = det[i].get("imposto").get("II").get("vBC")
  ii_vDespAdu = det[i].get("imposto").get("II").get("vDespAdu")
  ii_vII = det[i].get("imposto").get("II").get("vII")
  ii_vIOF = det[i].get("imposto").get("II").get("vIOF")
  # PIS
  pis_vBC = det[i].get("imposto").get("PIS").get("PISAliq").get("vBC")
  pis_pPIS = det[i].get("imposto").get("PIS").get("PISAliq").get("pPIS")
  pis_vPIS = det[i].get("imposto").get("PIS").get("PISAliq").get("vPIS")
  # COFINS
  cofins_vBC = det[i].get("imposto").get("COFINS").get("COFINSAliq").get("vBC")
  cofins_pCOFINS = det[i].get("imposto").get("COFINS").get("COFINSAliq").get("pCOFINS")
  cofins_vCOFINS = det[i].get("imposto").get("COFINS").get("COFINSAliq").get("vCOFINS")

  print(cProd, qCom, vUnCom, vFrete, vSeg, vOutro, nAdicao, nSeqAdic, cFabricante, icms_vBC, icms_pICMS, icms_vICMS, ipi_vBC, ipi_pIPI, ipi_vIPI, ii_vBC, ii_vDespAdu, ii_vII, ii_vIOF, pis_vBC, pis_pPIS, pis_vPIS, cofins_vBC, cofins_pCOFINS, cofins_vCOFINS)