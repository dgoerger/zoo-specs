%global debug_package %{nil}

Name:           python3-lru-dict
Version:        1.1.5
Release:        1%{?dist}
Summary:        An Dict like LRU container

Group:          Applications/Libraries
License:        Apache 2.0
URL:            https://pypi.python.org/pypi/lru-dict
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel

%description
A fixed size dict like container which evicts Least Recently Used (LRU) items once size limit is exceeded. There are many python implementations available which does similar things. This is a fast and efficient C implementation. LRU maximum capacity can be modified at run-time. If you are looking for pure python version, look else where.

%prep
%setup -q -n lru-dict-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%{python3_sitearch}/*

%changelog
* Mon Oct 24 2016 David Goerger <its-sa@yale.edu> - 1.1.5-1
- initial package
