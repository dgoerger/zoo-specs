%global debug_package %{nil}

Name:           python3-empyrical
Version:        0.2.1
Release:        1%{?dist}
Summary:        Common financial risk and performance metrics

Group:          Applications/Libraries
License:        Apache 2.0
URL:            https://github.com/quantopian/empyrical
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel

%description
Common financial risk and performance metrics. Used by zipline and pyfolio.

%prep
%setup -q -n empyrical-%{version}


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
