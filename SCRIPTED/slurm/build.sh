#!/bin/bash

VERSION="21.08.5"

source scl_source enable devtoolset-10

wget -c "https://download.schedmd.com/slurm/slurm-${VERSION}.tar.bz2"

rpmbuild -ts "slurm-${VERSION}.tar.bz2"
yum-builddep /root/rpmbuild/SRPMS/*.rpm
yum -y install mysql-devel pkgconfig hwloc-devel mumactl-devel ucx-devel http-parser-devel json-c-devel lua-devel hdf5-devel lz4-devel
rpmbuild -ta "slurm-${VERSION}.tar.bz2" --with slurmrestd --with slurmsmwd --with hdf5 --with hwloc --with lua --with mysql --with numa --with ucx

