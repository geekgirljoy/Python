def NxNequals (min, max, equation):
    max+=1;
    for a in range (min,max):

        if equation is True:
            target = open(str (a) + 'Times(n)Equations.dat', 'w');
        else:
            target = open(str (a) + 'Times(n).dat', 'w');
    
        for b in range (min,max):
            if equation is True:
                target.write(str (a) + ' times ' + str (b) + ' equals ' + str (a * b) + '\n');
            else:
                target.write(str (a * b) + '\n');
        
        target.close();
# end NxNequals

NxNequals(0,100, False); # generate just the multiples
NxNequals(0,100, True); # generate the multiples and include equasions in output
    
