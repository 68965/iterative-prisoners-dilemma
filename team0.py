Line up
-------------------------------------------------------------------------------
Player 0 (P0): E0, Collude
        Always collude.
Player 1 (P1): E1, Betray
        Always betray.
Player 2 (P2): E2, Alternate
        Collude, then alternate.
Player 3 (P3): E3, Collude but retaliate
        Collude first round. Collude, except in a round after getting 
        a severe punishment.
-------------------------------------------------------------------------------
Section 1 - Player vs. Player
-------------------------------------------------------------------------------
Each column shows pts/round earned against each other player:
             P0     P1     P2     P3
vs. P0 :      0    100     50      0
vs. P1 :   -500      0   -376   -375
vs. P2 :   -250    -75      0   -199
vs. P3 :      0    -75   -199      0
TOTAL  :   -750    -50   -525   -574
-------------------------------------------------------------------------------
Section 2 - Leaderboard
-------------------------------------------------------------------------------
Average points per round:
Team name (P#):  Score      with strategy name
E1        (P1):        -13 points with Betray                                  
E2        (P2):       -132 points with Alternate                               
E3        (P3):       -144 points with Collude but retaliate                   
E0        (P0):       -188 points with Collude     
reports[3][0]
cores, moves, reports = main_play([example1, example2, team0])

                      