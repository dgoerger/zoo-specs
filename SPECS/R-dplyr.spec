%global packname  dplyr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          A Grammar of Data Manipulation

Group:            Applications/Engineering 
License:          MIT + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-assertthat R-utils R-R6 R-Rcpp R-tibble R-magrittr R-lazyeval R-DBI
# Suggests:  R-RSQLite R-RMySQL R-RPostgreSQL R-testthat R-knitr R-microbenchmark R-ggplot2 R-mgcv R-Lahman R-nycflights13 R-methods R-rmarkdown R-covr R-dtplyr
# LinkingTo:
# Enhances:



Requires:         R-assertthat R-utils R-R6 R-Rcpp R-tibble R-magrittr R-lazyeval R-DBI 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-assertthat R-utils R-R6 R-Rcpp R-tibble R-magrittr R-lazyeval R-DBI 

%description
A fast, consistent tool for working with data frame like objects, both in
memory and out of memory.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Tue Dec 13 2016 deg38 <> 0.5.0-1
- initial package for Fedora
