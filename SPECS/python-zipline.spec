# Created by pyp2rpm-3.2.1
%global pypi_name zipline

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        1%{?dist}
Summary:        A backtester for financial algorithms

License:        Apache 2.0
URL:            http://zipline.io
Source0:        https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      x86_64
 
BuildRequires:  python3-devel
BuildRequires:  python3-numpy >= 1.11.1
BuildRequires:  python3-Cython >= 0.22.1
BuildRequires:  python3-setuptools

%description


%package -n     python3-%{pypi_name}
Summary:        A backtester for financial algorithms
%{?python_provide:%python_provide python3-%{pypi_name}}

Provides:       zipline
 
Requires:       python3-pip >= 7.1.0
Requires:       python3-setuptools > 18.0
Requires:       python3-logbook >= 0.12.5
Requires:       python3-pytz >= 2016.4
Requires:       python3-numpy >= 1.11.1
Requires:       python3-requests-file >= 1.4.1
Requires:       python3-scipy >= 0.17.1
Requires:       python3-pandas >= 0.18.1
Requires:       python3-pandas < 0.19
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
Requires:       python3-numexpr >= 2.6.1
Requires:       python3-bcolz >= 0.12.1
Requires:       python3-bcolz < 1
Requires:       python3-click >= 4.0.0
Requires:       python3-toolz >= 0.8.2
Requires:       python3-multipledispatch >= 0.4.8
Requires:       python3-markupsafe >= 0.23
Requires:       python3-mako >= 1.0.1
Requires:       python3-sqlalchemy >= 1.0.8
Requires:       python3-alembic >= 0.7.7
Requires:       python3-sortedcontainers >= 1.4.4
Requires:       python3-intervaltree >= 2.1.0
Requires:       python3-lru-dict >= 1.1.4
Requires:       python3-empyrical >= 0.2.2
Requires:       python3-tables >= 3.3.0
Requires:       python3-setuptools
%description -n python3-%{pypi_name}



%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/zipline
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Jun 29 2017 David Goerger - 1.1.0-1
- Initial package.
