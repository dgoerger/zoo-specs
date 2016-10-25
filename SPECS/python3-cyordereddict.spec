%global debug_package %{nil}

Name:           python3-cyordereddict
Version:        1.0.0
Release:        1%{?dist}
Summary:        Cython collections.OrderedDict

Group:          Applications/Libraries
License:        Apache 2.0
URL:            https://pypi.python.org/pypi/cyordereddict
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel

%description
Cython implementation of Python's collections.OrderedDict

%prep
%setup -q -n cyordereddict-%{version}


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
