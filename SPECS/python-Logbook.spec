# Created by pyp2rpm-3.1.3
%global pypi_name logbook

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        A logging replacement for Python

License:        BSD
URL:            http://logbook.pocoo.org/
Source0:        https://files.pythonhosted.org/packages/source/L/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-pytest
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
An awesome logging implementation that is fun to use.Quickstart :: from logbook
import Logger log Logger('A Fancy Name') log.warn('Logbook is too awesome for
most applications') log.error("Can't touch this")Works for web apps too :: from
logbook import MailHandler, Processor mailhandler
MailHandler(from_addr'servererror@example.com',
recipients['admin@example.com'], level'ERROR', ...

%package -n     python2-%{pypi_name}
Summary:        A logging replacement for Python
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
An awesome logging implementation that is fun to use.Quickstart :: from logbook
import Logger log Logger('A Fancy Name') log.warn('Logbook is too awesome for
most applications') log.error("Can't touch this")Works for web apps too :: from
logbook import MailHandler, Processor mailhandler
MailHandler(from_addr'servererror@example.com',
recipients['admin@example.com'], level'ERROR', ...

%package -n     python3-%{pypi_name}
Summary:        A logging replacement for Python
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
An awesome logging implementation that is fun to use.Quickstart :: from logbook
import Logger log Logger('A Fancy Name') log.warn('Logbook is too awesome for
most applications') log.error("Can't touch this")Works for web apps too :: from
logbook import MailHandler, Processor mailhandler
MailHandler(from_addr'servererror@example.com',
recipients['admin@example.com'], level'ERROR', ...


%prep
%autosetup -n Logbook-%{version}
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
%doc 
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/Logbook-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc 
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/Logbook-%{version}-py?.?.egg-info

%changelog
* Thu Nov 17 2016 David Goerger - 1.0.0-1
- Initial package.
