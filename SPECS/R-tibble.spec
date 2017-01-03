%global packname  tibble
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Simple Data Frames

Group:            Applications/Engineering 
License:          MIT + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-methods R-assertthat R-utils R-lazyeval R-Rcpp
# Suggests:  R-testthat R-withr R-knitr R-rmarkdown R-nycflights13 R-microbenchmark
# LinkingTo:
# Enhances:



Requires:         R-methods R-assertthat R-utils R-lazyeval R-Rcpp 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-methods R-assertthat R-utils R-lazyeval R-Rcpp  R-Rcpp-devel

%description
Provides a 'tbl_df' class that offers better checking and printing
capabilities than traditional data frames.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Tue Dec 13 2016 deg38 <> 1.2-1
- initial package for Fedora
