# Created by pyp2rpm-3.1.3
%global pypi_name plac

Name:           python-%{pypi_name}
Version:        0.9.6
Release:        1%{?dist}
Summary:        The smartest command line arguments parser in the world

License:        BSD License
URL:            https://github.com/micheles/plac
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel

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

%package -n     python2-%{pypi_name}
Summary:        The smartest command line arguments parser in the world
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
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
%py2_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py2_install
cp %{buildroot}/%{_bindir}/plac_runner.py %{buildroot}/%{_bindir}/plac_runner.py-2
ln -sf %{_bindir}/plac_runner.py-2 %{buildroot}/%{_bindir}/plac_runner.py-%{python2_version}

%py3_install
cp %{buildroot}/%{_bindir}/plac_runner.py %{buildroot}/%{_bindir}/plac_runner.py-3
ln -sf %{_bindir}/plac_runner.py-3 %{buildroot}/%{_bindir}/plac_runner.py-%{python3_version}


%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/plac_runner.py
%{_bindir}/plac_runner.py-3
%{_bindir}/plac_runner.py-%{python3_version}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/plac_core.py*
%{python3_sitelib}/plac_ext.py*
%{python3_sitelib}/plac_tk.py*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name}
%doc README.rst
%{_bindir}/plac_runner.py-2
%{_bindir}/plac_runner.py-%{python2_version}

%{python2_sitelib}/plac_core.py*
%{python2_sitelib}/plac_ext.py*
%{python2_sitelib}/plac_tk.py*
%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Nov 11 2016 David Goerger - 0.9.6-1
- Initial package.
