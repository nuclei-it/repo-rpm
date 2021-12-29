#!/bin/bash
set -Eeuo pipefail

rpmdev-setuptree
cp -r * "${HOME}/rpmbuild/SOURCES/"
rpmbuild -ba nucleisys-release.spec
