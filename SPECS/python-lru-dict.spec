# Created by pyp2rpm-3.1.3
%global pypi_name lru-dict

Name:           python-%{pypi_name}
Version:        1.1.5
Release:        1%{?dist}
Summary:        An Dict like LRU container

License:        MIT
URL:            https://github.com/amitdev/lru-dict
Source0:        https://files.pythonhosted.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
A fixed size dict like container which evicts Least Recently Used (LRU) items
once size limit is exceeded. There are many python implementations available
which does similar things. This is a fast and efficient C implementation. LRU
maximum capacity can be modified at runtime. If you are looking for pure python
version, look else where < This can be used to build a LRU cache. Usage is
almost ...

%package -n     python2-%{pypi_name}
Summary:        An Dict like LRU container
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
A fixed size dict like container which evicts Least Recently Used (LRU) items
once size limit is exceeded. There are many python implementations available
which does similar things. This is a fast and efficient C implementation. LRU
maximum capacity can be modified at runtime. If you are looking for pure python
version, look else where < This can be used to build a LRU cache. Usage is
almost ...

%package -n     python3-%{pypi_name}
Summary:        An Dict like LRU container
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A fixed size dict like container which evicts Least Recently Used (LRU) items
once size limit is exceeded. There are many python implementations available
which does similar things. This is a fast and efficient C implementation. LRU
maximum capacity can be modified at runtime. If you are looking for pure python
version, look else where < This can be used to build a LRU cache. Usage is
almost ...


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
%{python2_sitearch}/lru*.so
%{python2_sitearch}/lru_dict-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/lru*.so
%{python3_sitearch}/lru_dict-%{version}-py?.?.egg-info

%changelog
* Thu Nov 17 2016 David Goerger - 1.1.5-1
- Initial package.
