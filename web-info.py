print("\033[92m")
print
print
print
print
print
print
print
print
print
print("__________________________________________________________")
print
print("""__    __    ___  ____         ____  ____   _____   ___  
|  |__|  |  /  _]|    \       |    ||    \ |     | /   \ 
|  |  |  | /  [_ |  o  ) _____ |  | |  _  ||   __||     |
|  |  |  ||    _]|     ||     ||  | |  |  ||  |_  |  O  |
|  `  '  ||   [_ |  O  ||_____||  | |  |  ||   _] |     |
 \      / |     ||     |       |  | |  |  ||  |   |     |
  \_/\_/  |_____||_____|      |____||__|__||__|    \___/ 
                                                         """)
print
print("__________________________________________________________")
print
print("""DEVELOPED BY : RANAJIT SINGHA (M:8348932574)""")
print
print
print
import os
import urllib2
import sys
url = raw_input("ENTER WEBSITE LINK : ")
url.rstrip ( )
header =urllib2.urlopen (url) .info ( )
print(str (header) )
print
print
print("""THANK YOU""")
print
print
print
