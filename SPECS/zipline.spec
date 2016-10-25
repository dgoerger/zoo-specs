Name:           zipline
Version:        1.0.3a
Release:        3%{?dist}
Summary:        Pythonic algorithmic trading library

Group:          Applications/Libraries
License:        Apache 2.0
URL:            https://github.com/quantopian/zipline
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel
Requires:       python3-empyrical, python3-cachetools, python3-alembic, python3-sortedcontainers, python3-multipledispatch, python3-toolz, python3-click, python3-logbook, python3-numexpr, python3-networkx, python3-contextlib2, python3-Bottleneck >= 1.0.0, python3-cyordereddict, python3-Cython, python3-statsmodels, python3-pandas >= 0.18.1, python3-lru-dict, python3-logbook >= 1.0.0, python3-bcolz == 0.12.1, python3-intervaltree, python3-pandas-datareader, python3-scipy >= 0.17.1, python3-numpy >= 1.11.1

%description
Zipline is a Pythonic algorithmic trading library. It is an event-driven system that supports both backtesting and live-trading.

%prep
%setup -q -n %{name}-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc AUTHORS LICENSE
%{python3_sitearch}/*
%{_bindir}/%{name}

%changelog
* Mon Oct 24 2016 David Goerger <its-sa@yale.edu> - 1.0.3a-3
- update to fe90cd3177a3cc25608127ece67c7bf62ef2c0f2 for newer pandas

* Mon Oct 24 2016 David Goerger <its-sa@yale.edu> - 1.0.2-1
- initial package
