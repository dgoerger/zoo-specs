# Created by pyp2rpm-3.1.3
%global pypi_name pandas-datareader

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Data readers extracted from the pandas codebase,should be compatible with recent pandas versions

License:        BSD License
URL:            https://github.com/pydata/pandas-datareader
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python2-requests-file
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-requests-file

%description
pandasdatareader Up to date remote data access for pandas, works for multiple
versions of pandas. Installation Install via pip.. codeblock:: shell $ pip
install pandasdatareaderUsage *In future pandas releases (0.17+)
pandasdatareader will become a dependancy and using* pandas.io.data *will be
equivalent to using* pandas_datareader.data.For now, you must replace your
imports from pandas.io ...

%package -n     python2-%{pypi_name}
Summary:        Data readers extracted from the pandas codebase,should be compatible with recent pandas versions
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-pandas
Requires:       python-requests
Requires:       python-requests-file
%description -n python2-%{pypi_name}
pandasdatareader Up to date remote data access for pandas, works for multiple
versions of pandas. Installation Install via pip.. codeblock:: shell $ pip
install pandasdatareaderUsage *In future pandas releases (0.17+)
pandasdatareader will become a dependancy and using* pandas.io.data *will be
equivalent to using* pandas_datareader.data.For now, you must replace your
imports from pandas.io ...

%package -n     python3-%{pypi_name}
Summary:        Data readers extracted from the pandas codebase,should be compatible with recent pandas versions
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-pandas
Requires:       python3-requests
Requires:       python3-requests-file
%description -n python3-%{pypi_name}
pandasdatareader Up to date remote data access for pandas, works for multiple
versions of pandas. Installation Install via pip.. codeblock:: shell $ pip
install pandasdatareaderUsage *In future pandas releases (0.17+)
pandasdatareader will become a dependancy and using* pandas.io.data *will be
equivalent to using* pandas_datareader.data.For now, you must replace your
imports from pandas.io ...


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

%py2_install

# hyphens vs underscores
mv %{buildroot}/%{python2_sitelib}/pandas_datareader %{buildroot}/%{python2_sitelib}/%{pypi_name}
mv %{buildroot}/%{python3_sitelib}/pandas_datareader %{buildroot}/%{python3_sitelib}/%{pypi_name}

%files -n python2-%{pypi_name}
%license LICENSE.md
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/pandas_datareader-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/pandas_datareader-%{version}-py?.?.egg-info

%changelog
* Thu Nov 17 2016 David Goerger - 0.2.1-1
- Initial package.
