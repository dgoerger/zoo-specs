# Created by pyp2rpm-3.1.3
%global pypi_name Bottleneck

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Fast NumPy array functions written in Cython

License:        Simplified BSD
URL:            http://berkeleyanalytics.com/bottleneck
Source0:        https://files.pythonhosted.org/packages/source/B/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel

%description
Bottleneck is a collection of fast NumPy array functions written in
Cython.Let's give it a try. Create a NumPy array:: >>> import numpy as np >>>
arr np.array([1, 2, np.nan, 4, 5])Find the nanmean:: >>> import bottleneck as
bn >>> bn.nanmean(arr) Moving window mean:: >>> bn.move_mean(arr, window2,
min_count1) array([ 1. , 1.5, 2. , 4. , 4.5])Benchmark Bottleneck comes with a
benchmark suite:: ...

%package -n     python3-%{pypi_name}
Summary:        Fast NumPy array functions written in Cython
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-numpy
%description -n python3-%{pypi_name}
Bottleneck is a collection of fast NumPy array functions written in
Cython.Let's give it a try. Create a NumPy array:: >>> import numpy as np >>>
arr np.array([1, 2, np.nan, 4, 5])Find the nanmean:: >>> import bottleneck as
bn >>> bn.nanmean(arr) Moving window mean:: >>> bn.move_mean(arr, window2,
min_count1) array([ 1. , 1.5, 2. , 4. , 4.5])Benchmark Bottleneck comes with a
benchmark suite:: ...

%package -n     python2-%{pypi_name}
Summary:        Fast NumPy array functions written in Cython
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-numpy
%description -n python2-%{pypi_name}
Bottleneck is a collection of fast NumPy array functions written in
Cython.Let's give it a try. Create a NumPy array:: >>> import numpy as np >>>
arr np.array([1, 2, np.nan, 4, 5])Find the nanmean:: >>> import bottleneck as
bn >>> bn.nanmean(arr) Moving window mean:: >>> bn.move_mean(arr, window2,
min_count1) array([ 1. , 1.5, 2. , 4. , 4.5])Benchmark Bottleneck comes with a
benchmark suite:: ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
%py2_build
rm -rf html/.{doctrees,buildinfo}

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py2_install

%py3_install


%files -n python3-%{pypi_name}
%license LICENSE doc/source/license.rst doc/sphinxext/LICENSE.txt bottleneck/LICENSE
%doc README.rst
%{python3_sitearch}/bottleneck
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name}
%license LICENSE doc/source/license.rst doc/sphinxext/LICENSE.txt bottleneck/LICENSE
%doc README.rst
%{python2_sitearch}/bottleneck
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Thu Nov 17 2016 David Goerger - 1.2.0-1
- Initial package.
