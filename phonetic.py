#!/usr/bin/env python3
from sys import argv


ALPHABET = {
    'a': '(A)lpha',
    'b': '(B)ravo',
    'c': '(C)harlie',
    'd': '(D)elta',
    'e': '(E)cho',
    'f': '(F)oxtrot',
    'g': '(G)olf',
    'h': '(H)otel',
    'i': '(I)ndia',
    'j': '(J)uliett',
    'k': '(K)ilo',
    'l': '(L)ima',
    'm': '(M)ike',
    'n': '(N)ovember',
    'o': '(O)scar',
    'p': '(P)apa',
    'q': '(Q)uebec',
    'r': '(R)omeo',
    's': '(S)ierra',
    't': '(T)ango',
    'u': '(U)niform',
    'v': '(V)ictor',
    'w': '(W)hiskey',
    'x': '(X)-ray',
    'y': '(Y)ankee',
    'z': '(Z)ulu',
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '!': 'Exclamation mark',
    '"': 'Quotation mark (double quote)',
    '#': 'Hash sign (pound or number sign)',
    '$': 'Dollar sign',
    '%': 'Percent sign',
    '&': 'Ampersand',
    '\'': 'Apostrophe (single quote)',
    '(': 'Open parenthesis (left round bracket)',
    ')': 'Close parenthesis (right round bracket)',
    '*': 'Asterisk (star sign)',
    '+': 'Plus sign',
    ',': 'Comma',
    '-': 'Dash (minus sign)',
    '.': 'Dot (period or decimal point)',
    '/': 'Slash (forward slash)',
    ':': 'Colon',
    ';': 'Semicolon',
    '<': 'Less than sign',
    '>': 'Greater than sign',
    '=': 'Equal sign',
    '?': 'Question mark',
    '@': 'At sign',
    '[': 'Open bracket (left square bracket)',
    ']': 'Close bracket (right square bracket)',
    '\\': 'Backslash',
    '^': 'Caret',
    '_': 'Underscore (underline)',
    '`': 'Backquote (left single quote)',
    '{': 'Open brace (left curly bracket)',
    '}': 'Close brace (right curly bracket)',
    '|': 'Pipe (vertical bar)',
    '~': 'Tilde'
    }


def spell_word(word_to_spell):
    print(word_to_spell)
    print('-' * 40)
    for letter in word_to_spell.lower():
        print(letter + '\t' + ALPHABET[letter])


def get_phrase(arguments):
    result = arguments[1:]
    if not result:
        result = input('Type phrase to spell: ').split()
    return result


if __name__ == '__main__':
    phrase = get_phrase(argv)
    for word in phrase:
        spell_word(word)
        input('\nPress ENTER to continue...')
