# Nuclei System Technology Public RPM Repository

## Usage

Note: Public repository is a work in progress. Stay tuned.

## Development

### Directory Structure

### Environment Setup (Docker)

```shell
pushd docker/
docker build -t repo-rpm:centos7 -f Dockerfile.centos7 .
popd
```

### Compilation

```shell
docker run --rm -it -v $(pwd):/appdata repo-rpm:centos7 bash
bash /appdata/SCRIPTED/<software>/build.sh
```

Collect the artifacts from:
- `/root/rpmbuild/RPMS/**/*.rpm`
- `/root/rpmbuild/SRPMS/*.rpm`

## License

Files, unless noted otherwise, is licensed under the MIT license.
