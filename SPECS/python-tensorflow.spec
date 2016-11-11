# Created by pyp2rpm-3.1.3
%global pypi_name tensorflow

Name:           python-%{pypi_name}
Version:        0.11.0
Release:        1%{?dist}
Summary:        TensorFlow helps the tensors flow

License:        Apache 2.0
URL:            http://tensorflow.org/
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}-cp27-none-linux_x86_64.whl
Source1:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}-cp35-cp35m-linux_x86_64.whl
BuildArch:      x86_64
 
BuildRequires:  python-setuptools
BuildRequires:  python-six >= 1.10.0
BuildRequires:  python2-devel
BuildRequires:  python-mock >= 2.0.0
BuildRequires:  python-numpy >= 1.11.0
BuildRequires:  python-protobuf == 3.0.0
BuildRequires:  python-scipy >= 0.15.1
BuildRequires:  python-wheel
BuildRequires:  python-pip

BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-devel
BuildRequires:  python3-mock >= 2.0.0
BuildRequires:  python3-numpy >= 1.11.0
BuildRequires:  python3-protobuf == 3.0.0
BuildRequires:  python3-scipy >= 0.15.1
BuildRequires:  python3-wheel
BuildRequires:  python3-pip

%description
TensorFlow is an open source software library for numerical computation using data flow graphs. Nodes in the graph represent mathematical operations, while the graph edges represent the multidimensional data arrays (tensors) that flow between them. This flexible architecture lets you deploy computation to one or more CPUs or GPUs in a desktop, server, or mobile device without rewriting code. TensorFlow also includes TensorBoard, a data visualization toolkit.

%package -n     python2-%{pypi_name}
Summary:        TensorFlow helps the tensors flow
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-six >= 1.10.0
Requires:       python-mock >= 2.0.0
Requires:       python-numpy >= 1.11.0
Requires:       python-protobuf == 3.0.0
Requires:       python-wheel
%description -n python2-%{pypi_name}
tensorflow for python2

%package -n     python3-%{pypi_name}
Summary:        TensorFlow helps the tensors flow
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-six >= 1.10.0
Requires:       python3-mock >= 2.0.0
Requires:       python3-numpy >= 1.11.0
Requires:       python3-protobuf == 3.0.0
Requires:       python3-wheel
%description -n python3-%{pypi_name}
tensorflow for python3

%prep

%build

%install
pip2 install --no-deps --disable-pip-version-check -I %{SOURCE0} --root %{buildroot} --strip-file-prefix %{buildroot}
cp %{buildroot}/%{_bindir}/tensorboard %{buildroot}/%{_bindir}/tensorboard-2
ln -sf %{_bindir}/tensorboard-2 %{buildroot}/%{_bindir}/tensorboard-%{python2_version}
rm -rf %{buildroot}/%{python2_sitelib}/external
pip3 install --no-deps --disable-pip-version-check -I %{SOURCE1} --root %{buildroot} --strip-file-prefix %{buildroot}
#pip install -I dist-temp/*.whl --root %{buildroot} --strip-file-prefix %{buildroot} --disable-pip-version-check --no-deps
cp %{buildroot}/%{_bindir}/tensorboard %{buildroot}/%{_bindir}/tensorboard-3
ln -sf %{_bindir}/tensorboard-3 %{buildroot}/%{_bindir}/tensorboard-%{python3_version}
rm -rf %{buildroot}/%{python3_sitelib}/external


%check

%files -n python2-%{pypi_name}
%{_bindir}/tensorboard-2
%{_bindir}/tensorboard-%{python2_version}
%{python2_sitelib}/%{pypi_name}*

%files -n python3-%{pypi_name}
%{_bindir}/tensorboard
%{_bindir}/tensorboard-3
%{_bindir}/tensorboard-%{python3_version}
%{python3_sitelib}/%{pypi_name}*


%changelog
* Fri Nov 11 2016 David Goerger - 0.11.0-1
- Initial package.
