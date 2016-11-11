# Created by pyp2rpm-3.1.3
%global pypi_name cloudpickle

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Extended pickling support for Python objects

License:        LICENSE.txt
URL:            https://github.com/cloudpipe/cloudpickle
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
 cloudpickle[![Build Status]( )]( [![codecov.io]( makes it possible to
serialize Python constructs not supported by the default pickle module from the
Python standard library.cloudpickle is especially useful for cluster computing
where Python expressions are shipped over the network to execute on remote
hosts, possibly close to the data.Among other things, cloudpickle supports
pickling for ...

%package -n     python2-%{pypi_name}
Summary:        Extended pickling support for Python objects
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
 cloudpickle[![Build Status]( )]( [![codecov.io]( makes it possible to
serialize Python constructs not supported by the default pickle module from the
Python standard library.cloudpickle is especially useful for cluster computing
where Python expressions are shipped over the network to execute on remote
hosts, possibly close to the data.Among other things, cloudpickle supports
pickling for ...

%package -n     python3-%{pypi_name}
Summary:        Extended pickling support for Python objects
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 cloudpickle[![Build Status]( )]( [![codecov.io]( makes it possible to
serialize Python constructs not supported by the default pickle module from the
Python standard library.cloudpickle is especially useful for cluster computing
where Python expressions are shipped over the network to execute on remote
hosts, possibly close to the data.Among other things, cloudpickle supports
pickling for ...


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


%check
#%{__python2} setup.py test
#%{__python3} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.md
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Nov 11 2016 David Goerger - 0.2.1-1
- Initial package.
