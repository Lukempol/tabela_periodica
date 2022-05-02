from collections import namedtuple
from pprint import pprint

nomes = '''
hidrogênio hélio 
lítio berílio boro carbono nitrogênio oxigênio flúor neônio
sódio magnésio alumínio silício fósforo enxofre cloro argônio
potássio cálcio escândio titânio vanádio cromo manganês ferro 
cobalto níquel cobre zinco gálio germânio arsênio selênio bromo criptônio
rubídio estrôncio ítrio zircônio nióbio molibdênio tecnécio rutênio ródio
paládio prata cádmio índio estanho antimônio telúrio iodo xenônio
césio bário lantânio cério praseodímio neodímio promécio samário európio
gadolínio térbio disprósio hólmio érbio túlio itérbio lutécio háfnio tântalo tungstênio
rênio ósmio irídio platina ouro mercúrio tálio chumbo bismuto polônio ástato radônio
frâncio rádio actínio tório protactínio urânio netúnio plutônio amerício cúrio berquélio
califórnio einsténio férmio mendelévio nobélio laurêncio rutherfórdio dúbnio seabórgio
bóhrio hássio meitnério darmstádio roetgênio copernício nohômio fleróvio moscóvio  livermório  tenessino oganessônio
'''.split()

simbolos = '''
H He Li Be B C N O F Ne 
Na Mg Al Si P S Cl Ar
K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe
Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf 
Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf 
Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og
'''.split()

Elemento = namedtuple( 'Elemento', 'nome simbolo n')
tabela = []
for n, elemento in enumerate(zip(nomes, simbolos), 1):
    tabela.append(Elemento(elemento[0] , elemento[1], n))
