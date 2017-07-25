import pprint

def enter_seq():
    global new_seq, seq, seq_compl,key_index
    new_seq = input("please type in your sequence in capitalized letters as 'ATGC..', or type in 'DONE' to terminate sequence loading:\n")
    if new_seq == 'DONE':
        print('Program Terminated')
        print('The stored complemented sequencies printed in below:\n')
        print('(Note:the keys in dictionary represents the # of attempted seq.entering)')
        pprint.pprint(seq_compl)
        print('-------------------------------------------------------')
        stat_seq()
        quit()
    else:
        print('The sequence just entered is:\n {}'.format(new_seq))
        ASK = input("Is this the right sequence, type Y or N to confirm:\n")
        if ASK is 'N':
            print('please check your sequence and re-type the right one')
            enter_seq()
        else:
            print('sequence in checking......')
            volid_seq(new_seq)
            key_index += 1
        enter_seq()

def stat_seq():
    global seq,seq_compl,new_seq
    length = 0
    count = {}
    for key, value in seq_compl.items():
        length = length+len(seq_compl[key])
        for gene in list(value):
            count[gene] = count.get(gene, 0)+1
    avg_len = length/len(seq_compl)
    num_seq = len(seq)
    print('The database contains {} sequences'.format(num_seq))
    print('Average length per sequence is:\t{}'.format(avg_len))
    print("The frequencies of 'A','T','G' and 'C' as following:")
    print('A: {}%'.format(count['A']/length*100))
    print('C: {}%'.format(count['C']/length*100))
    print('G: {}%'.format(count['G']/length*100))
    print('T: {}%'.format(count['T']/length*100))

def volid_seq (new_seq):
    global key_itera,seq_compl,seq, key_index
    if new_seq in seq.values():
        print('The sequence entered is already in the database, please enter another one')
        enter_seq()
    else:
        inde = 0
        compl_control={'T':'A','G':'C','C':'G','A':'T'}
        new_compl='';
        for ele in list(new_seq):
            seq['{}'.format(key_index)] = ''
            seq_compl['{}'.format(key_index)] = ''
            if ele in ['T','A','G','C']:
               inde +=1; # This is the index for each element in current sequence
               new_compl = new_compl+(compl_control[ele])
               seq['{}'.format(key_index)] = new_seq
               seq_compl['{}'.format(key_index)] = new_compl
            else:
               del seq['{}'.format(key_index)]
               del seq_compl['{}'.format(key_index)]
               print('The sequence entered has an error nucletide at index {} for a {}'.format(inde, ele))
               break;

seq = {}
seq_compl = {}
key_index=0
enter_seq()

