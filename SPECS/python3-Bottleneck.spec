%global debug_package %{nil}

Name:           python3-Bottleneck
Version:        1.2.0
Release:        1%{?dist}
Summary:        Fast NumPy array functions written in C

Group:          Applications/Libraries
License:        Apache 2.0
URL:            https://pypi.python.org/pypi/Bottleneck
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel

%description
Bottleneck is a collection of fast NumPy array functions written in C.

%prep
%setup -q -n Bottleneck-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%{python3_sitearch}/*

%changelog
* Mon Oct 24 2016 David Goerger <its-sa@yale.edu> - 1.2.0-1
- initial package
