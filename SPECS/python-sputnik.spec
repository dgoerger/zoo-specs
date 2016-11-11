# Created by pyp2rpm-3.1.3
%global pypi_name sputnik

Name:           python-%{pypi_name}
Version:        0.9.3
Release:        1%{?dist}
Summary:        Data package manager library

License:        MIT
URL:            https://github.com/spacy-io/sputnik
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
 Sputnik: a data package manager library Sputnik is a library for managing data
packages for another library, e.g., models for a machine learning library.It
also comes with a commandline interface, run sputnik help or python m sputnik
help for assistance.Sputnik is a pure Python library licensed under MIT, has
minimal dependencies (only semver) and is compatible with python >2.6 and >3.3
on ...

%package -n     python2-%{pypi_name}
Summary:        Data package manager library
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-semver
Requires:       python-setuptools
%description -n python2-%{pypi_name}
 Sputnik: a data package manager library Sputnik is a library for managing data
packages for another library, e.g., models for a machine learning library.It
also comes with a commandline interface, run sputnik help or python m sputnik
help for assistance.Sputnik is a pure Python library licensed under MIT, has
minimal dependencies (only semver) and is compatible with python >2.6 and >3.3
on ...

%package -n     python3-%{pypi_name}
Summary:        Data package manager library
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-semver
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
 Sputnik: a data package manager library Sputnik is a library for managing data
packages for another library, e.g., models for a machine learning library.It
also comes with a commandline interface, run sputnik help or python m sputnik
help for assistance.Sputnik is a pure Python library licensed under MIT, has
minimal dependencies (only semver) and is compatible with python >2.6 and >3.3
on ...


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
cp %{buildroot}/%{_bindir}/sputnik %{buildroot}/%{_bindir}/sputnik-3
ln -sf %{_bindir}/sputnik-3 %{buildroot}/%{_bindir}/sputnik-%{python3_version}

%py2_install
cp %{buildroot}/%{_bindir}/sputnik %{buildroot}/%{_bindir}/sputnik-2
ln -sf %{_bindir}/sputnik-2 %{buildroot}/%{_bindir}/sputnik-%{python2_version}


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/sputnik
%{_bindir}/sputnik-2
%{_bindir}/sputnik-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/sputnik-3
%{_bindir}/sputnik-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Nov 11 2016 David Goerger - 0.9.3-1
- Initial package.