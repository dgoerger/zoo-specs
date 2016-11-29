# Created by pyp2rpm-3.2.1
%global pypi_name multipledispatch

Name:           python-%{pypi_name}
Version:        0.4.9
Release:        1%{?dist}
Summary:        Multiple dispatch

License:        BSD
URL:            http://github.com/mrocklin/multipledispatch/
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
UNKNOWN

%package -n     python2-%{pypi_name}
Summary:        Multiple dispatch
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
UNKNOWN

%package -n     python3-%{pypi_name}
Summary:        Multiple dispatch
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
UNKNOWN


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
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Nov 23 2016 David Goerger - 0.4.9-1
- Initial package.