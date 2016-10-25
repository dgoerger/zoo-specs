%global debug_package %{nil}

Name:           python3-pandas-datareader
Version:        0.2.1
Release:        1%{?dist}
Summary:        Data readers extracted from the pandas codebase

Group:          Applications/Libraries
License:        Apache 2.0
URL:            https://pypi.python.org/pypi/pandas-datareader
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel
Requires:       python3-requests-file

%description
Data readers extracted from the pandas codebase, should be compatible with recent pandas versions.

%prep
%setup -q -n pandas-datareader-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%{python3_sitelib}/*

%changelog
* Mon Oct 24 2016 David Goerger <its-sa@yale.edu> - 0.2.1-1
- initial package
