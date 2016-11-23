# Created by pyp2rpm-3.1.3
%global pypi_name cyordereddict

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Cython implementation of Python's collections.OrderedDict

License:        MIT
URL:            https://github.com/shoyer/cyordereddict
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
**This library is obsolete!** Python 3.5's collections.OrderedDict was
rewritten in C_, and is now significantly faster than cyordereddict.OrderedDict
for almost all operations... _rewritten in C: cyordereddict The Python standard
library's OrderedDict ported to Cython. A dropin replacement that is 26x
faster.Install: pip install cyordereddictDependencies: CPython (2.6, 2.7, 3.3
or 3.4) and a ...

%package -n     python2-%{pypi_name}
Summary:        Cython implementation of Python's collections.OrderedDict
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
**This library is obsolete!** Python 3.5's collections.OrderedDict was
rewritten in C_, and is now significantly faster than cyordereddict.OrderedDict
for almost all operations... _rewritten in C: cyordereddict The Python standard
library's OrderedDict ported to Cython. A dropin replacement that is 26x
faster.Install: pip install cyordereddictDependencies: CPython (2.6, 2.7, 3.3
or 3.4) and a ...

%package -n     python3-%{pypi_name}
Summary:        Cython implementation of Python's collections.OrderedDict
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
**This library is obsolete!** Python 3.5's collections.OrderedDict was
rewritten in C_, and is now significantly faster than cyordereddict.OrderedDict
for almost all operations... _rewritten in C: cyordereddict The Python standard
library's OrderedDict ported to Cython. A dropin replacement that is 26x
faster.Install: pip install cyordereddictDependencies: CPython (2.6, 2.7, 3.3
or 3.4) and a ...


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py2_build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install

%py2_install


%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Nov 17 2016 David Goerger - 1.0.0-1
- Initial package.