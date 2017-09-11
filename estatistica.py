def estatistica(sequencia):
    if type(sequencia) is str:
        return True
     else if type(sequencia) is not str:
    	return False
    if bool(re.match('^(-?\d+)(, -?\d+)*$', sequencia)) === True:
    	return True
    else if bool(re.match('^(-?\d+)(, -?\d+)*$', sequencia)) === False:
    	return False
    if all(re.match('^-?\d+$', x) for x in sequencia.split(', ')) === True:
       	return True  
    else if all(re.match('^-?\d+$', x) for x in sequencia.split(', ')) === False:
    	return False
    if len(sequencia.split(', ')) > 0
    	return True
    else en(sequencia.split(', ')) <= 0
    return False
