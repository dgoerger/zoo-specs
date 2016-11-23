# Created by pyp2rpm-3.1.3
%global pypi_name sortedcontainers

Name:           python-%{pypi_name}
Version:        1.5.4
Release:        1%{?dist}
Summary:        Python Sorted Container Types: SortedList, SortedDict, and SortedSet

License:        Apache 2.0
URL:            http://www.grantjenks.com/docs/sortedcontainers/
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python-tox
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-tox

%description
Python SortedContainers SortedContainers_ is an Apache2 licensed sorted
collections library_, written in purePython, and fast as Cextensions.Python's
standard library is great until you need a sorted collections type. Many will
attest that you can get really far without one, but the moment you **really
need** a sorted list, dict, or set, you're faced with a dozen different
implementations, ...

%package -n     python2-%{pypi_name}
Summary:        Python Sorted Container Types: SortedList, SortedDict, and SortedSet
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Python SortedContainers SortedContainers_ is an Apache2 licensed sorted
collections library_, written in purePython, and fast as Cextensions.Python's
standard library is great until you need a sorted collections type. Many will
attest that you can get really far without one, but the moment you **really
need** a sorted list, dict, or set, you're faced with a dozen different
implementations, ...

%package -n     python3-%{pypi_name}
Summary:        Python Sorted Container Types: SortedList, SortedDict, and SortedSet
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python SortedContainers SortedContainers_ is an Apache2 licensed sorted
collections library_, written in purePython, and fast as Cextensions.Python's
standard library is great until you need a sorted collections type. Many will
attest that you can get really far without one, but the moment you **really
need** a sorted list, dict, or set, you're faced with a dozen different
implementations, ...


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
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Nov 17 2016 David Goerger - 1.5.4-1
- Initial package.
