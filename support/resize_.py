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
        
        
import os
import cv2
 
for fichier in os.listdir(path):
    full_filename = str(path) + fichier
    print(full_filename)
    img = cv2.imread(full_filename, cv2.IMREAD_UNCHANGED)
     
    print('Original Dimensions : ',img.shape)
     
    scale_percent = 220 # percent of original size
    width = 416 #int(img.shape[1] * scale_percent / 100)
    height = 416#int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
     
    print('Resized Dimensions : ',resized.shape)
    
    cv2.imwrite(full_filename,resized)