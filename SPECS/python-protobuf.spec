# Created by pyp2rpm-3.1.3
%global pypi_name protobuf

Name:           %{pypi_name}
Version:        3.1.0.post1
Release:        1%{?dist}
Summary:        Protocol Buffers

License:        New BSD License
URL:            https://developers.google.com/protocol-buffers/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
Protocol Buffers are Google's data interchange format

%package -n     python2-%{pypi_name}
Summary:        Protocol Buffers
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-six >= 1.9
Requires:       python-setuptools
%description -n python2-%{pypi_name}
Protocol Buffers are Google's data interchange format

%package -n     python3-%{pypi_name}
Summary:        Protocol Buffers
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-six >= 1.9
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
Protocol Buffers are Google's data interchange format


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
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pypi_name}
%doc README.md
%{python2_sitelib}/protobuf_3.1.0.post1_py2.7_nspkg.pth
%{python2_sitelib}/google
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/protobuf_3.1.0.post1_py2.7_nspkg.pth
%{python3_sitelib}/google
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Nov 11 2016 David Goerger - 3.1.0.post1-1
- Initial package.