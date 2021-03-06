# Created by pyp2rpm-3.1.3
%global pypi_name murmurhash

Name:           python-%{pypi_name}
Version:        0.26.4
Release:        1%{?dist}
Summary:        Cython bindings for MurmurHash2

License:        MIT
URL:            https://github.com/spacy-io/murmurhash
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
Cython bindings for MurmurHash2

%package -n     python2-%{pypi_name}
Summary:        Cython bindings for MurmurHash2
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Cython bindings for MurmurHash2

%package -n     python3-%{pypi_name}
Summary:        Cython bindings for MurmurHash2
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Cython bindings for MurmurHash2


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
* Fri Nov 11 2016 David Goerger - 0.26.4-1
- Initial package.