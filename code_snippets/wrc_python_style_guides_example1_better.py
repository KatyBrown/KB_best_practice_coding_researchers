def print_values(n_entries, n_winners):
    '''
    Print the number of entries and winners and calculate and print
    the probability of success.
    '''
    print ('number of entries = %i' % (n_entries))
    print ('number of winners = %i' % (n_winners))
    print ("%% success = %.2f" % (n_winners / n_entries))


entries = 12
winners = 5
print_values(entries, winners)


