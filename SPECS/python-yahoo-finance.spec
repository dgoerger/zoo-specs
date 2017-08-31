# Created by pyp2rpm-3.2.1
%global pypi_name yahoo-finance

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        1%{?dist}
Summary:        Python module to get stock data from Yahoo! Finance

License:        MIT
URL:            https://github.com/lukaszbanasiak/yahoo-finance
Source0:        https://files.pythonhosted.org/packages/source/y/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
 yahoofinance Python module to get stock data from Yahoo! Finance Yahoo!
Finance backend is If this service is down or has network problems you will
receive errors from group YQL*, eg. YQLQueryError.You can monitor this service
via details From PyPI with pip:.. code:: bash $ pip install yahoofinanceFrom
development repo (requires git).. code:: bash $ git clone $ cd yahoofinance $
python ...

%package -n     python2-%{pypi_name}
Summary:        Python module to get stock data from Yahoo! Finance
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       pytz
Requires:       python-simplejson
Requires:       python-setuptools
%description -n python2-%{pypi_name}
 yahoofinance Python module to get stock data from Yahoo! Finance Yahoo!
Finance backend is If this service is down or has network problems you will
receive errors from group YQL*, eg. YQLQueryError.You can monitor this service
via details From PyPI with pip:.. code:: bash $ pip install yahoofinanceFrom
development repo (requires git).. code:: bash $ git clone $ cd yahoofinance $
python ...

%package -n     python3-%{pypi_name}
Summary:        Python module to get stock data from Yahoo! Finance
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-pytz
Requires:       python3-simplejson
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
 yahoofinance Python module to get stock data from Yahoo! Finance Yahoo!
Finance backend is If this service is down or has network problems you will
receive errors from group YQL*, eg. YQLQueryError.You can monitor this service
via details From PyPI with pip:.. code:: bash $ pip install yahoofinanceFrom
development repo (requires git).. code:: bash $ git clone $ cd yahoofinance $
python ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install
cp %{buildroot}/%{_bindir}/yahoo-finance %{buildroot}/%{_bindir}/yahoo-finance-3
ln -sf %{_bindir}/yahoo-finance-3 %{buildroot}/%{_bindir}/yahoo-finance-%{python3_version}

%py2_install
cp %{buildroot}/%{_bindir}/yahoo-finance %{buildroot}/%{_bindir}/yahoo-finance-2
ln -sf %{_bindir}/yahoo-finance-2 %{buildroot}/%{_bindir}/yahoo-finance-%{python2_version}


%files -n python2-%{pypi_name}
%doc README.rst
%{_bindir}/yahoo-finance
%{_bindir}/yahoo-finance-2
%{_bindir}/yahoo-finance-%{python2_version}
%{python2_sitelib}/yahoo_finance
%{python2_sitelib}/yahoo_finance-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/yahoo-finance-3
%{_bindir}/yahoo-finance-%{python3_version}
%{python3_sitelib}/yahoo_finance
%{python3_sitelib}/yahoo_finance-%{version}-py?.?.egg-info

%changelog
* Tue Jan 03 2017 David Goerger - 1.4.0-1
- Initial package.
