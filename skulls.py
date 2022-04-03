#private da Skull's society 404

import os
import time
import sys

#collors
Azul = '\033[94m'
Verde = '\033[92m'
Amarelo = '\033[93m'
Vermelho = '\033[91m'
Fim = '\033[0m'

#collors2
w = "\033[90;1m"
m = "\033[91;1m"
h = "\033[92;1m"
k = "\033[93;1m"
b = "\033[94;1m"
p = "\033[95;1m"
a = "\033[96;1m"
s = "\033[97;1m"

#time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#requisitos
os.system('pkg install ruby cowsay toilet figlet')
os.system('gem install lolcat')

#banner
os.system("clear")
print '''\033[92m"!                                    @@@@@##!:.
                                  !@@@@@@@@@@@@@@@#.
                              .@@@!  !@@@@@@@@@@@@@@@@@#
                   :#@@@!     .@@@:  !@@@@@@#  :#@@@@@@@@@#.
                  !@@@@@@@@@@@@@@@:              :@@@@@@@@@@@#
                   !@@@@@@@@@#!:..#@#!:.        :@@@@@@@@@@@@@@#
          .@@@@!#@@@@@@@#.        !@@@@@@@@#.      :@@:. #@@@@@@@:
         #@@@@@@@@@@@@:           !@@@@@@@@@@@:           .@@@@@@@#
           :#@@@@@@@@.            !@@@@@@@@@@@@#       .#@@@@@@@@@@!
           :@@@@@@@@#             !@@@@@@@@@@@@@.       !@@@@@@@@@@@.
      :##@@@@@@@@@@@@:            !@@@@@@@@@@@@!         ::::!@@@@@@!
      !@@@@@@@@@@@@@@@:           !@@@@@@@@@@@:              .@@@@@@#
      :####@@@@@@@@@@@!           !@@@@@@@@@@@:          !!!!#@@@@@@!
           .@@@@@@@@@.  :@@@@@@@: #@:       !@@#        !@@@@@@@@@@@.
           :#@@@@@@@@@:   :..    ::#@@@@###@@@:        .#@@@@@@@@@@!
         #@@@@@@@@@@@@@#. .:.   :!!:#@@@@#@@#.            .@@@@@@@#
           @@@@:!@@@@@@@@@@.      !@@@@@@!         !@@!  #@@@@@@@:
                   :@@@@@@@::#::!:!!.!!:!!      :@@@@@@@@@@@@@@#
                  #@@@@@@@@@@@@@@@:      .:.     .@@@@@@@@@@@#
                   .!@@@!     .@@@:  !@@@@@@# .!@@@@@@@@@@#.
                              .@@@!..!@@@@@@@@@@@@@@@@@!
                                  !@@@@@@@@@@@@@@@!.
                                  !@@@@##!:.\033[0m
'''
#letreiro
os.system('toilet -f standard "SKULLS" -F gay')
os.system('toilet -f standard "SOCIETY" -F gay')
print '''
___________________________________________
|                                          |
|      https://github.com/DiosDeLaWeb      |  [ 1 ] achar vulnerabilidades
|__________________________________________|
|                               |   Bem    |  [ 2 ] password hack
|  Codded by : Dios De la Web   |  vindo   |
|  Team : Skulls Society 404    |   esse   |  [ 3 ] hack cam
|  Lema : o enter faz a forca a |  script  |
|  uniao faz os hackers         |  e dos   |  [ 4 ] attack ddos/dos
|                               |  skulls  |    
|  SCRIPT PRIVATE DOS SKULLS    | society  |  [ 5 ] instalar todas
|_______________________________|__________|
                                [ 6 ] sair
'''
opcao = inp(input("NUMERO :"))

if opcao == 1:
    os.system("clear")
    os.system('toilet -f standard "SCANNERS" -F gay')
elif opcao == 2:
    os.system("clear")
    os.system('toilet -f standard "PASSW" -F gay')
elif opcao == 3:
    os.system("clear")
    os.system('toilet -f standard "cam hack" -F gay')
elif opcao == 4:
    os.system("clear")
    os.system('toilet -f standard "DDOS" -F gay')
elif opcao == 5:
    os.system("cleaf")
    os.system('toilet -f standard "TODAS" -F gay')
    print "[ + ] Preparando para instalar as ferramentas"
    time.sleep(2)
    print "[ + ] Lendo arquivos"
    time.sleep(2)
    print "[ + ] Comecando"
    time.sleep(1)
    os.system("figlet figlet")
    os.system("apt install figlet")
    os.system('toilet -f standard "FERRAMENTAS" -F gay')
    os.system('toilet -f standard "SKULLS" -F gay')
    os.system("figlet dios ddos")
    os.system("git clone https://github.com/DiosDeLaWeb/Dios-DDos")
    os.system("figlet person dios")
    os.system("git clone https://github.com/DiosDeLaWeb/Person-Dios")
    os.system("figlet scripts dios")
    os.system("git clone https://github.com/DiosDeLaWeb/Dios-Scripts")
    os.system('toilet -f standard "FIM" -F gay')
    os.system("figlet sqlmap")
    os.system("git clone https://github.com/sqlmapproject/sqlmap")
    os.system("figlet brute force")
    os.system("git clone https://github.com/IAmBlackHacker/Facebook-BruteForce")
    os.system("figlet lazymux")

elif opcao == 6:
    print "fechando ferramenta"
    time.sleep(2)
    exit()
 
else:
    print "opcao invalida"
