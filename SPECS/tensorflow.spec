%define debug_package %{nil}

Name:           tensorflow
Version:        0.10.0
Release:        1%{?dist}
Summary:        Computation using data flow graphs for scalable machine learning
License:        Apache License 2.0
URL:            http://www.tensorflow.org/
Source:         %{name}-%{version}.tar.gz

BuildRequires: bazel, python3-devel, python3-wheel, python3-pip, swig, gcc-c++, zlib-devel, pkgconfig
Requires:      python3-six python3-numpy
# we're bundling protobuf, rhbz#1209685
Conflicts: protobuf-python python3-protobuf

%description
TensorFlow is an open source software library for numerical computation using data flow graphs. Nodes in the graph represent mathematical operations, while the graph edges represent the multidimensional data arrays (tensors) that flow between them. This flexible architecture lets you deploy computation to one or more CPUs or GPUs in a desktop, server, or mobile device without rewriting code. TensorFlow also includes TensorBoard, a data visualization toolkit.

%prep
%setup -q
# python3
export PYTHON_BIN_PATH=/usr/bin/python3
echo -e '\nn' | ./configure

%build
export LANG=en_US.UTF-8
pushd %{name}
bazel build --verbose_failures -c opt //tensorflow/tools/pip_package:build_pip_package
popd

%check

%install
rm -rf dist-temp
bazel-bin/tensorflow/tools/pip_package/build_pip_package `pwd`/dist-temp
# work around weird error that tries to run setup.py under python2
echo "True" | tee setup.py
# install wheel per https://fedoraproject.org/wiki/PythonWheels
pip3 install -I dist-temp/*.whl --root %{buildroot} --strip-file-prefix %{buildroot} --disable-pip-version-check
# clean up files installed by the above
rm -f %{buildroot}/%{_bindir}/easy_install*
rm -f %{buildroot}/%{_bindir}/f2py
rm -f %{buildroot}/%{_bindir}/wheel
rm -rf %{buildroot}/%{python3_sitelib}/__pycache__
rm -rf %{buildroot}/%{python3_sitelib}/easy_install.py
rm -rf %{buildroot}/%{python3_sitearch}/numpy*
rm -rf %{buildroot}/%{python3_sitelib}/pkg_resources
rm -rf %{buildroot}/%{python3_sitelib}/setuptools*
rm -rf %{buildroot}/%{python3_sitelib}/six*
rm -rf %{buildroot}/%{python3_sitelib}/wheel*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/tensorboard
%{python3_sitelib}/%{name}
%{python3_sitelib}/external
%{python3_sitelib}/google
%{python3_sitelib}/%{name}-%{version}.dist-info
# bundle protobuf because rhbz#1209685
%{python3_sitelib}/protobuf-3.0.0b2-py2.7-nspkg.pth
%{python3_sitelib}/protobuf-3.0.0b2.dist-info

%changelog
* Fri Nov 04 2016 David Goerger <its-sa@yale.edu> - 0.10.0-1
- update to 0.10.0
- refactor install section to install the libs instead of a wheel package
- switch to python3

* Wed Jun 15 2016 alonid <unknown@fedoraproject.org> - 0.8.0-2
- initial packaging https://copr.fedorainfracloud.org/coprs/alonid/tensorflow
