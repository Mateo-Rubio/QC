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
    qr=QuantumRegister(2)
    qc = QuantumCircuit(qr)
    qc.x(qr[1])
    qc.h(qr[0]);qc.h(qr[1])
    return Statevector.from_instruction(qc)




def figure_it_out_2():
    """ Implement a function that passes the test, using a quantum circuit and gates only

    Args:
        None
    """
    qr=QuantumRegister(2)
    qc = QuantumCircuit(qr)
    qc.x(qr[0])
    qc.h(qr[0]);qc.h(qr[1])
    return Statevector.from_instruction(qc)


    


def figure_it_out_3():
    """ Implement a function that passes the test, using a quantum circuit and gates only

    Args:
        None
    """
    qr=QuantumRegister(2)
    qc = QuantumCircuit(qr)
    qc.x(qr[0]);qc.x(qr[1])
    qc.h(qr[0]);qc.h(qr[1])
    return Statevector.from_instruction(qc)


def figure_it_out_4():
    """ Implement a function that passes the test, using a quantum circuit and gates only

    Args:
        None
    """
    qr = QuantumRegister(2)
    qc = QuantumCircuit(qr)
    qc.h(qr[0])
    qc.cx(qr[0], qr[1])
    qc.x(qr[0])
    return Statevector.from_instruction(qc)



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
    M = np.zeros((4,4))
    M[:,0] = np.array([1 if i == 3 else 0 for i in range(4)])
    M[:,1] = np.array([1 if i == 2 else 0 for i in range(4)])
    M[:,2] = np.array([1 if i == 0 else 0 for i in range(4)])
    M[:,3] = np.array([1 if i == 1 else 0 for i in range(4)])
    return np.array([M@v])



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
    M = np.zeros((8,8))
    M[:,1] = np.array([1 if j == 7 else 0 for j in range(8)])
    M[:,3] = np.array([1 if j == 2 else 0 for j in range(8)]) 
    M[:,6] = np.array([1 if j == 3 else 0 for j in range(8)]) 
    M[:,7] = np.array([1 if j == 5 else 0 for j in range(8)])   
    return np.array([M@v])


def figure_it_out_7(init_vector):
    """ Implement a function that passes the tests. Use qiskit 'initialize'
        and then gates
    Args:
        init_vector
    """
    qr = QuantumRegister(2)
    qc = QuantumCircuit(qr)
    qc.initialize(init_vector)
    qc.cx(qr[0],qr[1])
    return Statevector.from_instruction(qc)



def figure_it_out_8(init_vector):
    """ Implement a function that passes the tests. Use qiskit 'initialize'
        and then gates
    Args:
        init_vector
    """
    qr = QuantumRegister(3)
    qc = QuantumCircuit(qr)
    qc.initialize(init_vector)
    qc.cx(qr[1], qr[0]) 
    qc.h(qr[0])
    qc.h(qr[1])
    qc.h(qr[2])
    return Statevector.from_instruction(qc)


if __name__ == '__main__':
    print(figure_it_out_1())
    print(figure_it_out_2())
    print(figure_it_out_3())
    print(figure_it_out_4())
    print(figure_it_out_5(np.array([1, 0, 0, 0])))
    print(figure_it_out_6(np.array([0, 1, 0, 0, 0, 0, 0, 0])))
    print(figure_it_out_7([1, 0, 0, 0]))
    print(figure_it_out_8([0, 0, 0, 0, 0, 0, 0, 1]))
