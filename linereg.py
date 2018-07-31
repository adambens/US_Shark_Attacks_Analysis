## Written by Adam Benson on 4/09/2018


def calcCoeffsErr(x, rootMeanSquareError):
    '''
    This function calculates the error on the coefficents.
    Inputs: (x) = x values of the equation + (rootMeanSquareError) RMSE on the fit. 

    Outputs the error on the slope and the y-intercept. (in that order!)

    '''
    import numpy as np
    
    delta = len(x)*sum(x**2) - (sum(x)**2)

    errSlope = rootMeanSquareError * np.sqrt((len(x)) / delta)
    errIntercept = rootMeanSquareError * np.sqrt(sum((x**2)) / delta)
    
    return(errSlope, errIntercept)
def calcRMSE(yModel, yData):
    '''
    inputs: ymodel and ydata as caculated by stats.linregress
    This calculates sigma y. 
    Outputs
    error on the fit of linear regression. 
    '''
    import numpy as np
    
    sumOfDiff = sum(((yModel - yData)**2))
    meanSquareError = (sumOfDiff / (len(yModel) - 2.0))
    
    return(np.sqrt(meanSquareError))
