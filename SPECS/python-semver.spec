# Created by pyp2rpm-3.1.3
%global pypi_name semver

Name:           python-%{pypi_name}
Version:        2.7.2
Release:        1%{?dist}
Summary:        Python helper for Semantic Versioning (http://semver.org/)

License:        BSD
URL:            https://github.com/k-bx/python-semver
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-tox
BuildRequires:  python-virtualenv
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-tox
BuildRequires:  python3-virtualenv

%description
Semver |latestversion| |buildstatus| |pythonsupport| |downloads| |license|A
Python module for semantic versioning_. Simplifies comparing versions. ..
|latestversio .. |buildstatu .. |pythonsuppor .. |download .. |licens ..
_semantic versioning: This module provides just couple of functions, main of
which are:.. codeblock:: python >>> import semver >>> semver.compare("1.0.0",
"2.0.0") >>> ...

%package -n     python2-%{pypi_name}
Summary:        Python helper for Semantic Versioning (http://semver.org/)
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Semver |latestversion| |buildstatus| |pythonsupport| |downloads| |license|A
Python module for semantic versioning_. Simplifies comparing versions. ..
|latestversio .. |buildstatu .. |pythonsuppor .. |download .. |licens ..
_semantic versioning: This module provides just couple of functions, main of
which are:.. codeblock:: python >>> import semver >>> semver.compare("1.0.0",
"2.0.0") >>> ...

%package -n     python3-%{pypi_name}
Summary:        Python helper for Semantic Versioning (http://semver.org/)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Semver |latestversion| |buildstatus| |pythonsupport| |downloads| |license|A
Python module for semantic versioning_. Simplifies comparing versions. ..
|latestversio .. |buildstatu .. |pythonsuppor .. |download .. |licens ..
_semantic versioning: This module provides just couple of functions, main of
which are:.. codeblock:: python >>> import semver >>> semver.compare("1.0.0",
"2.0.0") >>> ...


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

%py2_install


%files -n python2-%{pypi_name}
%doc README.rst

%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Nov 11 2016 David Goerger - 2.7.2-1
- Initial package.
