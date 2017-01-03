%global packname  covr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.1
Release:          1%{?dist}
Summary:          Test Coverage for Packages

Group:            Applications/Engineering 
License:          MIT + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-stats R-utils R-jsonlite R-rex R-httr R-crayon R-withr R-memoise
# Suggests:  R-R6 R-knitr R-rmarkdown R-shiny R-htmltools R-htmlwidgets R-DT R-testthat R-rstudioapi R-devtools R-xml2 R-parallel
# LinkingTo:
# Enhances:


Requires:         R-methods 
Requires:         R-stats R-utils R-jsonlite R-rex R-httr R-crayon R-withr R-memoise 
BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-stats R-utils R-jsonlite R-rex R-httr R-crayon R-withr R-memoise 

%description
Track and report code coverage for your package and (optionally) upload
the results to a coverage service like 'Codecov' (http://codecov.io) or
'Coveralls' (http://coveralls.io). Code coverage is a measure of the
amount of code being exercised by a set of tests. It is an indirect
measure of test quality and completeness. This package is compatible with
any testing methodology or framework and tracks coverage of both R code
and compiled C/C++/FORTRAN code.

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

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/www


%changelog
* Tue Dec 13 2016 deg38 <> 2.2.1-1
- initial package for Fedora
