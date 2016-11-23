# Created by pyp2rpm-3.1.3
%global pypi_name nose-parameterized

Name:           python-%{pypi_name}
Version:        0.5.0
Release:        1%{?dist}
Summary:        Parameterized testing with any Python test framework

License:        UNKNOWN
URL:            https://github.com/wolever/nose-parameterized
Source0:        https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel

%description
Parameterized testing with any Python test framework Parameterized testing in
Python sucks.noseparameterized fixes that. For everything. Parameterized
testing for nose, parameterized testing for py.test, parameterized testing for
unittest... code:: python test_math.py from nose.tools import assert_equal from
nose_parameterized import parameterized import unittest import math
@parameterized([ ...

%package -n     python3-%{pypi_name}
Summary:        Parameterized testing with any Python test framework
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Parameterized testing with any Python test framework Parameterized testing in
Python sucks.noseparameterized fixes that. For everything. Parameterized
testing for nose, parameterized testing for py.test, parameterized testing for
unittest... code:: python test_math.py from nose.tools import assert_equal from
nose_parameterized import parameterized import unittest import math
@parameterized([ ...

%package -n     python2-%{pypi_name}
Summary:        Parameterized testing with any Python test framework
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Parameterized testing with any Python test framework Parameterized testing in
Python sucks.noseparameterized fixes that. For everything. Parameterized
testing for nose, parameterized testing for py.test, parameterized testing for
unittest... code:: python test_math.py from nose.tools import assert_equal from
nose_parameterized import parameterized import unittest import math
@parameterized([ ...


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

# sigh
mv %{buildroot}/%{python2_sitelib}/nose_parameterized %{buildroot}/%{python2_sitelib}/%{pypi_name}
mv %{buildroot}/%{python3_sitelib}/nose_parameterized %{buildroot}/%{python3_sitelib}/%{pypi_name}

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/nose_parameterized-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name}
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/nose_parameterized-%{version}-py?.?.egg-info

%changelog
* Thu Nov 17 2016 David Goerger - 0.5.0-1
- Initial package.
