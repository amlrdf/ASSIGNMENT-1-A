list_of_protein_dicts = [{'seq': 'ACACIMED', 'ch': 2},
                         {'seq': 'ELEMYRATNE', 'ch': 1},
                         {'seq': 'wapwop', 'ch': 3},
                         {'seq': 'zeittsieg', 'ch': 2},
                         {'seq': 'DESFBIRC', 'ch': 1},
                         {'seq': 'altaatsiv', 'ch': 3},
                         {'seq': 'MEINWOHC', 'ch': 2}]
# mass(A) = 71.03711360
# mass(C) = 103.0091854
# mass(D) = 115.0269428
# mass(E) = 129.0425928
# mass(F) = 147.0684136
# mass(G) = 57.02146360
# mass(H) = 137.0589116
# mass(I) = 113.0840636
# mass(K) = 128.0949626
# mass(L) = 113.0840636
# mass(M) = 131.0404854
# mass(N) = 114.0429272
# mass(P) = 97.05276360
# mass(Q) = 128.0585772
# mass(R) = 156.1011106
# mass(S) = 87.03202820
# mass(T) = 101.0476782
# mass(V) = 99.06841360
# mass(W) = 186.0793126
# mass(Y) = 163.0633282

def Split_check_cal(mass_dict,list_of_protein_dicts):
    # This function splitting-->individual code (double splitting)
    # Validating codes of protein-->printing 'invalidation'
    # Calculating the mass and m/z
    # Inputting mass_dict of individual code and formatted protein data
    # Outputting the list_of_protain_dicts for display in a good format
    for ele in list_of_protein_dicts:
        for indv in list(ele['seq']):
            if indv in list(mass_dict.keys()):
                ele['mass'] += mass_dict[indv]
                ele['m/z'] = ele['mass']/ele['ch']
            else:
                ele['mass'] = 'invalid sequence'
                ele['m/z'] = 'invalid sequence'
                ele['ch'] = 'invalid sequence'
                break
    return list_of_protein_dicts
def Printing(list_of_protein_dicts):
    import pprint
    print('Table of Protein & Info')
    print('-----------'*10)
    for ele in list_of_protein_dicts:
        print('seq: {}\t\t mass_of_protein: {}\t\t m/z: {}\t\t'.format(ele['seq'],ele['mass'],ele['m/z']))
def Init(list_of_protein_dicts):
    # INPUT: a list of protein data (seq & charge);
    # OUTPUT: dictionary of mass, control_list of protein data(seq, mass, m/z, charge)
    mass_dict={'A':71.03711360,
               'C':103.0091854,
               'D':115.0269428,
               'E':129.0425928,
               'F':147.0684136,
               'G':57.02146360,
               'H':137.0589116,
               'I':113.0840636,
               'K':128.0949626,
               'L':113.0840636,
               'M':131.0404854,
               'N':114.0429272,
               'P':97.05276360,
               'Q':128.0585772,
               'R':156.1011106,
               'S':87.03202820,
               'T':101.0476782,
               'V':99.06841360,
               'W':186.0793126,
               'Y':163.0633282,
               'a': 71.03711360,
               'c': 103.0091854,
               'd': 115.0269428,
               'd': 129.0425928,
               'f': 147.0684136,
               'g': 57.02146360,
               'h': 137.0589116,
               'i': 113.0840636,
               'k': 128.0949626,
               'l': 113.0840636,
               'm': 131.0404854,
               'n': 114.0429272,
               'p': 97.05276360,
               'q': 128.0585772,
               'r': 156.1011106,
               's': 87.03202820,
               't': 101.0476782,
               'v': 99.06841360,
               'w': 186.0793126,
               'y': 163.0633282
               }
    for ele in list_of_protein_dicts:
        ele['mass'] = 0
        ele['m/z'] = 0
    Split_check_cal(mass_dict,list_of_protein_dicts)
    Printing(list_of_protein_dicts)

Init(list_of_protein_dicts)

