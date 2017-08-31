# Created by pyp2rpm-3.2.1
%global pypi_name parameterized

Name:           python-%{pypi_name}
Version:        0.6.1
Release:        1%{?dist}
Summary:        Parameterized testing with any Python test framework

License:        FreeBSD
URL:            https://github.com/wolever/parameterized
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
Parameterized testing with any Python test framework Parameterized testing in
Python sucks.parameterized fixes that. For everything. Parameterized testing
for nose, parameterized testing for py.test, parameterized testing for
unittest... code:: python test_math.py from nose.tools import assert_equal from
parameterized import parameterized import unittest import math @parameterized([
(2, 2, 4), ...

%package -n     python3-%{pypi_name}
Summary:        Parameterized testing with any Python test framework
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Parameterized testing with any Python test framework Parameterized testing in
Python sucks.parameterized fixes that. For everything. Parameterized testing
for nose, parameterized testing for py.test, parameterized testing for
unittest... code:: python test_math.py from nose.tools import assert_equal from
parameterized import parameterized import unittest import math @parameterized([
(2, 2, 4), ...

%package -n     python2-%{pypi_name}
Summary:        Parameterized testing with any Python test framework
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Parameterized testing with any Python test framework Parameterized testing in
Python sucks.parameterized fixes that. For everything. Parameterized testing
for nose, parameterized testing for py.test, parameterized testing for
unittest... code:: python test_math.py from nose.tools import assert_equal from
parameterized import parameterized import unittest import math @parameterized([
(2, 2, 4), ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
%py2_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py2_install

%py3_install


%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Jun 30 2017 David Goerger - 0.6.1-1
- Initial package.
