# Created by pyp2rpm-3.1.3
%global pypi_name bcolz

Name:           python-%{pypi_name}
Version:        0.12.1
Release:        1%{?dist}
Summary:        columnar and compressed data containers

License:        BSD
URL:            https://github.com/Blosc/bcolz
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python-setuptools
%if 0%{?fedora} > 24
BuildRequires:  python-Cython >= 0.22
%else
BuildRequires:  Cython >= 0.22
%endif
BuildRequires:  python2-devel
BuildRequires:  python-numpy >= 1.7
BuildRequires:  python-setuptools > 18.0
BuildRequires:  python-setuptools_scm > 1.5.4
BuildRequires:  python-sphinx
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython >= 0.22
BuildRequires:  python3-devel
BuildRequires:  python3-numpy >= 1.7
BuildRequires:  python3-setuptools > 18.0
BuildRequires:  python3-setuptools_scm > 1.5.4

%description
bcolz provides columnar and compressed data containers. Column storage allows
for efficiently querying tables with a large number of columns. It also allows
for cheap addition and removal of column. In addition, bcolz objects are
compressed by default for reducing memory/disk I/O needs. The compression
process is carried out internally by Blosc, a highperformance compressor that
is optimized ...

%package -n     python2-%{pypi_name}
Summary:        columnar and compressed data containers
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-numpy >= 1.7
%description -n python2-%{pypi_name}
bcolz provides columnar and compressed data containers. Column storage allows
for efficiently querying tables with a large number of columns. It also allows
for cheap addition and removal of column. In addition, bcolz objects are
compressed by default for reducing memory/disk I/O needs. The compression
process is carried out internally by Blosc, a highperformance compressor that
is optimized ...

%package -n     python3-%{pypi_name}
Summary:        columnar and compressed data containers
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-numpy >= 1.7
%description -n python3-%{pypi_name}
bcolz provides columnar and compressed data containers. Column storage allows
for efficiently querying tables with a large number of columns. It also allows
for cheap addition and removal of column. In addition, bcolz objects are
compressed by default for reducing memory/disk I/O needs. The compression
process is carried out internally by Blosc, a highperformance compressor that
is optimized ...

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


%files -n python2-%{pypi_name}
%doc bench_asv/README_asv.md c-blosc/README_HEADER.rst c-blosc/README_THREADED.rst README.rst
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc bench_asv/README_asv.md c-blosc/README_HEADER.rst c-blosc/README_THREADED.rst README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Thu Nov 17 2016 David Goerger - 0.12.1-1
- Initial package.
