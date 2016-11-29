# Created by pyp2rpm-3.2.1
%global pypi_name zipline

Name:           python-%{pypi_name}
Version:        1.0.3a
Release:        1%{?dist}
Summary:        A backtester for financial algorithms

License:        Apache 2.0
URL:            http://zipline.io
Source0:        https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python2-devel
BuildRequires:  python-numpy >= 1.9.2
BuildRequires:  python-setuptools
%if 0%{?fedora} > 24
BuildRequires:  python-Cython >= 0.22
%else
BuildRequires:  Cython >= 0.22
%endif
 
BuildRequires:  python3-devel
BuildRequires:  python3-numpy >= 1.9.2
BuildRequires:  python3-Cython >= 0.22.1
BuildRequires:  python3-setuptools

%description
Zipline is a Pythonic algorithmic trading library.
It is an event-driven system that supports both backtesting and ...

%package -n     python2-%{pypi_name}
Summary:        A backtester for financial algorithms
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-pip >= 7.1.0
Requires:       python-setuptools > 18.0
Requires:       python-logbook >= 1.0.0
Requires:       pytz >= 2015.4
Requires:       python-numpy >= 1.11.1
Requires:       python-scipy >= 0.17.1
Requires:       python-pandas >= 0.18.1
Requires:       python-pandas-datareader >= 0.2.1
Requires:       python-patsy >= 0.4.0
Requires:       python-statsmodels >= 0.6.1
Requires:       python-dateutil >= 2.4.2
Requires:       python-six >= 1.10.0
Requires:       python-requests >= 2.9.1
%if 0%{?fedora} > 24
Requires:       python-Cython >= 0.22
%else
Requires:       Cython >= 0.22
%endif
Requires:       python-cyordereddict >= 0.2.2
Requires:       python-Bottleneck >= 1.0.0
Requires:       python-contextlib2 >= 0.4.0
Requires:       python-decorator >= 4.0.0
Requires:       python-networkx >= 1.9.1
Requires:       python-numexpr >= 2.4.6
Requires:       python-bcolz < 1
Requires:       python-bcolz >= 0.12.1
Requires:       python-click >= 4.0.0
Requires:       python-toolz >= 0.7.4
Requires:       python-multipledispatch >= 0.4.8
Requires:       python-sqlalchemy >= 1.0.8
Requires:       python-alembic >= 0.7.7
Requires:       python-sortedcontainers >= 1.4.4
Requires:       python-intervaltree >= 2.1.0
Requires:       python-cachetools >= 1.1.5
Requires:       python-empyrical >= 0.1.11
Requires:       python-setuptools
%description -n python2-%{pypi_name}
Zipline is a Pythonic algorithmic trading library.
It is an event-driven system that supports both backtesting and ...

%package -n     python3-%{pypi_name}
Summary:        A backtester for financial algorithms
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-pip >= 7.1.0
Requires:       python3-setuptools > 18.0
Requires:       python3-logbook >= 1.0.0
Requires:       python3-pytz >= 2015.4
Requires:       python3-numpy >= 1.11.1
Requires:       python3-scipy >= 0.17.1
Requires:       python3-pandas >= 0.18.1
Requires:       python3-pandas-datareader >= 0.2.1
Requires:       python3-patsy >= 0.4.0
Requires:       python3-statsmodels >= 0.6.1
Requires:       python3-dateutil >= 2.4.2
Requires:       python3-six >= 1.10.0
Requires:       python3-requests >= 2.9.1
Requires:       python3-Cython >= 0.22.1
Requires:       python3-cyordereddict >= 0.2.2
Requires:       python3-Bottleneck >= 1.0.0
Requires:       python3-contextlib2 >= 0.4.0
Requires:       python3-decorator >= 4.0.0
Requires:       python3-networkx >= 1.9.1
Requires:       python3-numexpr >= 2.4.6
Requires:       python3-bcolz < 1
Requires:       python3-bcolz >= 0.12.1
Requires:       python3-click >= 4.0.0
Requires:       python3-toolz >= 0.7.4
Requires:       python3-multipledispatch >= 0.4.8
Requires:       python3-sqlalchemy >= 1.0.8
Requires:       python3-alembic >= 0.7.7
Requires:       python3-sortedcontainers >= 1.4.4
Requires:       python3-intervaltree >= 2.1.0
Requires:       python3-cachetools >= 1.1.5
Requires:       python3-empyrical >= 0.1.11
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
Zipline is a Pythonic algorithmic trading library.
It is an event-driven system that supports both backtesting and ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install
cp %{buildroot}/%{_bindir}/zipline %{buildroot}/%{_bindir}/zipline-3
ln -sf %{_bindir}/zipline-3 %{buildroot}/%{_bindir}/zipline-%{python3_version}

%py2_install
cp %{buildroot}/%{_bindir}/zipline %{buildroot}/%{_bindir}/zipline-2
ln -sf %{_bindir}/zipline-2 %{buildroot}/%{_bindir}/zipline-%{python2_version}


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/zipline
%{_bindir}/zipline-2
%{_bindir}/zipline-%{python2_version}
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/%{pypi_name}-*.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/zipline-3
%{_bindir}/zipline-%{python3_version}
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-*.egg-info

%changelog
* Wed Nov 23 2016 David Goerger - 1.0.3a-1
- Initial package.
