# Created by pyp2rpm-3.2.1
%global pypi_name empyrical

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        1%{?dist}
Summary:        empyrical is a Python library with performance and risk statistics commonly used in quantitative finance

License:        Apache License, Version 2.0
URL:            https://github.com/quantopian/empyrical
Source0:        https://files.pythonhosted.org/packages/source/e/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-nose >= 1.3.7
BuildRequires:  python3-parameterized >= 0.6.1
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-nose >= 1.3.7
BuildRequires:  python-parameterized >= 0.6.1
BuildRequires:  python-setuptools

%description
empyrical is a Python library with performance and risk statistics commonly
used in quantitative finance by Quantopian Inc_... _Quantopian Inc: ..
_Zipline: .. _pyfolio:

%package -n     python3-%{pypi_name}
Summary:        empyrical is a Python library with performance and risk statistics commonly used in quantitative finance
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-numpy >= 1.9.2
Requires:       python3-pandas >= 0.16.1
Requires:       python3-scipy >= 0.15.1
Requires:       python3-Bottleneck >= 1.0.0
%description -n python3-%{pypi_name}
empyrical is a Python library with performance and risk statistics commonly
used in quantitative finance by Quantopian Inc_... _Quantopian Inc: ..
_Zipline: .. _pyfolio:

%package -n     python2-%{pypi_name}
Summary:        empyrical is a Python library with performance and risk statistics commonly used in quantitative finance
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-numpy >= 1.9.2
Requires:       python-pandas >= 0.16.1
Requires:       python-scipy >= 0.15.1
Requires:       python-Bottleneck >= 1.0.0
%description -n python2-%{pypi_name}
empyrical is a Python library with performance and risk statistics commonly
used in quantitative finance by Quantopian Inc_... _Quantopian Inc: ..
_Zipline: .. _pyfolio:


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
%doc 
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name}
%doc 
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Jun 30 2017 David Goerger - 0.3.0-1
- Initial package.
