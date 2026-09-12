from qiskit import QuantumCircuit,  QuantumRegister
from qiskit.quantum_info import Statevector
from math import pi
import qiskit
import numpy as np

def figure_it_out_1():
    """ Implement a function that passes the test, using a quantum circuit and gates only

    Args:
        None
    """


def figure_it_out_2():
    """ Implement a function that passes the test, using a quantum circuit and gates only

    Args:
        None
    """


def figure_it_out_3():
    """ Implement a function that passes the test, using a quantum circuit and gates only

    Args:
        None
    """


def figure_it_out_4():
    """ Implement a function that passes the test, using a quantum circuit and gates only

    Args:
        None
    """


def figure_it_out_5(v):
    """ Implement a function that passes the test, by creating a matrix that transform the
        following inputs into the following outputs. You dont need qiskit for this,
        only numpy, such as np.matrix(...)

          input   output
          |00> : |11>
          |01> : |10>
          |10> : |00>
          |11> : |01>

    Args:
        vector that is multiplied by the matrix
    """


def figure_it_out_6(v):
    """ Implement a function that passes the test, by creating a matrix that transform the
        following inputs into the following outputs. You dont need qiskit for this,
        only numpy, such as np.matrix(...)

          input   output
          |001> : |111>
          |011> : |010>
          |110> : |011>
          |111> : |101>

    Args:
        vector that is multiplied by the matrix
    """


def figure_it_out_7(init_vector):
    """ Implement a function that passes the tests. Use qiskit 'initialize'
        and then gates
    Args:
        init_vector
    """


def figure_it_out_8(init_vector):
    """ Implement a function that passes the tests. Use qiskit 'initialize'
        and then gates
    Args:
        init_vector
    """


if __name__ == '__main__':
    print(figure_it_out_1())
    print(figure_it_out_2())
    print(figure_it_out_3())
    print(figure_it_out_4())
    print(figure_it_out_5(np.array([1, 0, 0, 0])))
    print(figure_it_out_6(np.array([0, 1, 0, 0, 0, 0, 0, 0])))
    print(figure_it_out_7([1, 0, 0, 0]))
    print(figure_it_out_8([0, 0, 0, 0, 0, 0, 0, 1]))
