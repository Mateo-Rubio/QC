import qc1
from qiskit.quantum_info import Statevector

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_example_not():
    """ This is an example that passes a test 

    Args: 
        None
    """
    assert Statevector(Statevector([0.+0.j, 1+ 0.j],dims=(2,))).equiv(qc1.example_not())
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_hadamard():
    """ Tests hadamard gate function

    Args: 
        None
    """
    assert Statevector(Statevector([0.70710678+0.j, 0.70710678+0.j],dims=(2,))).equiv(qc1.hadamard())
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_one_state():
    """ Tests one_state function

    Args: 
        None
    """
    assert Statevector(Statevector([0+0.j, 1+0.j],dims=(2,))).equiv(qc1.one_state())
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_phase():
    """ Tests a function that returns a state with a phase of -1

    Args: 
        None
    """
    assert Statevector(Statevector([ 0.+0.j, -1.+0.j],dims=(2,))).equiv(qc1.phase())
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_figure_it_out_1():
    """ Tests a function that returns this same state vector USING GATES

    Args: 
        None
    """
    assert Statevector(Statevector([ 0.70710678+0.j, -0.70710678+0.j],dims=(2,))).equiv(qc1.figure_it_out_1())
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_figure_it_out_2():
    """ Tests a function that returns this same state vector USING GATES

    Args: 
        None
    """
    
    assert Statevector(Statevector([0.70710678+0.j , 0.5       +0.5j],dims=(2,))).equiv(qc1.figure_it_out_2())
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_figure_it_out_3():
    """ Tests a function that returns this same state vector USING GATES

    Args: 
        None
    """
    
    assert Statevector(Statevector([0.70710678+0.j , 0.69351992+0.13794969j])).equiv(qc1.figure_it_out_3())
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_figure_it_out_4():
    """ Tests a function that returns this same state vector USING GATES

    Args: 
        None
    """
    
    assert Statevector(Statevector([0.97492791+0.j        , 0.18002322+0.13079452j])).equiv(qc1.figure_it_out_4())
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
if __name__ == '__main__':
    """ Run this to verify if tests are failing"""
    test_example_not()
    test_hadamard()
    test_one_state()
    test_phase()
    test_figure_it_out_1()
    test_figure_it_out_2()
    test_figure_it_out_3()
    test_figure_it_out_4()
    
