#!/bin/bash

VERSION="21.08.5"

wget "https://download.schedmd.com/slurm/slurm-${VERSION}.tar.bz2"
rpmbuild -ta "slurm-${VERSION}.tar.bz2" --with slurmrestd --with slurmsmwd --with hdf5 --with hwloc --with lua --with mysql --with numa --with ucx --with pmix --with nvml
