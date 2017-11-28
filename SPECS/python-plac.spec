%global pypi_name plac

Name:           python-%{pypi_name}
Version:        0.9.6
Release:        2%{?dist}
Summary:        The smartest command line arguments parser in the world

License:        BSD License
URL:            https://github.com/micheles/plac
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
 
%description
Installation If you are lazy, just perform:: $ pip install placwhich will
install the module on your system (and possibly argparse too, if it is not
already installed).If you prefer to install the full distribution from source,
including the documentation, download the tarball_, unpack it and run:: $
python setup.py installin the main directory, possibly as superuser...
_tarball: $ python ...

%package -n     python3-%{pypi_name}
Summary:        The smartest command line arguments parser in the world
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Installation If you are lazy, just perform:: $ pip install placwhich will
install the module on your system (and possibly argparse too, if it is not
already installed).If you prefer to install the full distribution from source,
including the documentation, download the tarball_, unpack it and run:: $
python setup.py installin the main directory, possibly as superuser...
_tarball: $ python ...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/plac_runner.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/plac_core.py*
%{python3_sitelib}/plac_ext.py*
%{python3_sitelib}/plac_tk.py*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Nov 28 2017 David Goerger - 0.9.6-2
- cleanup and deprecate python2

* Fri Nov 11 2016 David Goerger - 0.9.6-1
- Initial package.
