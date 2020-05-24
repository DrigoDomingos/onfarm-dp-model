# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:49:12 2020

@author: Rodrigo
"""

############################## etapa 1 azul_claro  #####################################################

###################  azul_claro_aglomerados
#path = "C:\\Users\\Rodrigo\\Desktop\\PROJETOS\\ONFARM\\01_fotos_separadas\\et1-azul_claro_aglomerados\\"
#bacteria = "et1-azul_claro_aglomerados_"


###################  azul_claro_isoladas
#path = "C:\\Users\\Rodrigo\\Desktop\\PROJETOS\\ONFARM\\01_fotos_separadas\\et1-azul_claro_isoladas\\"
#bacteria = "et1-azul_claro_isoladas_"

###################  azul_claro_colonias
#path = "C:\\Users\\Rodrigo\\Desktop\\PROJETOS\\ONFARM\\01_fotos_separadas\\et1-azul_claro_colonias\\"
#bacteria = "et1-azul_claro_colonias_"

#########################################################################################################


############################## etapa 1 azul_escuro  #####################################################

###################  azul_escuro_aglomerados
#path = "C:\\Users\\Rodrigo\\Desktop\\PROJETOS\\ONFARM\\01_fotos_separadas\\et1-azul_escuro_aglomerados\\"
#bacteria = "et1-azul_escuro_aglomerados_"


###################  azul_escuro_isoladas
#path = "C:\\Users\\Rodrigo\\Desktop\\PROJETOS\\ONFARM\\01_fotos_separadas\\et1-azul_escuro_isoladas\\"
#bacteria = "et1-azul_escuro_isoladas_"

###################  azul_escuro_colonias
#path = "C:\\Users\\Rodrigo\\Desktop\\PROJETOS\\ONFARM\\01_fotos_separadas\\et1-azul_escuro_colonias\\"
#bacteria = "et1-azul_escuro_colonias_"

#########################################################################################################



############################## etapa 2 roxo  ############################################################

###################  roxo_aglomerados
#path = "C:\\Users\\Rodrigo\\Desktop\\PROJETOS\\ONFARM\\01_fotos_separadas\\et2-roxo_aglomerados\\"
#bacteria = "et2-roxo_aglomerados_"


###################  roxo_isoladas
#path = "C:\\Users\\Rodrigo\\Desktop\\PROJETOS\\ONFARM\\01_fotos_separadas\\et2-roxo_isoladas\\"
#bacteria = "et2-roxo_isoladas_"

###################  roxo_colonias
#path = "C:\\Users\\Rodrigo\\Desktop\\PROJETOS\\ONFARM\\01_fotos_separadas\\et2-roxo_colonias\\"
#bacteria = "et2-roxo_colonias_"

##########################################################################################################
        
        
from PIL import Image
import random
import os

rotate_list = [0,45,90,180,270]
 
for fichier in os.listdir(path):
    full_filename = str(path) + fichier
    print(full_filename)
    colorImage  = Image.open(full_filename)
     
    rotated     = colorImage.rotate(random.choice(rotate_list))
     
    
    rotated.save(full_filename)