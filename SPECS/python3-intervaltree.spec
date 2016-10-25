%global debug_package %{nil}

Name:           python3-intervaltree
Version:        2.1.0
Release:        1%{?dist}
Summary:        Pythonic algorithmic trading library

Group:          Applications/Libraries
License:        Apache 2.0
URL:            https://github.com/chaimleib/intervaltree
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel

%description
A mutable, self-balancing interval tree. Queries may be by point, by range overlap, or by range containment.

%prep
%setup -q -n intervaltree-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%{python3_sitelib}/*

%changelog
* Mon Oct 24 2016 David Goerger <its-sa@yale.edu> - 2.1.0-1
- initial package
