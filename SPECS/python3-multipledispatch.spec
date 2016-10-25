%global debug_package %{nil}

Name:           python3-multipledispatch
Version:        0.4.9
Release:        1%{?dist}
Summary:        Multiple dispatch

Group:          Applications/Libraries
License:        Apache 2.0
URL:            https://pypi.python.org/pypi/multipledispatch
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel

%description
Multiple dispatch

%prep
%setup -q -n multipledispatch-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%{python3_sitelib}/*

%changelog
* Mon Oct 24 2016 David Goerger <its-sa@yale.edu> - 0.4.9-1
- initial package
