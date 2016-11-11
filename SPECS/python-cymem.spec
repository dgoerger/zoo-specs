# Created by pyp2rpm-3.1.3
%global pypi_name cymem

Name:           python-%{pypi_name}
Version:        1.31.2
Release:        1%{?dist}
Summary:        Manage calls to calloc/free through Cython

License:        MIT
URL:            https://github.com/spacy-io/cymem
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
Cython Memory Helper cymem provides two small memorymanagement helpers for
Cython. They make it easy to tie memory to a Python object's lifecycle, so that
the memory is freed when the object is garbage collected.The most useful is
cymem.Pool, which acts as a thin wrapper around the calloc function: >>> from
cymem.cymem cimport Pool >>> cdef Pool mem Pool() >>> data1 <int*>mem.alloc(10,
...

%package -n     python2-%{pypi_name}
Summary:        Manage calls to calloc/free through Cython
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Cython Memory Helper cymem provides two small memorymanagement helpers for
Cython. They make it easy to tie memory to a Python object's lifecycle, so that
the memory is freed when the object is garbage collected.The most useful is
cymem.Pool, which acts as a thin wrapper around the calloc function: >>> from
cymem.cymem cimport Pool >>> cdef Pool mem Pool() >>> data1 <int*>mem.alloc(10,
...

%package -n     python3-%{pypi_name}
Summary:        Manage calls to calloc/free through Cython
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Cython Memory Helper cymem provides two small memorymanagement helpers for
Cython. They make it easy to tie memory to a Python object's lifecycle, so that
the memory is freed when the object is garbage collected.The most useful is
cymem.Pool, which acts as a thin wrapper around the calloc function: >>> from
cymem.cymem cimport Pool >>> cdef Pool mem Pool() >>> data1 <int*>mem.alloc(10,
...


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
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Nov 11 2016 David Goerger - 1.31.2-1
- Initial package.