# Created by pyp2rpm-3.1.3
%global pypi_name pathlib

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        1%{?dist}
Summary:        Object-oriented filesystem paths

License:        MIT License
URL:            https://pathlib.readthedocs.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-sphinx
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
pathlib offers a set of classes to handle filesystem paths. It offers the
following advantages over using string objects:* No more cumbersome use of os
and os.path functions. Everything can be done easily through operators,
attribute accesses, and method calls.* Embodies the semantics of different path
types. For example, comparing Windows paths ignores casing.* Welldefined
semantics, ...

%package -n     python2-%{pypi_name}
Summary:        Object-oriented filesystem paths
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
pathlib offers a set of classes to handle filesystem paths. It offers the
following advantages over using string objects:* No more cumbersome use of os
and os.path functions. Everything can be done easily through operators,
attribute accesses, and method calls.* Embodies the semantics of different path
types. For example, comparing Windows paths ignores casing.* Welldefined
semantics, ...

%package -n     python3-%{pypi_name}
Summary:        Object-oriented filesystem paths
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pathlib offers a set of classes to handle filesystem paths. It offers the
following advantages over using string objects:* No more cumbersome use of os
and os.path functions. Everything can be done easily through operators,
attribute accesses, and method calls.* Embodies the semantics of different path
types. For example, comparing Windows paths ignores casing.* Welldefined
semantics, ...

%package -n python-%{pypi_name}-doc
Summary:        pathlib documentation
%description -n python-%{pypi_name}-doc
Documentation for pathlib

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py2_build
%py3_build
# generate html docs 
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install

%py2_install


%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.txt

%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.txt
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Fri Nov 11 2016 David Goerger - 1.0.1-1
- Initial package.