#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Print the acknowledgements sentence with all the project references!
See acknowledgements.py -h or run acknowledgements.py ? for help or simply use as 
acknowledgements.py Author1 Author2
"""

import sys
import pprint
from collections import OrderedDict
import argparse
import textwrap


name = 'acknowledgements'
FCT = r'Funda\c{c}\~ao para a Ci\^encia e a Tecnologia (FCT, Portugal)'
FEDER = r'FEDER - Fundo Europeu de Desenvolvimento Regional'
COMPETE2020 = r'COMPETE2020 - Programa Operacional Competitividade e Internacionaliza\c{c}\~ao'


def from_tex(s):
    s = s.replace(r'\c{c}', 'ç')
    s = s.replace(r'\~a', 'ã')
    s = s.replace(r'\^e', 'ê')
    return s


def _parser():
    parser = argparse.ArgumentParser(description='Print %s' % name)
    parser.add_argument('authors', metavar='authors', type=str, nargs='+',
                        help='authors for the current paper')
    parser.add_argument('--sort', dest='sortalpha', action='store_true',
                        default=False,
                        help='sort the authors alphabetically?')
    parser.add_argument('--notex', action='store_true', default=False,
                        help='no LaTeX output')
    parser.add_argument('-w', '--width', type=int, default=80,
                        help='width of lines in output (default=80)')
    parser.add_argument('--noGEANES', action='store_true', default=False,
                        help='remove G.EANES project from acknowledgements')
    parser.add_argument('--noEPIC', action='store_true', default=False,
                        help='remove EPIC project from acknowledgements')

    args = parser.parse_args()
    # print args
    return args

def comma_separator(sequence):
    if not sequence:
        return ''
    if isinstance(sequence, dict):
        sequence = list(sequence.values())
    if len(sequence) == 1:
        return sequence[0]
    return '{} and {}'.format(', '.join(sequence[:-1]), sequence[-1])

flatten = lambda l: [item for sublist in l for item in sublist]


def justy(text, width=80, ret=False):
    """ Print text limiting the number of characters per line to `width` """
    broken = textwrap.wrap(text, width, break_long_words=False)
    if ret:
        return '\n'.join(broken)
    else:
        print('\n'.join(broken))


def individual(initials, normal=True, dl57=False, ifct=False, width=80, ret=False):
    if dl57 or ifct:
        normal = False

    if len(initials) > 0:
        if len(initials) == 1:
            t1, t2, t3, t4 = 'is', 'acknowledges', 'contract', 'reference'
            te = 'a'
        else:
            t1, t2, t3, t4 = 'are', 'acknowledge', 'contracts', 'references'
            te = ''

        if normal:
            msg = comma_separator(list(initials.keys())) + ' '
            msg += f'{t2} support from FCT through {t3} with {t4} '
            msg += comma_separator(flatten(list(initials.values())))
        elif dl57:
            msg = comma_separator(list(initials.keys())) + ' '
            msg += f'{t1} supported in the form of {te} work {t3} funded by national funds through FCT with {t4} '
            msg += comma_separator(flatten(list(initials.values())))
        elif ifct:
            msg = comma_separator(list(initials.keys())) + ' '
            msg += f'{t2} support from FCT through Investigador FCT {t3} '
            msg += comma_separator(flatten(list(initials.values())))
    
        if ret:
            return msg + '. '
        else:
            justy(msg + '. ', width)
    
    return ''



IA_akn = {
    'IA': 'UID/FIS/04434/2019',
}


team_akn = {
    'GEANES': 'PTDC/FIS-AST/32113/2017 & POCI-01-0145-FEDER-032113',
    'EPIC': 'PTDC/FIS-AST/28953/2017 & POCI-01-0145-FEDER-028953',
}

    # 'UID/FIS/04434/2013',
    # 'POCI-01-0145-FEDER-007672',
    # 'PTDC/FIS-AST/1526/2014',
    # 'POCI-01-0145-FEDER-016886'

Vardan_project = [
    'PTDC/FIS-AST/7073/2014',
    'POCI-01-0145-FEDER-016880',
]

acknow = {
('Elisa Delgado Mena', 'E.D.M.', 'Elisa')               : ['IF/00849/2015',],
('Gabriella Gilli', 'G.G.', 'Gabriella')                : [],
('Nuno C. Santos', 'N.C.S.', 'Nuno')                    : [], #['IF/00169/2012/CP0150/CT0002',],
('Olivier D. S. Demangeon', 'O.D.', 'Olivier')          : ['DL57/2016/CP1364/CT0004'],
('Pedro Figueira', 'P.F.', 'PedroF')                    : [], #['IF/01037/2013CP1191/CT0001',],
('Pedro Machado', 'P.M.', 'PedroM')                     : [],
('Pedro T. P. Viana', 'P.T.P.V.', 'PedroV')             : [],
('Sérgio A. G. Sousa', 'S.G.S.', 'Sergio')              : ['IF/00028/2014/CP1215/CT0002',],
('Susana C. C. Barros', 'S.C.C.B.', 'Susana')           : ['IF/01312/2014/CP1215/CT0004',],
('Vardan Zh. Adibekyan', 'V.A.', 'Vardan')              : ['IF/00650/2015/CP1273/CT0001'], #['IF/00650/2015',],
# ('Andressa C. S. Ferreira', 'A.C.S.F.', 'Andressa')     : [],
# ('Daniel Thaagaard Andreasen', 'D.T.A.', 'Daniel')      : [],
# ('Jason J. Neal', 'J.J.N.', 'Jason')                    : [],
('João P. S. Faria', 'J.P.F.', 'Faria')                 : ['DL57/2016/CP1364/CT0005'], #['SFRH/BD/93848/2013',],
('João Gomes da Silva', 'J.G.dS.', 'GomesDaSilva')      : [],
('Jorge H. C. Martins', 'J.H.C.M.', 'Jorge')            : ['DL57/2016/CP1364/CT0007'],
('Luisa M. Serrano', 'L.M.S.', 'Luisa')                 : ['SFRH/BD/120518/2016'],
('Pedro I. T. K. Sarmento', 'P.I.T.K.S.', 'PedroS')     : [],
('Ruben Gonçalves', 'R.G.', 'Ruben')                    : [],
('Saeed Hojjatpanah', 'S.H.', 'Saeed')                  : [],
('Solène C. Ulmer-Moll', 'S.C.M.', 'Solene')            : [],
}


DL57 = ('Olivier', 'Faria', 'Jorge')
iFCT = ('Sergio', 'Susana', 'Vardan')


def acknowledgements(authors, noGEANES=False, noEPIC=False, notex=False, width=80):
    # build a dict with the acknowledgements for these authors only
    ThisPaperAcknow = OrderedDict()
    for author in authors:
        for k,v in acknow.items():
            if author in k:
                ThisPaperAcknow[k] = v

    # print the damn thing!!!
    # print('\n\n')
    # print(name)
    # print('='*len(name) + '\n')

    if noGEANES:
        team_akn.pop('GEANES')
    if noEPIC:
        team_akn.pop('EPIC')
    projects = {**IA_akn, **team_akn}

    if notex:
        detex = from_tex
    else:
        detex = lambda x: x

    msg = 'This work was supported by %s through national funds ' % detex(FCT)
    msg += f'and by {detex(FEDER)} '
    msg += f'through {detex(COMPETE2020)} '
    if len(projects) == 1:
        msg += 'by the grant '
    else:
        msg += 'by these grants: '
    # final = justy(msg, width, ret=True)

    if 'Vardan' in authors:
        msg += comma_separator(team_akn + Vardan_project) + '. '
    else:
        msg += comma_separator(projects) + '. '

    initials = [n[1] for n in list(ThisPaperAcknow.keys())]
    dl57 = {}
    ifct = {}
    other = {}
    for i, (initial, (k,v)) in enumerate(zip(initials, list(ThisPaperAcknow.items()))):
        if k[2] in DL57:
            dl57[initial] = v
        elif k[2] in iFCT:
            ifct[initial] = v
        else:
            if v:
                other[initial] = v
        # if len(v)==0: 
        #     initials.pop(i)
        #     ThisPaperAcknow.pop(k)

    msg += '\n'
    msg += individual(dl57, dl57=True, width=width, ret=True)
    msg += individual(ifct, ifct=True, width=width, ret=True)
    msg += individual(other, width=width, ret=True)

    return msg



if __name__ == '__main__':

    args = _parser()
    print(args)
    list_authors = args.authors


    if '?' in list_authors:
        print('Possible names for authors are (space-separated):')
        [print('  ' + n[2]) for n in list(acknow.keys())]
        sys.exit(0)



    print('There are %d team members with known %s' % (len(acknow), name))
    nauthors = len(list_authors)
    if nauthors == 1:
        print('There is 1 author:')
    else:
        print('There are %d authors:' % len(list_authors))
    print(list_authors)


    # should we sort alphabetically?
    # otherwise use the same order as input
    if args.sortalpha:
        print('Sorting authors alphabetically by first name:')
        list_authors = sorted(list_authors)
        print(list_authors)


    # build a dict with the acknowledgements for these authors only
    ThisPaperAcknow = OrderedDict()
    for author in list_authors:
        for k,v in acknow.items():
            if author in k:
                ThisPaperAcknow[k] = v



    # print the damn thing!!!
    print('\n\n')
    print(name)
    print('='*len(name) + '\n')

    if args.noGEANES:
        team_akn.pop('GEANES')
    if args.noEPIC:
        team_akn.pop('EPIC')
    projects = {**IA_akn, **team_akn}

    if args.notex:
        pass
    else:
        from_tex = lambda x: x


    msg = 'This work was supported by %s through national funds ' % from_tex(FCT)
    msg += f'and by {from_tex(FEDER)} '
    msg += f'through {from_tex(COMPETE2020)} '
    if len(projects) == 1:
        msg += 'by the grant '
    else:
        msg += 'by these grants: '
    justy(msg, args.width)


    if 'Vardan' in list_authors:
        justy(comma_separator(team_akn + Vardan_project) + '.', args.width)
    else:
        justy(comma_separator(projects) + '.', args.width)


    initials = [n[1] for n in list(ThisPaperAcknow.keys())]
    dl57 = {}
    ifct = {}
    other = {}
    for i, (initial, (k,v)) in enumerate(zip(initials, list(ThisPaperAcknow.items()))):
        if k[2] in DL57:
            dl57[initial] = v
        elif k[2] in iFCT:
            ifct[initial] = v
        else:
            if v:
                other[initial] = v
        # if len(v)==0: 
        #     initials.pop(i)
        #     ThisPaperAcknow.pop(k)

    # do the DL57
    # print()
    individual(dl57, dl57=True, width=args.width)

    # do the iFCT
    # print()
    individual(ifct, ifct=True, width=args.width)

    # do the rest
    # print()
    individual(other, width=args.width)
    
    # if len(initials) > 0:
    #     if len(initials) == 1:
    #         t1 = 'acknowledges'
    #         t2 = 'the contract'
    #     else:
    #         t1 = 'acknowledge'
    #         t2 = 'contracts'
    #     print(comma_separator(initials) + ' ' + \
    #           'further %s support from FCT through %s\n' % (t1, t2) + \
    #           comma_separator(flatten(list(ThisPaperAcknow.values()))))

    sys.exit(0)
    print('\n\n')
    print('#'*10)
    print('OR')
    print('#'*10)
    print('\n\n')


    # print('The Porto group acknowledges the support from %s' % FCT)
    # print('through national funds and from FEDER through COMPETE2020 by the following grants:')

    # if 'Vardan' in list_authors:
    #     print(comma_separator(team_akn + Vardan_project) + '.')
    # else:
    #     print(comma_separator({**IA_akn, **team_akn}) + '.')


    # initials = [n[1] for n in list(ThisPaperAcknow.keys())]
    # for i, (initial, (k,v)) in enumerate(zip(initials, list(ThisPaperAcknow.items()))):
    #     if len(v)==0: 
    #         initials.pop(i)
    #         ThisPaperAcknow.pop(k)


    # if len(initials) > 0:
    #     if len(initials) == 1:
    #         t1 = 'acknowledges'
    #         t2 = 'the contract'
    #     else:
    #         t1 = 'acknowledge'
    #         t2 = 'contracts'
    #     print(comma_separator(initials) + ' ' + \
    #           'further %s support from FCT through %s\n' % (t1, t2) + \
    #           comma_separator(flatten(list(ThisPaperAcknow.values()))))

