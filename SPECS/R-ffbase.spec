%global packname  ffbase
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.12.3
Release:          1%{?dist}
Summary:          Basic Statistical Functions for Package 'ff'

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-ff
# Imports:   R-fastmatch R-bit
# Suggests:  R-testthat R-parallel R-LaF R-biglm
# LinkingTo:
# Enhances:


Requires:         R-ff 
Requires:         R-fastmatch R-bit 
Requires:         R-testthat R-parallel R-LaF R-biglm R-R6
BuildRequires:    R-devel tex(latex) R-ff
BuildRequires:    R-fastmatch R-bit 
BuildRequires:   R-testthat R-parallel R-LaF R-biglm R-R6

%description
Extends the out of memory vectors of 'ff' with statistical functions and
other utilities to ease their usage.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Tue Dec 13 2016 deg38 <> 0.12.3-1
- initial package for Fedora
