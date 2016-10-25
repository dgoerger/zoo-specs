%global debug_package %{nil}

Name:           python3-sortedcontainers
Version:        1.5.4
Release:        1%{?dist}
Summary:        Improved sorting for python

Group:          Applications/Libraries
License:        Apache 2.0
URL:            https://pypi.python.org/pypi/sortedcontainers
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel

%description
Python's standard library is great until you need a sorted collections type. Many will attest that you can get really far without one, but the moment you really need a sorted list, dict, or set, you're faced with a dozen different implementations, most using C-extensions without great documentation and benchmarking.

%prep
%setup -q -n sortedcontainers-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%{python3_sitelib}/*

%changelog
* Mon Oct 24 2016 David Goerger <its-sa@yale.edu> - 1.5.4-1
- initial package
