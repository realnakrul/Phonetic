#!/usr/bin/env python3
from sys import argv
argv.pop(0)
if not argv:
    argv=input('Phrase to spell: ').split()
ALPHABET= {
'a':'(A)lpha',
'b':'(B)ravo',
'c':'(C)harlie',
'd':'(D)elta',
'e':'(E)cho',
'f':'(F)oxtrot',
'g':'(G)olf',
'h':'(H)otel',
'i':'(I)ndia',
'j':'(J)uliett',
'k':'(K)ilo',
'l':'(L)ima',
'm':'(M)ike',
'n':'(N)ovember',
'o':'(O)scar',
'p':'(P)apa',
'q':'(Q)uebec',
'r':'(R)omeo',
's':'(S)ierra',
't':'(T)ango',
'u':'(U)niform',
'v':'(V)ictor',
'w':'(W)hiskey',
'x':'(X)-ray',
'y':'(Y)ankee',
'z':'(Z)ulu'
}
while argv:
    print('-'*20)
    print(str(argv[0]))
    for LETTER in argv[0].lower():
        print('\t'+ALPHABET[LETTER])
    argv.pop(0)
    input('\nPress Enter to continiue...')
