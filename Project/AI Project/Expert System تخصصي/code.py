# -*- coding: utf-8 -*-
"""Copy of uniCode2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uqnzgmP_dOEmwT4OW1X2JaXXGl4V3xxJ
"""

! pip install experta

from experta import *
class uni(Fact):
  pass
#=================TABUK=============================
class myUniversity(KnowledgeEngine):
  @Rule(OR(AND( uni(D=('b') ),  uni(city=('t')),uni(gender=('f')),uni(major=('cs'))),AND( uni(D=('b') ),  uni(city=('t')),uni(gender=('m')),uni(major=('cs'))),AND( uni(D=('m') ),  uni(city=('t')),uni(gender=('f')),uni(major=('ai'))),AND( uni(D=('m') ),  uni(city=('t')),uni(gender=('m')),uni(major=('ai'))),AND( uni(D=('m') ),  uni(city=('t')),uni(gender=('f')),uni(major=('s'))),AND( uni(D=('m') ),  uni(city=('t')),uni(gender=('male')),uni(major=('s'))),AND( uni(D=('m') ),  uni(city=('t')),uni(gender=('f')),uni(major=('d'))),AND( uni(D=('m') ),  uni(city=('t')),uni(gender=('f')),uni(major=('d')))))
  def Tabuk_University(self):
    print("Tabuk University")



#=================Arar=============================
  @Rule(OR(AND( uni(D=('b') ),  uni(city=('ar')),uni(gender=('f')),uni(major=('cs'))),AND( uni(D=('b') ),  uni(city=('ar')),uni(gender=('m')),uni(major=('cs')))))
  def Northern_Borders_University(self):
    print("Northern Boroders University")   


#=================hail=============================
  @Rule(OR(AND( uni(D=('b') ),  uni(city=('h')),uni(gender=('f')),uni(major=('cs'))),AND( uni(D=('b') ),  uni(city=('h')),uni(gender=('m')),uni(major=('cs'))),AND( uni(D=('m') ),  uni(city=('h')),uni(gender=('f')),uni(major=('ai'))),AND( uni(D=('m') ),  uni(city=('h')),uni(gender=('m')),uni(major=('ai'))),AND( uni(D=('m') ),  uni(city=('h')),uni(gender=('f')),uni(major=('s'))),AND( uni(D=('m') ),  uni(city=('h')),uni(gender=('m')),uni(major=('s'))),AND( uni(D=('d') ),  uni(city=('h')),uni(gender=('f')),uni(major=('s'))),AND( uni(D=('d') ),  uni(city=('h')),uni(gender=('m')),uni(major=('s')))))
  def University_of_Hail(self):
    print("University of Hail")


#=================jwaf=============================
  @Rule(OR(AND( uni(D=('d') ),  uni(city=('j')),uni(gender=('f')),uni(major=('n'))),AND( uni(D=('d') ),  uni(city=('j')),uni(gender=('m')),uni(major=('n'))),AND( uni(D=('d') ),  uni(city=('j')),uni(gender=('f')),uni(major=('d'))),AND( uni(D=('d') ),  uni(city=('j')),uni(gender=('m')),uni(major=('d'))),AND( uni(D=('b') ),  uni(city=('j')),uni(gender=('f')),uni(major=('cs'))),AND( uni(D=('b') ),  uni(city=('j')),uni(gender=('m')),uni(major=('cs'))),AND( uni(D=('b') ),  uni(city=('j')),uni(gender=('f')),uni(major=('se'))),AND( uni(D=('b') ),  uni(city=('j')),uni(gender=('m')),uni(major=('se'))),AND( uni(D=('m') ),  uni(city=('j')),uni(gender=('f')),uni(major=('d'))),AND( uni(D=('m') ),  uni(city=('j')),uni(gender=('m')),uni(major=('d'))),AND( uni(D=('m') ),  uni(city=('j')),uni(gender=('f')),uni(major=('ai'))),AND( uni(D=('m') ),  uni(city=('j')),uni(gender=('m')),uni(major=('ai'))),AND( uni(D=('m') ),  uni(city=('j')),uni(gender=('f')),uni(major=('s'))),AND( uni(D=('m') ),  uni(city=('j')),uni(gender=('m')),uni(major=('s')))))
  def Al_Jawf_University(self):
    print("Al Jawf University")


#=================Najran===========================
  @Rule(OR(AND( uni(D=('b') ),  uni(city=('n')),uni(gender=('f')),uni(major=('cs'))),AND( uni(D=('b') ),  uni(city=('n')),uni(gender=('m')),uni(major=('cs')))))
  def Najran_University(self):
    print("Najran University")


#==========Baha===================  

  @Rule(OR(AND( uni(D=('b') ),  uni(city=('ba')),uni(gender=('f')),uni(major=('cs'))),AND( uni(D=('b') ),  uni(city=('ba')),uni(gender=('m')),uni(major=('cs'))),AND(uni(D=('m')),uni(city=('ba')),uni(gander=('f')),uni(major=('ai'))),AND(uni(D=('m')),uni(city=('ba')),uni(gander=('m')),uni(major=('ai'))),AND(uni(D=('m')),uni(city=('ba')),uni(gander=('m')),uni(major=('s')))))
  def AlBaha_University(self):
    print("Al-Baha University")

#=================jazan============================
  @Rule(OR(AND( uni(D=('d') ),  uni(city=('jz')),uni(gender=('f')),uni(major=('cs'))),AND( uni(D=('d') ),  uni(city=('jz')),uni(gender=('m')),uni(major=('cs'))),AND( uni(D=('b') ),  uni(city=('jz')),uni(gender=('f')),uni(major=('cs'))),AND( uni(D=('b') ),  uni(city=('jz')),uni(gender=('m')),uni(major=('cs')))))
  def Jazan_University(self):
    print("Jazan University")    


#=================abha==============================
  @Rule(OR(AND( uni(D=('d') ),  uni(city=('ab')),uni(gender=('m')),uni(major=('n'))),AND( uni(D=('d') ),  uni(city=('ab')),uni(gender=('f')),uni(major=('p'))),AND( uni(D=('d') ),  uni(city=('ab')),uni(gender=('m')),uni(major=('p'))),AND( uni(D=('b') ),  uni(city=('ab')),uni(gender=('f')),uni(major=('cs'))),AND( uni(D=('b') ),  uni(city=('ab')),uni(gender=('m')),uni(major=('cs'))),AND( uni(D=('m') ),  uni(city=('ab')),uni(gender=('f')),uni(major=('cs'))),AND( uni(D=('m') ),  uni(city=('ab')),uni(gender=('m')),uni(major=('cs'))),AND( uni(D=('m') ),  uni(city=('ab')),uni(gender=('f')),uni(major=('s'))),AND( uni(D=('m') ),  uni(city=('ab')),uni(gender=('m')),uni(major=('s'))),AND( uni(D=('m') ),  uni(city=('ab')),uni(gender=('f')),uni(major=('d'))),AND( uni(D=('m') ),  uni(city=('ab')),uni(gender=('m')),uni(major=('d')))))
  def King_Khalid_University(self):
    print("King Khalid University")

#----------------------------------------------------------------------------------------------------------------------------------

#=================Qassim=============================
  @Rule(OR(AND(uni(gender=('m')), uni(major=('cs')), uni(city=('q')),uni(D=('b'))), AND( uni(gender=('f')), uni (major=('cs')), uni(city=('q')),uni(D=('b'))) ,AND( uni(gender=('m')), uni (major=('cs')), uni(city=('q')),uni(D=('m'))),AND( uni(gender=('f')), uni (major=('cs')), uni(city=('q')),uni(D=('m'))),AND( uni(gender=('m')), uni (major=('n')), uni(city=('q')),uni(D=('m'))),AND( uni(gender=('f')), uni (major=('n')),  uni(city=('q')),uni(D=('m')))))
  def QassimUni(self): 
    print("Qassim university")
  

#=================#Eastern Province=============================
  @Rule(OR(AND(uni(gender=('m')), uni(major=('ai')),uni(city=('e')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('ai')),  uni(city=('e')),uni(D=('b'))),AND( uni(gender=('m')), uni (major=('cs')),  uni(city=('e')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('cs')),   uni(city=('e')),uni(D=('b'))),AND( uni(gender=('m')), uni (major=('s')),  uni(city=('e')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('s')),  uni(city=('e')),uni(D=('b'))),AND( uni(gender=('m')), uni (major=('cs')),  uni(city=('e')),uni(D=('m'))),AND( uni(gender=('f')), uni (major=('cs')),       uni(city=('e')),uni(D=('m')))))
  def ima_Abdulrahman(self): 
    print("imam Abdulrahman bin Faisal university")  
 
  @Rule(OR(AND( uni(gender=('m')), uni (major=('ai')), uni(city=('e')),uni(D=('m'))), AND( uni(gender=('f')), uni (major=('ai')),  uni(city=('e')),uni(D=('m'))),AND( uni(gender=('m')), uni (major=('s')),  uni(city=('e')),uni(D=('m'))),AND( uni(gender=('f')), uni (major=('s')),   uni(city=('e')),uni(D=('m'))),AND( uni(gender=('m')), uni (major=('e')),   uni(city=('e')),uni(D=('m'))),AND( uni(gender=('f')), uni (major=('e')),  uni(city=('e')),uni(D=('m'))),AND( uni(gender=('m')), uni (major=('n')),  uni(city=('e')),uni(D=('m'))),AND( uni(gender=('f')), uni (major=('n')),  uni(city=('e')),uni(D=('m'))),AND( uni(gender=('m')), uni (major=('n')),  uni(city=('e')),uni(D=('p'))),AND( uni(gender=('f')), uni (major=('n')), uni(city=('e')),uni(D=('p'))),AND( uni(gender=('m')), uni (major=('cs')),  uni(city=('e')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('cs')),   uni(city=('e')),uni(D=('b'))),AND( uni(gender=('m')), uni (major=('cs')),  uni(city=('e')),uni(D=('m'))),AND( uni(gender=('f')), uni (major=('cs')),       uni(city=('e')),uni(D=('m'))),AND( uni(gender=('m')), uni (major=('e')), uni(city=('e')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('e')), uni(city=('e')),uni(D=('b')))))
  def King_Fahd_University(self): 
    print("King Fahd University of Petroleum & Minerals")
   

    
  @Rule(OR(AND( uni(gender=('m')), uni (major=('s')),  uni(city=('e')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('s')),  uni(city=('e')),uni(D=('b'))),AND( uni(gender=('m')), uni (major=('e')), uni(city=('e')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('e')), uni(city=('e')),uni(D=('b'))),AND( uni(gender=('m')), uni (major=('cs')),  uni(city=('e')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('cs')),   uni(city=('e')),uni(D=('b')))))
  def University_of_Hafr_AlBatin(self): 
    print("University of Hafr Al Batin")
  
  
   
  @Rule(OR(AND( uni(gender=('m')), uni (major=('cs')),  uni(city=('e')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('cs')),   uni(city=('e')),uni(D=('b'))),AND( uni(gender=('m')), uni (major=('e')), uni(city=('e')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('e')), uni(city=('e')),uni(D=('b')))))
  def prince_Mohammad_bin_Fahd_university(self): 
    print("prince Mohammad bin Fahd university ")

   


  @Rule(OR(AND( uni(gender=('m')), uni (major=('n')),  uni(city=('e')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('n')), uni(city=('e')),uni(D=('b'))),AND( uni(gender=('m')), uni (major=('cs')),  uni(city=('e')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('cs')),   uni(city=('e')),uni(D=('b'))),AND( uni(gender=('m')), uni (major=('cs')),  uni(city=('e')),uni(D=('m'))),AND( uni(gender=('f')), uni (major=('cs')),       uni(city=('e')),uni(D=('m'))),AND( uni(gender=('m')), uni (major=('s')),  uni(city=('e')),uni(D=('m'))),AND( uni(gender=('f')), uni (major=('s')),   uni(city=('e')),uni(D=('m')))))
  def King_Faisal_University (self): 
    print("King Faisal University  ")  
   
  
 
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#=================riaydh=============================
#riaydh
  @Rule(OR(AND( uni(gender=('m')), uni (major=('cs')),   uni(city=('r')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('cs')),  uni(city=('r')),uni(D=('b'))),AND( uni(gender=('m')), uni (major=('cs')),  uni(city=('r')),uni(D=('m'))),AND( uni(gender=('f')), uni (major=('cs')), uni(city=('r')),uni(D=('m')))))
  def imam_Muhammad_Saud(self): 
     print("imam Muhammad ibn Saud Islamic university    ")
 
 
  @Rule(OR(AND( uni(gender=('m')), uni (major=('cs')), uni(city=('r')),uni(D=('p'))),AND( uni(gender=('f')), uni (major=('cs')),    uni(city=('r')),uni(D=('p'))),AND( uni(gender=('m')), uni (major=('e')),  uni(city=('r')),uni(D=('m'))),AND( uni(gender=('f')), uni (major=('e')),    uni(city=('r')),uni(D=('m'))),AND( uni(gender=('m')), uni (major=('e')),   uni(city=('r')),uni(D=('p'))),AND( uni(gender=('f')), uni (major=('e')),  uni(city=('r')),uni(D=('p'))),AND( uni(gender=('m')), uni (major=('e')),    uni(city=('r')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('e')),  uni(city=('r')),uni(D=('b'))),AND( uni(gender=('m')), uni (major=('cs')),  uni(city=('r')),uni(D=('m'))),AND( uni(gender=('f')), uni (major=('cs')), uni(city=('r')),uni(D=('m'))),AND( uni(gender=('m')), uni (major=('cs')),   uni(city=('r')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('cs')),  uni(city=('r')),uni(D=('b')))))
  def king_Saud_university(self): 
    print("king Saud university")  
   
  

#-
  @Rule(OR(AND( uni(gender=('m')), uni (major=('ai')),    uni(city=('r')),uni(D=('m'))),AND( uni(gender=('f')), uni (major=('ai')), uni(city=('r')),uni(D=('m'))),AND( uni(gender=('m')), uni (major=('d')),   uni(city=('r')),uni(D=('m'))),AND( uni(gender=('f')), uni (major=('d')),   uni(city=('r')),uni(D=('m'))),AND( uni(gender=('m')), uni (major=('s')),   uni(city=('r')),uni(D=('m'))),AND( uni(gender=('f')), uni (major=('s')),   uni(city=('r')),uni(D=('m'))),AND( uni(gender=('m')), uni (major=('e')),    uni(city=('r')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('e')),  uni(city=('r')),uni(D=('b'))),AND( uni(gender=('m')), uni (major=('cs')),   uni(city=('r')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('cs')),  uni(city=('r')),uni(D=('b')))))
  def prince_Sattam(self): 
    print("prince Sattam bin Abdulaziz university ")  
   


  @Rule(OR(AND(uni(gender='m'), uni(major='p'), uni(city='r'), uni(D='d')),AND(uni(gender='f'), uni(major='cs'), uni(city='r'), uni(D='b')),AND(uni(gender='m'), uni(major='cs'), uni(city='r'), uni(D='b')))
  def The_Majmaah_UnivUniversity(self): 
      print(" Majmaah University ")

  @Rule(OR(AND(uni(gender='f'), uni(major='cs'), uni(city='r'), uni(D='b')),AND(uni(gender='m'), uni(major='cs'), uni(city='r'), uni(D='b')),AND(uni(gender='f'), uni(major='se'), uni(city='r'), uni(D='b')),AND(uni(gender='m'), uni(major='se'), uni(city='r'), uni(D='b'))))
  def Shaqra_UniUniversity(self):
    print(" Shaqra University ")
      
  @Rule(OR(AND(uni(gender='f'), uni(major='p'), uni(city='r'), uni(D='d')),AND(uni(gender='f'), uni(major='cs'), uni(city='r'), uni(D='b')),AND(uni(gender='f'), uni(major='ds'), uni(city='r'), uni(D='b')),AND(uni(gender='f'), uni(major='s'), uni(city='r'), uni(D='b')),AND(uni(gender='f'), uni(major='ai'), uni(city='r'), uni(D='b')),AND(uni(gender='f'), uni(major='ds'), uni(city='r'), uni(D='m'))))
  def Princess_Nourah_UniUniversity (self): 
      print(" Princess Nourah Bint Abdulrahman University ")


#=================Jeddah=============================
  @Rule(OR(AND( uni(D='b'), uni(city='jd'), uni(gender='m'), uni(major='cs')),AND( uni(D='b'), uni(city='jd'), uni(gender='f'), uni(major='cs')),AND( uni(D='m'), uni(city='jd'), uni(gender='f'), uni(major='cs')),AND(uni(degree='m'), uni(city='jd'), uni(gender='m'), uni(major='cs')),AND(uni(degree='p'), uni(city='jd'), uni(gender='f'), uni(major='cs')),AND(uni(degree='p'), uni(city='jd'), uni(gender='m'), uni(major='cs'))))
  def KAU(self): 
      print("King Abdulaziz UnivUniversity ")

 
  @Rule(OR(AND(uni(gender='f'), uni(major='cs'), uni(city='jd'), uni(D='b')) ,AND(uni(gender='f'), uni(major='s'), uni(city='jd'), uni(D='b')) ,AND(uni(gender='f'), uni(major='se'), uni(city='jd'), uni(D='b'))   ,AND(uni(gender='f'), uni(major='n'), uni(city='jd'), uni(D='b'))  ,AND(uni(gender='f'), uni(major='cs'), uni(city='jd'), uni(D='m'))  ,AND(uni(gender='m'), uni(major='cs'), uni(city='jd'), uni(D='m'))  ,AND(uni(gender='f'), uni(major='s'), uni(city='jd'), uni(D='m'))  ,AND(uni(gender='m'), uni(major='s'), uni(city='jd'), uni(D='m'))  ,AND(uni(gender='f'), uni(major='ds'), uni(city='jd'), uni(D='m'))  ,AND(uni(gender='m'), uni(major='ds'), uni(city='jd'), uni(D='m'))))
  def Jeddah_UnivUniversity(self): 
      print("Then University Of Jeddah ")

#=================Makkah=============================

  @Rule(OR(AND(uni(gender='f'), uni(major='cs'), uni(city='mk'), uni(D='b')),AND(uni(gender='m'), uni(major='cs'), uni(city='mk'), uni(D='b')),AND(uni(gender='f'), uni(major='ai'), uni(city='mk'), uni(D='m')),AND(uni(gender='m'), uni(major='ai'), uni(city='mk'), uni(D='m')),AND(uni(gender='f'), uni(major='cs'), uni(city='mk'), uni(D='m')),AND(uni(gender='m'), uni(major='cs'), uni(city='mk'), uni(D='m'))))
  def Umm_AlQura_UniUniversity(self):
    print("Then Umm Al-Qura University")


#=================Taif=============================
  @Rule(OR(AND(uni(gender=('m')), uni(major=('cs')), uni(city=('tf')),uni(D=('b'))), AND( uni(gender=('f')), uni (major=('cs')), uni(city=('tf')),uni(D=('b')))))
  def Taif_University(self): 
    print("Taif University ")  
   
#=================Medina=============================
  @Rule(OR(AND(uni(gender=('m')), uni(major=('cs')), uni(city=('md')),uni(D=('b'))), AND( uni(gender=('f')), uni (major=('cs')), uni(city=('md')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('cs')), uni(city=('md')),uni(D=('m'))),AND( uni(gender=('m')), uni (major=('cs')), uni(city=('md')),uni(D=('m')))))
  def Taibah_University(self): 
    print("Taibah University ")  

  @Rule(OR(AND(uni(gender=('m')), uni(major=('cs')), uni(city=('md')),uni(D=('b'))), AND( uni(gender=('f')), uni (major=('cs')), uni(city=('md')),uni(D=('b'))),AND( uni(gender=('f')), uni (major=('d')), uni(city=('md')),uni(D=('m'))),AND( uni(gender=('f')), uni (major=('d')), uni(city=('md')),uni(D=('m')))))
  def IslamicUniversityofMadinah(self): 
    print("Islamic University of Madinah")  


print("****************** Wellcome to تخصصي expert System that will help you to chose a university ******************")
n=int(input("\n\n> To start Enter 1 \n  exit Enter 0\n"))
while n > 0: 
  engine=myUniversity()
  engine.reset()
  engine.declare(uni(D=input("\n> What dgree do you want ?  \n\n d for Diploma | b for Bachelor | m for master | p for Phd \n  "),city=input("\n> Where are you from ? \n \n r for Riaydh | mk for makkah | jd for Jeddah | md for Medina | tf for taif \n  e for Eastern region | t for Tabuk | ar for Arara | h for Hail | j for Al-Jwaf \n | n for Najran | ba for Al-Baha  | jz for Jazan | ab for Abha | Q for Qassim  \n "),gender=input("\n>Enter Your gender \n\n f for Female |m for male\n  "),major=input("\n>what major do you want  \n\n  n for Networking | p for programing | cs for computer science \n | d for Data Science  | ai for artificial intelligence | s for Cyber security | se for Software engineering \n  ")))
  print("The university recommended for you is")
  engine.run()
  n=int(input("> To start Enter 1 \n  exit Enter 0\n"))
print("Thank you <3")