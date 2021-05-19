#! /usr/bin/env python3
# coding: utf-8

from programs.feuilles import Index
from programs.feuilles import Perimeter
from programs.feuilles import Summary
from programs.feuilles import Gini
from programs.feuilles import ClassificationReport
from programs.feuilles import Correlation
from programs.feuilles import Overrides
from programs.feuilles import ISISvg
from programs.feuilles import IQS
from programs.feuilles import ScoreDistribution

from programs.review import ScopeAndContext
from programs.review import PerformanceAnalysis
from programs.review import StabilityAnalysis
from programs.review import CorrelationAnalysis
from programs.review import ScoreDistributionAnalysis


Idx = Index('GPS_521_GRILLE_SOF_V1_Calculation_Template_2020.xlsx','1. Index')
Per = Perimeter('GPS_521_GRILLE_SOF_V1_Calculation_Template_2020.xlsx','3. Perimeter of the analysis')
Sum = Summary('GPS_521_GRILLE_SOF_V1_Calculation_Template_2020.xlsx','4. Summary Table')
G = Gini('GPS_521_GRILLE_SOF_V1_Calculation_Template_2020.xlsx','5. GINI')
Cl = ClassificationReport('GPS_521_GRILLE_SOF_V1_Calculation_Template_2020.xlsx','6. Classification report')
Corr = Correlation('GPS_521_GRILLE_SOF_V1_Calculation_Template_2020.xlsx','7. Correlation analysis')
O = Overrides('GPS_521_GRILLE_SOF_V1_Calculation_Template_2020.xlsx','8. Overrides monitoring')
Sp = ISISvg('GPS_521_GRILLE_SOF_V1_Calculation_Template_2020.xlsx','9.2. IS-ISVG (T-1 vs T)')
Sc = ISISvg('GPS_521_GRILLE_SOF_V1_Calculation_Template_2020.xlsx','9.1. IS-ISVG (Dev vs T)')
Iqs = IQS('GPS_521_GRILLE_SOF_V1_Calculation_Template_2020.xlsx','10.IQS')
SD = ScoreDistribution('GPS_521_GRILLE_SOF_V1_Calculation_Template_2020.xlsx','11.Score distribution')

print('---------- SUCCESS ---------------')
