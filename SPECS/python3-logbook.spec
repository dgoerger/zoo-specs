%global debug_package %{nil}

Name:           python3-logbook
Version:        1.0.0
Release:        1%{?dist}
Summary:        A logging replacement for Python

Group:          Applications/Libraries
License:        Apache 2.0
URL:            https://pypi.python.org/pypi/Logbook
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel

%description
An awesome logging implementation that is fun to use.

%prep
%setup -q -n Logbook-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%{python3_sitearch}/*

%changelog
* Mon Oct 24 2016 David Goerger <its-sa@yale.edu> - 1.0.0-1
- initial package
