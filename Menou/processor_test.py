#!/usr/bin/env python
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

print "proc %d/%d" %(rank, size)

