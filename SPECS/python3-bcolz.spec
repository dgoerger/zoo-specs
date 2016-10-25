%global debug_package %{nil}

Name:           python3-bcolz
Version:        0.12.1
Release:        1%{?dist}
Summary:        Columnar and compressed data containers

Group:          Applications/Libraries
License:        Apache 2.0
URL:            https://pypi.python.org/pypi/bcolz
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel

%description
bcolz provides columnar and compressed data containers. Column storage allows for efficiently querying tables with a large number of columns. It also allows for cheap addition and removal of column. In addition, bcolz objects are compressed by default for reducing memory/disk I/O needs. The compression process is carried out internally by Blosc, a high-performance compressor that is optimized for binary data.

%prep
%setup -q -n bcolz-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%{python3_sitearch}/*

%changelog
* Mon Oct 24 2016 David Goerger <its-sa@yale.edu> - 0.12.1-1
- initial package
