team_name = '100'
strategy_name = 'Betray 75% of the time'
strategy_description = 'It gives a false sense that we will collude with other players'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    

    return 'c'

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+their_history+"'", "'"+my_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    if test_move(my_history='',
              their_history='', 
              my_score='',
              their_score='',
              result='b'):
         print 'Test passed'
    test_move(my_history='bbb',
              their_history='ccc', 
              my_score='', 
              their_score='',
              result='b')