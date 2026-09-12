import qc2
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info import Statevector, Operator
import numpy as np

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_figure_it_out_1():
    """ Tests a function 

    Args: 
        None
    """

    assert Statevector(Statevector([ 0.5+0.j,  0.5+0.j, -0.5+0.j, -0.5+0.j],dims=(2,2))).equiv(qc2.figure_it_out_1())
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_figure_it_out_2():
    """ Tests a function

    Args: 
        None
    """

    assert Statevector(Statevector([ 0.5+0.j, -0.5+0.j,  0.5+0.j, -0.5+0.j],dims=(2,2))).equiv(qc2.figure_it_out_2())
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_figure_it_out_3():
    """ Tests a function 

    Args: 
        None
    """

    assert Statevector(Statevector([ 0.5+0.j, -0.5+0.j, -0.5+0.j,  0.5+0.j])).equiv(qc2.figure_it_out_3())
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_figure_it_out_4():
    """ Tests a function 

    Args: 
        None
    """

    assert Statevector(Statevector([0.        +0.j, 0.70710678+0.j, 0.70710678+0.j, 0.        +0.j])).equiv(qc2.figure_it_out_4())
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_figure_it_out_5():
    """ Tests a function 

    Args: 
        None
    """
    
    assert np.array_equal(qc2.figure_it_out_5(np.array([1,0,0,0]) ),np.array([[0,0,0,1]] ))
    assert np.array_equal(qc2.figure_it_out_5(np.array([0,1,0,0]) ),np.array([[0,0,1,0]] ))
    assert np.array_equal(qc2.figure_it_out_5(np.array([0,0,1,0]) ),np.array([[1,0,0,0]] ))
    assert np.array_equal(qc2.figure_it_out_5(np.array([0,0,0,1]) ),np.array([[0,1,0,0]] ))
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_figure_it_out_6():
    """ Tests a function 

    Args: 
        None
    """
    assert np.array_equal(qc2.figure_it_out_6(np.array([0,1,0,0,0,0,0,0]) ),np.array([[0,0,0,0,0,0,0,1]] ))
    assert np.array_equal(qc2.figure_it_out_6(np.array([0,0,0,1,0,0,0,0]) ),np.array([[0,0,1,0,0,0,0,0]] ))
    assert np.array_equal(qc2.figure_it_out_6(np.array([0,0,0,0,0,0,1,0]) ),np.array([[0,0,0,1,0,0,0,0]] ))
    assert np.array_equal(qc2.figure_it_out_6(np.array([0,0,0,0,0,0,0,1]) ),np.array([[0,0,0,0,0,1,0,0]] ))
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_figure_it_out_7():
    """ Tests a function 

    Args: 
        None
    """
    assert Statevector(Statevector([6.12323400e-17+0.j,  1.00000000e+00+0.j, -4.26642159e-17+0.j, -2.00955151e-34+0.j])).equiv(qc2.figure_it_out_7([0,0,0,1]))
    assert Statevector(Statevector([6.123234e-17+0.j, 0.000000e+00+0.j, 1.000000e+00+0.j,  0.000000e+00+0.j])).equiv(qc2.figure_it_out_7([0,0,1,0]))
    assert Statevector(Statevector([4.26642159e-17+0.j, 0.00000000e+00+0.j, 0.00000000e+00+0.j,1.00000000e+00+0.j])).equiv(qc2.figure_it_out_7([0,1,0,0]))
    assert Statevector(Statevector([1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j])).equiv(qc2.figure_it_out_7([1,0,0,0]))

    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_figure_it_out_8():
    """ Tests a function 

    Args: 
        None
    """
                       
    assert Statevector(Statevector([ 0.35355339+0.j,  0.35355339+0.j, -0.35355339+0.j,
             -0.35355339+0.j, -0.35355339+0.j, -0.35355339+0.j,
              0.35355339+0.j,  0.35355339+0.j])).equiv(qc2.figure_it_out_8([0,0,0,0,0,0,0,1]))
    assert Statevector(Statevector([ 0.35355339+0.j, -0.35355339+0.j,  0.35355339+0.j,
             -0.35355339+0.j, -0.35355339+0.j,  0.35355339+0.j,
             -0.35355339+0.j,  0.35355339+0.j])).equiv(qc2.figure_it_out_8([0,0,0,0,0,1,0,0]))
    assert Statevector(Statevector([ 0.35355339+0.j,  0.35355339+0.j, -0.35355339+0.j,
             -0.35355339+0.j,  0.35355339+0.j,  0.35355339+0.j,
             -0.35355339+0.j, -0.35355339+0.j])).equiv(qc2.figure_it_out_8([0,0,0,1,0,0,0,0]))
    assert Statevector(Statevector([ 0.35355339+0.j, -0.35355339+0.j,  0.35355339+0.j,
             -0.35355339+0.j,  0.35355339+0.j, -0.35355339+0.j,
              0.35355339+0.j, -0.35355339+0.j])).equiv(qc2.figure_it_out_8([0,1,0,0,0,0,0,0]))

    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
if __name__ == '__main__':
    """ Run this to verify if tests are failing"""

    test_figure_it_out_1()
    test_figure_it_out_2()
    test_figure_it_out_3()
    test_figure_it_out_4()
    test_figure_it_out_5()
    test_figure_it_out_6()
    test_figure_it_out_7()
    test_figure_it_out_8()
